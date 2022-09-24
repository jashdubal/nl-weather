## This script will make a pineapple on the Nanoleaf array

import random
import nanoleafapi as nl
import time


ips = [ "192.168.1.4"]

auths = ['0AJgQMml89aa12iAYpAqEoWKrKW18JZa']


controllers = [0] * len(ips)

# A simple for loop initializes all of the Nanoleaf objects into a list of 10
for i in range(len(ips)):
    controllers[i] = nl.Nanoleaf(ips[i], auths[i])

for controller in controllers:
    controller.set_brightness(100)

digital_twin = [0] * len(controllers)

for i, controller in enumerate(controllers):
    digital_twin[i] = nl.digital_twin.NanoleafDigitalTwin(controller)

# The following lists (and lists of lists) are the panel id's for the nanoleaf panels. This allows the values to be easily accessed.
# These value were found in an external script.
# controller0 and controller9 cont

# controller0 = [[102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90],
# [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87, 88, 89]]

# controller1 = [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 9, 10, 11, 16]

# controller2 = [44, 45, 46, 15, 19, 18, 17, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]

# controller3 = [38, 37, 36, 88, 89, 90, 91, 17, 13, 12, 11, 10, 92, 93, 94, 18, 95, 96, 41, 45, 97]

# controller4 = [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]

# controller5 = [69, 71, 78, 70, 64, 68, 85, 59, 79, 73, 80, 61, 33, 72, 67, 63, 62, 17, 65, 66, 75, 77, 31]

controller6 = [70, 52, 53, 54, 55, 56, 57, 58, 59, 17, 18, 60, 61, 62, 63, 64, 65, 66, 67, 68, 71]

# controller7 = [75, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 78, 79]

# controller8 = [69, 59, 60, 131, 38, 37, 61, 62, 63, 65, 66, 67, 22, 21, 20, 19, 68]

# controller9 = [[39, 98, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 100],
# [75, 55, 97, 96, 95, 94, 93, 92, 91, 90, 89, 10, 88]]

# digital_twin[0].set_color(78, (0, 255, 0))
# digital_twin[0].set_color(80, (0, 255, 0))
# digital_twin[0].set_color(82, (0, 255, 0))
# digital_twin[0].set_color(84, (0, 255, 0))

# the next few lines are just for setting colors in RGB
leaf = (0, 180, 0)
leaf2 = (0, 100, 0)
colorX = 200
yellow = (255, 185, 30)
brown = (80, 30, 0)
orange = (120, 50, 0)
red = (255,0,0)

# the following list comprehensions set the colors using slicing to create a repeated pattern. The specific values were
# found using trial and error on the nanoleaf array The comprehensions are separated by controller.

# [x.set_all_colors((100, 180, 255)) for x in digital_twin]


for i in range(3):
    colorX = (int(random.random()*255), int(random.random()*255), int(random.random()*255))
    colorY = (int(random.random()*255), int(random.random()*255), int(random.random()*255))

    [digital_twin[0].set_color(x, colorX) for x in controller6[4:17]]
    [digital_twin[0].set_color(x, orange) for x in controller6[4:17:3]]
    [digital_twin[0].set_color(x, colorY) for x in controller6[5:17:3]]
    [x.sync() for x in digital_twin]
    time.sleep(5)


# This final line syncs the digital twin with the actual controllers, applying everything set up before.
