"""
Written by: Prapti Sarker

Description:
    Written to display "ZETTA" and spellout zetta on u of c brand color background on a hexagon display, created with 216
    nanoleaf light panels.
    
    Each row in the display has a dedicated controller except 1st two rows and last two rows. Total there are 12 rows and 10 controllers.
    
    This code is extended from the Demo script of basic OpenAPI functionality for interacting with Nanoleaf Light Panels.
    Which Included:
    - Retrieving authentication token
    - Getting device data including orientation, panelIds, and positions of all panels
    - Activation of stream control mode
    - Building and sending of stream control frames

    Comments are to help parse the code, and simplify understanding
    
Nanoleaf Devices OpenAPI Documentation: https://forum.nanoleaf.me/docs (requires registering for a developer account)
"""

import sys
import socket  # Used to stream data to the devices when in streaming mode, in DGRAM mode to facilitate communication to a udp socket
import json  # Used to convert dictionaries to jsons and vice versa, device data is stored in a json
import time
import http.client as httplib  # Used for communication with the devices, changing modes and such
import random

API_PORT = "16021"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send is used heavily in the other functions to send the API commands needed. Read the nanoleaf open API documentation to get all of the
# possible functionality of this function!

def send(verb, endpoint, body, ip):
    '''
    Sends an API command to the Nanoleaf device at a given IP address
    '''
    LISTENER = ip + ":" + API_PORT
    try:
        conn = httplib.HTTPConnection(LISTENER)
        if len(body) != 0:
            conn.request(verb, endpoint, body, {"Content-Type": "application/json"})
        else:
            conn.request(verb, endpoint)
        response = conn.getresponse()
        body = response.read()
        return response.status, response.reason, body  # status is equivalent to the 200 phrase in the api docs,
        # reason is the text next to the number (OK, No Content, etc.) body, as defined in the line above is found using
        # the .read() method, and returns the response body as defined in the api docs.
    except (httplib.HTTPException, socket.error) as ex:
        print("Error: %s" % ex)

# these next few functions are specified commands from the open API, the "section" referred to in the docstring is
# the section of the open API that this command is in.
def getDeviceData(ip, auth):
    '''
    Gets all panel info from the Nanoleaf device, returns in the format of the API JSON in the documentation
    can be accessed using json.loads() to create a dictionary, then by using regular python dictionary syntax

    Section 4.1 "API JSON Structure > Light Panels"
    '''
    endpoint = "/api/v1/" + auth
    status, __, body = send("GET", endpoint, {}, ip)  # body is the json
    if not status == 200:
        print("could not connect: " + str(status))
        # exit(1)
    return body


def setStreamControlMode(ip, auth, version):
    '''
    Enables stream control mode on the Nanoleaf device version should be 1, all controllers need to be set to be streamed to

    Section 3.2.6.2 "External Control (extControl)" && Section 5.7 "External Control (Streaming)"
    '''
    end_point = "/api/v1/" + auth + "/effects"
    ext_control_version = "v" + str(version)
    ext_control_command = {
        'write': {'command': 'display', 'animType': 'extControl', 'extControlVersion': ext_control_version}}
    status, __, __ = send("PUT", end_point, json.dumps(ext_control_command), ip)  # json.dumps() changes the dict to
    # json format to be used by the devices
    if not (status == 200 or status == 204):
        print("could not connect: " + str(status))

# This function is how the panel data is sent to the controllers, if you
def sendStreamControlFrames(frames, ip):
    '''
    frames: An array of frames, with each frame consisting of a dictionary with the panelId and the color
    the panel must go to in the specified time. Color is specified as R, G, B and transTime (T) in multiples of 100ms.

    Section 3.2.6.2 "External Control (extControl)" && Section 5.7 "External Control (Streaming)"
    '''
    stream = bytearray()
    stream.append(len(frames) & 0xFF)
    # Port is 60221 for v1 (original Light Panels), v2 for our newer products (Shapes, Elements, Canvas)
    # this number can be found by returning the body in the setStreamControlMode function
    port = 60221
    for frame in frames:
        stream.append(frame['panelId'] & 0xFF)  # This & 0xFF term makes is so only the last 8 bytes are used,
        # not sure if it is necessary here but it doesn't hurt
        stream.append(1 & 0xFF)
        stream.append(frame['R'] & 0xFF)
        stream.append(frame['G'] & 0xFF)
        stream.append(frame['B'] & 0xFF)
        stream.append(0 & 0xFF)  # White channel is automatically controlled, no need to set it
        stream.append(frame['T'] & 0xFF)
    sock.sendto(stream, (ip, port))

# Personally never had to use the coordinates, I'm sure they'll be useful in some projects though!
def getCoordinateRange(pData):
    '''
    Utility function that returns the minimum and maximum values for x and y from the positionData JSON
    Helpful for determining the bounds of your coordinate system!
    '''
    xMin, yMin = 99999, 99999
    xMax, yMax = -99999, -99999
    for panel in pData:
        xMin = min(xMin, panel['x'])
        yMin = min(yMin, panel['y'])
        xMax = max(xMax, panel['x'])
        xMax = max(yMax, panel['y'])
    coordinateRange = {'xMin': xMin, 'yMin': yMin, 'xMax': xMax, 'yMax': yMax}
    return coordinateRange


'''
From here different animation/pattern functions are written
'''
index1 = 0  # index1 is used to change the value of green color
index2 = 0  # index2 is used to change the value of blue color
index1_flag = True  # used to increment the value of index1 by 5 if true else decrement by 5
index2_flag = True  # used to increment the value of index2 by 1 if true else decrement by 1

# This function is used for the background when displaying the white ZETTA letters
def UofCGradient(positionD):
    '''
    This function displays UofC brand color gradient on the whole display. The color gradient is in vertical direction.
    parameter: positionD
    parameter description:
        positionD is a list of lists of dictionaries, where the dictionary contain the panelID along with the position and orientation of the panel.
        In the function only the panelIDs are being used.
    '''
    frames = []  # frames is used as a list of dictionaries where each dictionary will contain the panel ID and rgb color value of the panel
    frames_final = []  # frames_final is a list of list of dictionaries, it will have a size of 10. Each element of the list will have the list of dictiontary containing panelID and rgb color value for all the panel connected to one specific controller and this will be the variable that will be return in from the function
    T = 5
    global index1
    global index2
    global index1_flag
    global index2_flag
    for i, panelData in enumerate(positionD):
        if i != 0 or i != 9:  # All the controllers that controls a dedicated row in the display
            for panel in panelData:
                R = 255
                G = 255 - index1
                B = 0 + index2
                frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                frames.append(frame)
            frames_final.append(frames)
            frames = []
        elif i == 0:
            for k, panel in enumerate(reversed(panelData)):
                if k != 0 and k < 14:
                    R = 255
                    G = 255 - index1
                    B = 0 + index2
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                    if k == 13:
                        if index1 > 160:
                            index1_flag = False
                        elif index1 <= 0:
                            index1_flag = True
                        if index2 > 30:
                            index2_flag = False
                        elif index2 <= 0:
                            index2_flag = True

                        if index1_flag == True:
                            index1 = index1 + 5
                        else:
                            index1 = index1 - 5
                        if index2_flag == True:
                            index2 = index2 + 1
                        else:
                            index2 = index2 - 1
                elif k == 0 or k > 13:
                    R = 255
                    G = 255 - index1
                    B = 0 + index2
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
            frames_final.append(frames)
            frames = []
        elif i == 9:
            for k, panel in enumerate(panelData):
                if 0 < k < 15:
                    R = 255
                    G = 255 - index1
                    B = 0 + index2
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                    if k == 14:
                        if index1 > 160:
                            index1_flag = False;
                        elif index1 <= 0:
                            index1_flag = True;
                        if index2 > 30:
                            index2_flag = False;
                        elif index2 <= 0:
                            index2_flag = True;

                        if index1_flag == True:
                            index1 = index1 + 5
                        else:
                            index1 = index1 - 5
                        if index2_flag == True:
                            index2 = index2 + 1
                        else:
                            index2 = index2 - 1
                else:
                    R = 255
                    G = 255 - index1
                    B = 0 + index2
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
            frames_final.append(frames)
            frames = []
        if index1 > 160:
            index1_flag = False;
        elif index1 <= 0:
            index1_flag = True;
        if index2 > 30:
            index2_flag = False;
        elif index2 <= 0:
            index2_flag = True;

        if index1_flag == True:
            index1 = index1 + 5
        else:
            index1 = index1 - 5
        if index2_flag == True:
            index2 = index2 + 1
        else:
            index2 = index2 - 1
    return frames_final

# ALl of the letter functions are to display the letter in white on the u of c gradient background.
def z_of_zetta(positionD):
    '''
    This function display alphabet "Z" in white on the display. The size of the alphabet is fixed and occupies the inner 6 rows of the display.
    '''

    frames = []
    frames_final = []

    # The flag_list is in this function but it is only used when the alphabet is displayed on a changing background
    # it designates which controllers have a portion of the letter, in this case the letter Z only the middle 6 controllers are needed.
    flag_list = [False, False, True, True, True, True, True, True, False, False]
    T = 5
    counter = 0  # for row 7 and 8(in otherwords controller 5 and 6) we need to light up 12th and 13th, and 10th and 11th respectively.
    # And,variable counter helps to reduce the number of lines.
    for i, panelData in enumerate(positionD):
        print(panelData)

        if i > 1 and i < 8:
            if i == 2:
                for j, panel in enumerate(panelData):
                    if j > 5 and j < 14:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
            if i == 3 or i == 4:
                for j, panel in enumerate(panelData):
                    if j == 12 or j == 13:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
            if i == 5 or i == 6:
                for j, panel in enumerate(panelData):
                    if j == 11 - counter or j == 12 - counter:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                counter = counter + 2
                frames_final.append(frames)
                frames = []
            if i == 7:
                for j, panel in enumerate(panelData):
                    if j > 6 and j < 15:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
    return [flag_list, frames_final]


def e_of_zetta(positionD):
    '''
    This function displays alphabet "E" in white on the display. The size of the alphabet is fixed and occupies the inner 6 rows of the display.
    '''
    frames = []
    frames_final = []
    flag_list = [False, False, True, True, True, True, True, True, False, False]
    T = 5
    counter = 0

    for i, panelData in enumerate(positionD):
        if i > 1 and i < 8:
            if i == 2:
                for j, panel in enumerate(panelData):
                    if j > 7 and j < 16:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
            if i == 3:
                for j, panel in enumerate(panelData):
                    if j == 8 or j == 9:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
            if i == 4:
                for j, panel in enumerate(panelData):
                    if 7 < j < 14:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
            if i == 5 or i == 6:
                for j, panel in enumerate(panelData):
                    if j == 7 - counter or j == 8 - counter:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                counter = counter + 2
                frames_final.append(frames)
                frames = []
            if i == 7:
                for j, panel in enumerate(panelData):
                    if 2 < j < 11:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
    return [flag_list, frames_final]


def t_of_zetta(positionD):
    '''
    This function display alphabet "T" in white on the display. The size of the alphabet is fixed and occupies the inner 6 rows of the display
    '''
    frames = []
    frames_final = []
    flag_list = [False, False, True, True, True, True, True, True, False, False]
    T = 5
    counter = 0

    for i, panelData in enumerate(positionD):
        if 1 < i < 8:
            if i == 2:
                for j, panel in enumerate(panelData):
                    if 3 < j < 16:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
            if i == 3 or i == 4:
                for j, panel in enumerate(panelData):
                    if j == 10 or j == 11:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
            if i == 5 or i == 6 or i == 7:
                for j, panel in enumerate(panelData):
                    if j == 9 - counter or j == 10 - counter:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                counter = counter + 2
                frames_final.append(frames)
                frames = []
    return [flag_list, frames_final]


def a_of_zetta(positionD):
    '''
    This function display alphabet "A" in white on the display. The size of the alphabet is fixed and occupies the inner 6 rows of the display
    '''
    frames = []
    frames_final = []
    flag_list = [False, True, True, True, True, True, True, True, False, False]
    T = 5

    for i, panelData in enumerate(positionD):
        if 0 < i < 8:
            if i == 1:
                for j, panel in enumerate(panelData):
                    if j == 8:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
            if i == 2:
                for j, panel in enumerate(panelData):
                    if 7 < j < 11:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
            if i == 3:
                for j, panel in enumerate(panelData):
                    if j == 8 or j == 9 or j == 11 or j == 12:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
            if i == 4:
                for j, panel in enumerate(panelData):
                    if j == 8 or j == 9 or j == 13 or j == 14:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
            if i == 5:
                for j, panel in enumerate(panelData):
                    if 6 < j < 16:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
            if i == 6:
                for j, panel in enumerate(panelData):
                    if j == 5 or j == 6 or j == 14 or j == 15:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
            if i == 7:
                for j, panel in enumerate(panelData):
                    if j == 3 or j == 4 or j == 14 or j == 15:
                        R = 255
                        G = 255
                        B = 255
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
    return [flag_list, frames_final]


# constant_color function display single random color in the whole display. However, I did not use this function.
def constant_color(positionData1, positionData2, positionData3, positionData4, positionData5, positionData6,
                   positionData7, positionData8, positionData9, positionData10):
    T = 5

    frames11 = []
    frames12 = []
    frames13 = []
    frames14 = []
    frames15 = []
    frames16 = []
    frames17 = []
    frames18 = []
    frames19 = []
    frames20 = []
    r = random.randint(5, 255)
    g = random.randint(5, 255)
    b = random.randint(5, 255)
    for x in range(len(positionData1)):
        R = r
        G = g
        B = b
        frame11 = {'panelId': positionData1[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frame20 = {'panelId': positionData10[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames11.append(frame11)
        frames20.append(frame20)
    for x in range(len(positionData2)):
        R = r
        G = g
        B = b
        frame12 = {'panelId': positionData2[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frame19 = {'panelId': positionData9[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames12.append(frame12)
        frames19.append(frame19)
    for x in range(len(positionData3)):
        R = r
        G = g
        B = b
        frame13 = {'panelId': positionData3[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frame18 = {'panelId': positionData8[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames13.append(frame13)
        frames18.append(frame18)
    for x in range(len(positionData4)):
        R = r
        G = g
        B = b
        frame14 = {'panelId': positionData4[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frame17 = {'panelId': positionData7[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames14.append(frame14)
        frames17.append(frame17)

    for x in range(len(positionData5)):
        R = r
        G = g
        B = b
        frame15 = {'panelId': positionData5[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frame16 = {'panelId': positionData6[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames15.append(frame15)
        frames16.append(frame16)

    final_frame = []
    final_frame.append(frames11)
    final_frame.append(frames12)
    final_frame.append(frames13)
    final_frame.append(frames14)
    final_frame.append(frames15)
    final_frame.append(frames16)
    final_frame.append(frames17)
    final_frame.append(frames18)
    final_frame.append(frames19)
    final_frame.append(frames20)
    return final_frame


# there are total of 6 hexagon from the center of the display. The outer ones being bigger than the inner ones
# hex_count counts the number of the those hexagon. 0 being the the largest/outer one
hex_count = 0
hex_flag = [True, True, True, True, True, True, True, True, True,
            True]  # hex_flag indicates the controllers which have all its connected panels change color


# from the function "hexagon". The controller which have all its panels color changed will
# have "false" in the same index of the hex_flag list.
def hexagon(positionD, R1, G1, B1):
    '''
    This function covers the whole display with hexagons that are color defined in the parameter, starting from the most outer one.
    parameter description: R1, G1, B1 are the rgb color that user wants.
    '''
    frames = []
    frames_final = []
    global hex_count
    global hex_flag
    for i, panelData in enumerate(positionD):
        if hex_count == 0:
            if i == 0:
                for j, panel in enumerate(panelData):
                    if (13 < j < 27) or j < 2 or j == 13 or j == 27:
                        R = R1
                        G = G1
                        B = B1
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
                hex_flag[i] = False
            if i == 9:
                for j, panel in enumerate(panelData):
                    if j > 14 or j == 14 or j == 13 or j == 27 or j == 26 or j == 0 or j == 1:
                        R = R1
                        G = G1
                        B = B1
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                frames_final.append(frames)
                frames = []
                hex_flag[i] = False
        elif hex_count > 0:
            if i < hex_count or i > (len(positionD) - 1 - hex_count):
                for j, panel in enumerate(panelData):
                    R = R1
                    G = G1
                    B = B1
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                frames_final.append(frames)
                frames = []
                hex_flag[i] = False
        for k, flag in enumerate(hex_flag):
            if flag == True:
                if k == i:
                    for j, panel in enumerate(panelData):
                        if j < 2 * (1 + hex_count) or j > len(panelData) - 1 - 2 * (1 + hex_count):
                            R = R1
                            G = G1
                            B = B1
                            frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                            frames.append(frame)
                    frames_final.append(frames)
                    frames = []
    if hex_count < 5:
        hex_count = hex_count + 1
    else:
        hex_count = 0
    return frames_final


# zetta_counter used count the index of the word "zetta". Where 0 indicate the first letter.
zetta_counter = 0


def zetta_display(positionD):
    '''
    this function displays each letter of zetta in a specific color and white background. 
    '''
    global zetta_counter
    final_frames = []
    frames = []
    for j, panelData in enumerate(positionD):
        if j == 1:
            for i, panel in enumerate(panelData):
                if zetta_counter == 1:
                    if 5 < i < 10:
                        R = 71
                        G = 166
                        B = 124
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 3:
                    if i > 11:
                        R = 237
                        G = 10
                        B = 114
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                else:
                    R = 255
                    G = 255
                    B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
            final_frames.append(frames)
            frames = []
        if j == 2:
            for i, panel in enumerate(panelData):
                if zetta_counter == 0:
                    if i < 6:
                        R = 214
                        G = 0
                        B = 28
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 1:
                    if i == 6 or i == 7:
                        R = 71
                        G = 166
                        B = 124
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 2:
                    if i > 7 and i < 14:
                        R = 255
                        G = 205
                        B = 0
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 3:
                    if i == 14 or i == 15:
                        R = 237
                        G = 10
                        B = 114
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 4:
                    if i == 16:
                        R = 255
                        G = 103
                        B = 31
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                else:
                    R = 255
                    G = 255
                    B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
            final_frames.append(frames)
            frames = []
        if j == 3:
            for i, panel in enumerate(panelData):
                if zetta_counter == 0:
                    if i == 4 or i == 5:
                        R = 214
                        G = 0
                        B = 28
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 1:
                    if 5 < i < 10:
                        R = 71
                        G = 166
                        B = 124
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 2:
                    if i == 10 or i == 11:
                        R = 255
                        G = 205
                        B = 0
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 3:
                    if i == 14 or i == 15:
                        R = 237
                        G = 10
                        B = 114
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 4:
                    if 15 < i < 19:
                        R = 255
                        G = 103
                        B = 31
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                else:
                    R = 255
                    G = 255
                    B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
            final_frames.append(frames)
            frames = []
        if j == 4:
            for i, panel in enumerate(panelData):
                if zetta_counter == 0:
                    if i == 4 or i == 5:
                        R = 214
                        G = 0
                        B = 28
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 1:
                    if i == 6 or i == 7:
                        R = 71
                        G = 166
                        B = 124
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 2:
                    if i == 10 or i == 11:
                        R = 255
                        G = 205
                        B = 0
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 3:
                    if i == 14 or i == 15:
                        R = 237
                        G = 10
                        B = 114
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 4:
                    if (15 < i < 18) or (18 < i < 21):
                        R = 255
                        G = 103
                        B = 31
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                else:
                    R = 255
                    G = 255
                    B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
            final_frames.append(frames)
            frames = []
        if j == 5:
            for i, panel in enumerate(panelData):
                if zetta_counter == 0:
                    if i == 3 or i == 4:
                        R = 214
                        G = 0
                        B = 28
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 1:
                    if 4 < i < 9:
                        R = 71
                        G = 166
                        B = 124
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 2:
                    if i == 9 or i == 10:
                        R = 255
                        G = 205
                        B = 0
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 3:
                    if i == 13 or i == 14:
                        R = 237
                        G = 10
                        B = 114
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 4:
                    if 14 < i < 22:
                        R = 255
                        G = 103
                        B = 31
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                else:
                    R = 255
                    G = 255
                    B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
            final_frames.append(frames)
            frames = []
        if j == 6:
            for i, panel in enumerate(panelData):
                if zetta_counter == 0:
                    if 0 < i < 7:
                        R = 214
                        G = 0
                        B = 28
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 2:
                    if i == 7 or i == 8:
                        R = 255
                        G = 205
                        B = 0
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                elif zetta_counter == 4:
                    if i == 13 or i == 14 or i == 20:
                        R = 255
                        G = 103
                        B = 31
                    else:
                        R = 255
                        G = 255
                        B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
                else:
                    R = 255
                    G = 255
                    B = 255
                    frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                    frames.append(frame)
            final_frames.append(frames)
            frames = []
    if zetta_counter < 4:
        zetta_counter = zetta_counter + 1
    else:
        zetta_counter = 0
    return final_frames


# seq_flag indicates which controller has all its panels lit up by the zig_zag_sequence() function
seq_flag = [True, False, False, False, False, False, False, False, False, False]
index101 = 0
index102 = 0


def zig_zig_sequence(positionD, R1, G1, B1):
    '''
    this function displays one panel in the whole display at a time. This function returns the ip address of the controller and the color of the
    panel that needs to be changed
    '''
    global index101
    global index102
    global seq_flag
    frames = []
    ip = 0
    for j, panelData in enumerate(positionD):
        if j % 2 == 0 and seq_flag[j] == True:
            if j == 0:
                for k, panel in enumerate(reversed(panelData)):
                    if index101 < 13:
                        if k != 0 and k < 14 and k <= index101 + 1:
                            R = R1
                            G = G1
                            B = B1
                            frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                            frames.append(frame)
                    elif index101 > 12:
                        if k < index101 + 1:
                            R = R1
                            G = G1
                            B = B1
                            frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                            frames.append(frame)
                ip = j
            else:
                for k, panel in enumerate(reversed(panelData)):
                    if k <= index101:
                        R = R1
                        G = G1
                        B = B1
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                ip = j
        elif seq_flag[j] == True:
            if j == 9:
                for k, panel in enumerate(panelData):
                    if index101 < 15:
                        if (k < 14 and k == index101) or (index101 == 14 and k == len(panelData) - 1):
                            R = R1
                            G = G1
                            B = B1
                            frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                            frames.append(frame)
                    elif index101 > 14:
                        if k == index101 - 1:
                            R = R1
                            G = G1
                            B = B1
                            frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                            frames.append(frame)
                ip = j
            else:
                for k, panel in enumerate(panelData):
                    if k <= index101:
                        R = R1
                        G = G1
                        B = B1
                        frame = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
                        frames.append(frame)
                ip = j
        if seq_flag[index102] == True and index101 > len(positionD[index102]) - 1:
            seq_flag[index102] = False
            if index102 < len(seq_flag) - 1:
                index102 = index102 + 1
                seq_flag[index102] = True
            index101 = 0
        elif seq_flag[j] == True and index101 < len(positionD[index102]):
            index101 = index101 + 1
    return [ip, frames]


if __name__ == "__main__":  # in python, this differentiates between importing a file as a module and running the file directly, this code will only run if the file is run directly.
    '''
    Usage: python3 nanobest.py
    '''
    '''
    all the controllers have static ip addresses. It is required to send data stream to the controller.
    '''
    ip1 = "192.168.1.14"
    ip2 = "192.168.1.13"
    ip3 = "192.168.1.12"
    ip4 = "192.168.1.10"
    ip5 = "192.168.1.11"
    ip6 = "192.168.1.9"
    ip7 = "192.168.1.4"
    ip8 = "192.168.1.5"
    ip9 = "192.168.1.28"
    ip10 = "192.168.1.2"
    ips = [ip1, ip2, ip3, ip4, ip5, ip6, ip7, ip8, ip9, ip10]

    # authentication keys are also required to establish connection. These can change if students hold the physical
    # buttons too long.
    auth1 = "LKI439ILyLPOZ73i0fOodP3rgxObe2eO"
    auth2 = "Vu9ggkGI9RNQ2SDaFPNfUIa7kX9r86nq"
    auth3 = "Q6hNMymIYPtuJmc8c3Ok4roVjFlFO3F7"
    auth4 = "Vu9ggkGI9RNQ2SDaFPNfUIa7kX9r86nq"
    auth5 = "LKI439ILyLPOZ73i0fOodP3rgxObe2eO"
    auth6 = "s4R1paJWsiccOAiy2xP39yYWSAfhNmdx"
    auth7 = "ALf4TvPrNiK4hxEVdjtbc5Gl0X2l0NCl"
    auth8 = "eRTQpXfNZh4KLdvnJXsdQMsSzspSerPu"
    auth9 = "8Wd6krYZG8bpcOkN8zvfbsFG69b2G4QL"
    auth10 = "s0M4TKH8BhTxdSIReRuAJzAHTYkHTdWU"

    # This following section loads the entire device data json into a python dictionary which can be accessed using
    # dictionary access syntax
    data1 = json.loads(getDeviceData(ip1, auth1))
    data2 = json.loads(getDeviceData(ip2, auth2))
    data3 = json.loads(getDeviceData(ip3, auth3))
    data4 = json.loads(getDeviceData(ip4, auth4))
    data5 = json.loads(getDeviceData(ip5, auth5))
    data6 = json.loads(getDeviceData(ip6, auth6))
    data7 = json.loads(getDeviceData(ip7, auth7))
    data8 = json.loads(getDeviceData(ip8, auth8))
    data9 = json.loads(getDeviceData(ip9, auth9))
    data10 = json.loads(getDeviceData(ip10, auth10))

    print("-------")

    # this position data initialization allows you to get the panel id's from the json in the controllers,
    # the panel id's are needed to access individual panels.
    # The specific dictionary syntax first accesses the panelLayout dict, then the layout dict in there, then the position data in there.
    positionData1 = data1['panelLayout']['layout']['positionData']
    positionData2 = data2['panelLayout']['layout']['positionData']
    positionData3 = data3['panelLayout']['layout']['positionData']
    positionData4 = data4['panelLayout']['layout']['positionData']
    positionData5 = data5['panelLayout']['layout']['positionData']
    positionData6 = data6['panelLayout']['layout']['positionData']
    positionData7 = data7['panelLayout']['layout']['positionData']
    positionData8 = data8['panelLayout']['layout']['positionData']
    positionData9 = data9['panelLayout']['layout']['positionData']
    positionData10 = data10['panelLayout']['layout']['positionData']

    # this has to be set to control the panels remotely
    setStreamControlMode(ip1, auth1, 1)
    setStreamControlMode(ip2, auth2, 1)
    setStreamControlMode(ip3, auth3, 1)
    setStreamControlMode(ip4, auth4, 1)
    setStreamControlMode(ip5, auth5, 1)
    setStreamControlMode(ip6, auth6, 1)
    setStreamControlMode(ip7, auth7, 1)
    setStreamControlMode(ip8, auth8, 1)
    setStreamControlMode(ip9, auth9, 1)
    setStreamControlMode(ip10, auth10, 1)

    # this next line intitializes the controllers as a list, allowing the panels to be iterated over
    positionD = [positionData1, positionData2, positionData3, positionData4, positionData5, positionData6,
                 positionData7, positionData8, positionData9, positionData10]

    # the following 10 frames will store the data for each controller to display zetta at once in the whole display
    frames1 = []
    frames2 = []
    frames3 = []
    frames4 = []
    frames5 = []
    frames6 = []
    frames7 = []
    frames8 = []
    frames9 = []
    frames10 = []

    # the next code is the snippet used in the "SimpleExample" file, it is used in this larger file to display zetta at
    # the very end of the script.

    # T sets the time for transitioning to the next color in the panels, it is in tenths of a second (transtime in the API documentation)
    T = 5

    # in the following code, each 'frame' corresponds to an individual panel, each 'frames' is a controller
    # this code displays 'ZETTA', the rgb values are done manually, but it is a good example of how to access and index individual panels
    # This code is called on line 1511 to display the coloured letters of zetta on the white background near the end of the loop

    for x in range(
            len(positionData1)):  # len(positionData1) is the number of panels connected to the controller, range makes this iterable
        R = 255
        G = 255
        B = 255
        frame1 = {'panelId': positionData1[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frame10 = {'panelId': positionData10[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames1.append(frame1)
        frames10.append(frame10)
    for panel in positionData8:
        R = 255
        G = 255
        B = 255
        frame8 = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames8.append(frame8)
    for panel in positionData9:
        R = 255
        G = 255
        B = 255
        frame9 = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames9.append(frame9)
    for i, panel in enumerate(positionData2):
        if 5 < i < 10:
            R = 71
            G = 166
            B = 124
        elif i > 11:
            R = 237
            G = 10
            B = 114
        else:
            R = 255
            G = 255
            B = 255
        frame2 = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames2.append(frame2)

    for i, panel in enumerate(positionData3):
        if i < 6:
            R = 214
            G = 0
            B = 28
        elif i == 6 or i == 7:
            R = 71
            G = 166
            B = 124
        elif 7 < i < 14:
            R = 255
            G = 205
            B = 0
        elif i == 14 or i == 15:
            R = 237
            G = 10
            B = 114
        elif i == 16:
            R = 255
            G = 103
            B = 31
        else:
            R = 255
            G = 255
            B = 255
        frame3 = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames3.append(frame3)
    for i, panel in enumerate(positionData4):
        if i == 4 or i == 5:
            R = 214
            G = 0
            B = 28
        elif 5 < i < 10:
            R = 71
            G = 166
            B = 124
        elif i == 10 or i == 11:
            R = 255
            G = 205
            B = 0
        elif i == 14 or i == 15:
            R = 237
            G = 10
            B = 114
        elif 15 < i < 19:
            R = 255
            G = 103
            B = 31
        else:
            R = 255
            G = 255
            B = 255
        frame4 = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames4.append(frame4)
    for i, panel in enumerate(positionData5):
        if i == 4 or i == 5:
            R = 214
            G = 0
            B = 28
        elif i == 6 or i == 7:
            R = 71
            G = 166
            B = 124
        elif i == 10 or i == 11:
            R = 255
            G = 205
            B = 0
        elif i == 14 or i == 15:
            R = 237
            G = 10
            B = 114
        elif (15 < i < 18) or (18 < i < 21):
            R = 255
            G = 103
            B = 31
        else:
            R = 255
            G = 255
            B = 255
        frame5 = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames5.append(frame5)

    for i, panel in enumerate(positionData6):
        if i == 3 or i == 4:
            R = 214
            G = 0
            B = 28
        elif 4 < i < 9:
            R = 71
            G = 166
            B = 124
        elif i == 9 or i == 10:
            R = 255
            G = 205
            B = 0
        elif i == 13 or i == 14:
            R = 237
            G = 10
            B = 114
        elif 14 < i < 22:
            R = 255
            G = 103
            B = 31
        else:
            R = 255
            G = 255
            B = 255
        frame6 = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames6.append(frame6)
    for i, panel in enumerate(positionData7):
        if 0 < i < 7:
            R = 214
            G = 0
            B = 28
        elif i == 7 or i == 8:
            R = 255
            G = 205
            B = 0
        elif i == 13 or i == 14 or i == 20:
            R = 255
            G = 103
            B = 31
        else:
            R = 255
            G = 255
            B = 255
        frame7 = {'panelId': panel['panelId'], 'R': R, 'G': G, 'B': B, 'T': T}
        frames7.append(frame7)

    # from here I am sending commands to the controllers using the various zetta letter functions as well as the
    # zig zag and hex functions defined above.

    # Variables are as follows:
    # while_counter: simply an index for the controllers that never resets, generally 10, one for each controller but certain functions such as the hexagon repeat fewer times than there are controllers
    # flag: boolean that states whether a given function changes a controller or not, for example, z_of_zetta only changes the middle 6 rows, so only the middle six indices are true in this, these were defined in each individual function
    # template_frame: the data for all of the panels changing color in the background, (the template on which the letters are overlayed)
    # all_data_z: the all data variables are the position data of each letter, which is contrasted with template_frame to see which panels need to be changed and which need to stay to display the letters on the changing background
    # controller index: self explanatory, the index for the controller from 0-9 (top to bottom)

    while 1:
        while_counter = 0  # while_counter controls the amount of times each animation funtion will be called
        while (while_counter < 10):
            controller_index = 0
            template_frame = UofCGradient(positionD)
            all_data_z = z_of_zetta(positionD)
            # the following nested for loop puts the letter z in uofc color gradient background
            for i, flag in enumerate(all_data_z[0]):
                if flag == True:
                    for h in all_data_z[1][controller_index]:
                        for k in template_frame[i]:
                            if h['panelId'] == k['panelId']:
                                k['R'] = h['R']
                                k['G'] = h['G']
                                k['B'] = h['B']
                    if controller_index < (len(all_data_z[1]) - 1):
                        controller_index = controller_index + 1
            # the following for loop is sending data to all the controllers
            for i in range(len(template_frame)):
                sendStreamControlFrames(template_frame[i], ips[i])
            time.sleep(5 / 10)  # a longer sleep time will keep the template_frame on the display longer
            while_counter = while_counter + 1
        '''
        will proceed to next line if while_counter is greater than 9. This loop makes the background change.
        '''
        gradient_frame = UofCGradient(positionD)
        # the following for loop will remove "Z" from the display
        for i in range(len(gradient_frame)):
            sendStreamControlFrames(gradient_frame[i], ips[i])
        time.sleep(5 / 10)
        # the following while loop will do the same to display letter E as it did for letter Z and this pattern will continue until all
        # letters of zetta are displayed

        while (while_counter < 20):
            controller_index = 0
            template_frame = UofCGradient(positionD)
            all_data_e = e_of_zetta(positionD)
            for i, flag in enumerate(all_data_e[0]):
                if flag == True:
                    for h in all_data_e[1][controller_index]:
                        for k in template_frame[i]:
                            if h['panelId'] == k['panelId']:
                                k['R'] = h['R']
                                k['G'] = h['G']
                                k['B'] = h['B']
                    if controller_index < (len(all_data_e[1]) - 1):
                        controller_index = controller_index + 1
            for i in range(len(template_frame)):
                sendStreamControlFrames(template_frame[i], ips[i])
            time.sleep(5 / 10)
            while_counter = while_counter + 1
        gradient_frame = UofCGradient(positionD)
        for i in range(len(gradient_frame)):
            sendStreamControlFrames(gradient_frame[i], ips[i])
        time.sleep(5 / 10)
        while (while_counter < 30):
            controller_index = 0
            template_frame = UofCGradient(positionD)
            all_data_t = t_of_zetta(positionD)
            for i, flag in enumerate(all_data_t[0]):
                if flag == True:
                    for h in all_data_t[1][controller_index]:
                        for k in template_frame[i]:
                            if h['panelId'] == k['panelId']:
                                k['R'] = h['R']
                                k['G'] = h['G']
                                k['B'] = h['B']
                    if controller_index < (len(all_data_t[1]) - 1):
                        controller_index = controller_index + 1
            for i in range(len(template_frame)):
                sendStreamControlFrames(template_frame[i], ips[i])
            time.sleep(5 / 10)
            while_counter = while_counter + 1
        gradient_frame = UofCGradient(positionD)
        for i in range(len(gradient_frame)):
            sendStreamControlFrames(gradient_frame[i], ips[i])
        time.sleep(5 / 10)
        while (while_counter < 40):
            controller_index = 0
            template_frame = UofCGradient(positionD)
            all_data_t = t_of_zetta(positionD)
            for i, flag in enumerate(all_data_t[0]):
                if flag == True:
                    for h in all_data_t[1][controller_index]:
                        for k in template_frame[i]:
                            if h['panelId'] == k['panelId']:
                                k['R'] = h['R']
                                k['G'] = h['G']
                                k['B'] = h['B']
                    if controller_index < (len(all_data_t[1]) - 1):
                        controller_index = controller_index + 1
            for i in range(len(template_frame)):
                sendStreamControlFrames(template_frame[i], ips[i])
            time.sleep(5 / 10)
            while_counter = while_counter + 1
        gradient_frame = UofCGradient(positionD)
        for i in range(len(gradient_frame)):
            sendStreamControlFrames(gradient_frame[i], ips[i])
        time.sleep(5 / 10)
        while (while_counter < 50):
            controller_index = 0
            template_frame = UofCGradient(positionD)
            all_data_a = a_of_zetta(positionD)
            for i, flag in enumerate(all_data_a[0]):
                if flag == True:
                    for h in all_data_a[1][controller_index]:
                        for k in template_frame[i]:
                            if h['panelId'] == k['panelId']:
                                k['R'] = h['R']
                                k['G'] = h['G']
                                k['B'] = h['B']
                    if controller_index < (len(all_data_a[1]) - 1):
                        controller_index = controller_index + 1
            for i in range(len(template_frame)):
                sendStreamControlFrames(template_frame[i], ips[i])
            time.sleep(5 / 10)
            while_counter = while_counter + 1
        gradient_frame = UofCGradient(positionD)
        for i in range(len(gradient_frame)):
            sendStreamControlFrames(gradient_frame[i], ips[i])
        time.sleep(5 / 10)
        '''
        displaying all the letters of zetta in u of c background is done and now the following loop will cover the whole display gradually
        in white, but in hexagon pattern
        '''
        while (while_counter < 56):
            hexagon_frames = hexagon(positionD, 255, 255, 255)
            for i in range(len(hexagon_frames)):
                sendStreamControlFrames(hexagon_frames[i], ips[i])
            time.sleep(5 / 10)
            while_counter = while_counter + 1
        hex_flag = [True, True, True, True, True, True, True, True, True, True]  # reseting all the hex_flag for reusablity
        #
        while (while_counter < 61):
            zettaframes = zetta_display(positionD)
            for i in range(len(zettaframes)):
                sendStreamControlFrames(zettaframes[i], ips[1 + i])
            time.sleep(10 / 10)
            while_counter = while_counter + 1
        while (while_counter < 71): # This set of commands displays the coloured letters of zetta on the white background as defined way above (line 1187), (control-f to find the definition of frames1-9 to see where)
            sendStreamControlFrames(frames1, ip1)
            sendStreamControlFrames(frames2, ip2)
            sendStreamControlFrames(frames3, ip3)
            sendStreamControlFrames(frames4, ip4)
            sendStreamControlFrames(frames5, ip5)
            sendStreamControlFrames(frames6, ip6)
            sendStreamControlFrames(frames7, ip7)
            sendStreamControlFrames(frames8, ip8)
            sendStreamControlFrames(frames9, ip9)
            sendStreamControlFrames(frames10, ip10)
            time.sleep(5 / 10)
            while_counter = while_counter + 1
        while (while_counter < 77):
            hexagon_frames = hexagon(positionD, 255, 163, 0)
            for i in range(len(hexagon_frames)):
                sendStreamControlFrames(hexagon_frames[i], ips[i])
            time.sleep(5 / 10)
            while_counter = while_counter + 1
        hex_flag = [True, True, True, True, True, True, True, True, True, True]
        while (while_counter < 294): #zig_zag_sequence takes a long time, so it is takes a lot of while counters
            zig_zag = zig_zig_sequence(positionD, 255, 255, 255)
            sendStreamControlFrames(zig_zag[1], ips[zig_zag[0]])
            time.sleep(1 / 10)
            while_counter = while_counter + 1
        seq_flag = [True, False, False, False, False, False, False, False, False, False]
        index102 = 0
        index101 = 0