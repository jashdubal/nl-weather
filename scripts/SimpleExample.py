# This file is intended as a starting point to understand the logic of the larger example file
# This file has only the necessary items to send data to the files
# all functions are defined the same as in the larger file,
# a lot of the formatting could be improved but it is totally functional

import socket
import http.client as httplib
import json


API_PORT = "16021"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def setStreamControlMode(ip, auth, version):
    '''
    Enables stream control mode on the Nanoleaf device version should be 1, all controllers need to be set to send commands
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


def send(verb, endpoint, body, ip):
    '''
    Sends an API command to the Nanoleaf device at a given IP address using the formatting in the open API
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


def getDeviceData(ip, auth):
    '''
    Gets all panel info from the Nanoleaf device, returns in the format of the API JSON in the documentation
    can be accessed using json.loads() to create a dictionary, then accessed by using regular python dictionary syntax

    Section 4.1 "API JSON Structure > Light Panels"
    '''
    endpoint = "/api/v1/" + auth
    status, __, body = send("GET", endpoint, {}, ip)  # body is the json
    if not status == 200:
        print("could not connect: " + str(status))
        # exit(1)
    return body


def sendStreamControlFrames(frames, ip):
    '''
    frames: An array of frames, with each frame consisting of a dictionary with the panelId and the color
    the panel must go to in the specified time. Color is specified as R, G, B and transTime (T) in multiples of 100ms.

    Section 3.2.6.2 "External Control (extControl)" && Section 5.7 "External Control (Streaming)"
    '''
    stream = bytearray()
    stream.append(len(frames) & 0xFF)
    # Port is 60221 for v1 (original Light Panels), v2 for newer products (Shapes, Elements, Canvas) NOT USED IN OUR ARRAY
    # this port number can be found by returning the body in the setStreamControlMode function
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

# This is where the ip's, Auth's and device data are defined
# note: these can be initialized into lists to allow loops to be used, thereby shrinking the code. They are left in this
# format as this is how it was originally written.

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

    # authentication keys are also required to establish connection. These can change if any students hold the physical
    # buttons too long,


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

# positionData gets the relevant section of the dictionary to access the panelID's try printing the whole data variable to understand this code!

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

    # this has to be set to control the panels remotely (external streaming control)
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

# This simply initializes the variables used in the following loop
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

# T sets the time for transitioning to the next color in the panels, it is in tenths of a second (transtime in the API documentation)
T=5

# in the following code, each 'frame' corresponds to an individual panel, each 'frames' is a controller
# this code displays 'ZETTA', the rgb values are done manually, but it is a good example of how to access and index individual panels
# 1-10 refer to the top-bottom controllers
# The code is imperfect and confusing in parts but should allow you to learn the syntax to send static data to the controllers

#this first loop sets the top and bottom to be white
for x in range(len(positionData1)):  # len(positionData1) is the number of panels connected to the controller, range makes this iterable for the 'for' loop
    R = 255
    G = 255
    B = 255
    frame1 = {'panelId': positionData1[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T} #positionData1[x]['panelId'] is how to access the panel id in the position data dictionary
    frame10 = {'panelId': positionData10[x]['panelId'], 'R': R, 'G': G, 'B': B, 'T': T} # these lines are formatted to send the commands to the controllers, copy this format in your own code!
    frames1.append(frame1)
    frames10.append(frame10)
for panel in positionData8: # This loop sets row 8 to white
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
for i, panel in enumerate(positionData2): # The rest of the loops go row by row, setting each colour for each letter
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


allframes = [frames1, frames2, frames3, frames4, frames5, frames6, frames7, frames8, frames9, frames10]

# this sends the frames using the function

for i, single in enumerate(allframes):
   sendStreamControlFrames(single, ips[i])