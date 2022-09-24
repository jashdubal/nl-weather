from __future__ import annotations

import random
import time
from weather import Weather


import data
from nanoleaf import Nanoleaf, PanelUpdate

nl = Nanoleaf()
nl1 = Nanoleaf()
weath = Weather()


# random hex colors
colors = ["#92ac1d", "#58f982", "#bf6070",
          "#0eff1f", "#8d2b5d", "#db684c", "#FFFFFF"]
color = "#FFFFFF"
color1 = "#F1FCFC"
colorSun = "#f3eb0c"
colorcloud = "#b8b8af"
colorRain = "#2d75ad"
colorbluesnow = "#ffffff"
colorwhitesnow = "#ffffff"


class Conditions():
    # dark blue
    UpdateSnow = [
        PanelUpdate(4, 8, colorbluesnow),
        PanelUpdate(4, 10, colorbluesnow),
        PanelUpdate(4, 12, colorbluesnow),
        PanelUpdate(4, 14, colorbluesnow),

        PanelUpdate(5, 7, colorbluesnow),
        PanelUpdate(5, 9, colorbluesnow),
        PanelUpdate(5, 11, colorbluesnow),
        PanelUpdate(5, 13, colorbluesnow),

        PanelUpdate(5, 15, colorbluesnow),

        PanelUpdate(6, 7, colorbluesnow),
        PanelUpdate(6, 9, colorbluesnow),
        PanelUpdate(6, 11, colorbluesnow),
        PanelUpdate(6, 13, colorbluesnow),
        PanelUpdate(6, 15, colorbluesnow),

        PanelUpdate(7, 8, colorbluesnow),
        PanelUpdate(7, 10, colorbluesnow),
        PanelUpdate(7, 12, colorbluesnow),
        PanelUpdate(7, 14, colorbluesnow),

        # start of white

        PanelUpdate(2, 11, colorwhitesnow),
        PanelUpdate(3, 5, colorwhitesnow),
        PanelUpdate(3, 6, colorwhitesnow),
        PanelUpdate(3, 11, colorwhitesnow),
        PanelUpdate(3, 16, colorwhitesnow),

        PanelUpdate(3, 17, colorwhitesnow),
        PanelUpdate(8, 5, colorwhitesnow),
        PanelUpdate(8, 6, colorwhitesnow),
        PanelUpdate(8, 11, colorwhitesnow),
        PanelUpdate(8, 16, colorwhitesnow),

        PanelUpdate(8, 17, colorwhitesnow),
        PanelUpdate(9, 11, colorwhitesnow)

    ]

    updateSun = [
        PanelUpdate(2, 9, colorSun),
        PanelUpdate(2, 11, colorSun),
        PanelUpdate(2, 13, colorSun),
        PanelUpdate(3, 7, colorSun),
        PanelUpdate(3, 8, colorSun),
        PanelUpdate(3, 9, colorSun),
        PanelUpdate(3, 10, colorSun),
        PanelUpdate(3, 11, colorSun),
        PanelUpdate(3, 12, colorSun),
        PanelUpdate(3, 13, colorSun),
        PanelUpdate(3, 14, colorSun),
        PanelUpdate(3, 15, colorSun),
        PanelUpdate(4, 6, colorSun),
        PanelUpdate(4, 7, colorSun),
        PanelUpdate(4, 8, colorSun),
        PanelUpdate(4, 9, colorSun),
        PanelUpdate(4, 10, colorSun),
        PanelUpdate(4, 11, colorSun),
        PanelUpdate(4, 12, colorSun),
        PanelUpdate(4, 13, colorSun),
        PanelUpdate(4, 14, colorSun),
        PanelUpdate(4, 15, colorSun),
        PanelUpdate(4, 16, colorSun),
        PanelUpdate(5, 5, colorSun),
        PanelUpdate(5, 6, colorSun),
        PanelUpdate(5, 7, colorSun),
        PanelUpdate(5, 8, colorSun),
        PanelUpdate(5, 9, colorSun),
        PanelUpdate(5, 10, colorSun),
        PanelUpdate(5, 11, colorSun),
        PanelUpdate(5, 12, colorSun),
        PanelUpdate(5, 13, colorSun),
        PanelUpdate(5, 14, colorSun),
        PanelUpdate(5, 15, colorSun),
        PanelUpdate(5, 16, colorSun),
        PanelUpdate(5, 17, colorSun),
        PanelUpdate(6, 5, colorSun),
        PanelUpdate(6, 6, colorSun),
        PanelUpdate(6, 7, colorSun),
        PanelUpdate(6, 8, colorSun),
        PanelUpdate(6, 9, colorSun),
        PanelUpdate(6, 10, colorSun),
        PanelUpdate(6, 11, colorSun),
        PanelUpdate(6, 12, colorSun),
        PanelUpdate(6, 13, colorSun),
        PanelUpdate(6, 14, colorSun),
        PanelUpdate(6, 15, colorSun),
        PanelUpdate(6, 16, colorSun),
        PanelUpdate(6, 17, colorSun),
        PanelUpdate(7, 6, colorSun),
        PanelUpdate(7, 7, colorSun),
        PanelUpdate(7, 8, colorSun),
        PanelUpdate(7, 9, colorSun),
        PanelUpdate(7, 10, colorSun),
        PanelUpdate(7, 11, colorSun),
        PanelUpdate(7, 12, colorSun),
        PanelUpdate(7, 13, colorSun),
        PanelUpdate(7, 14, colorSun),
        PanelUpdate(7, 15, colorSun),
        PanelUpdate(7, 16, colorSun),
        PanelUpdate(8, 7, colorSun),
        PanelUpdate(8, 8, colorSun),
        PanelUpdate(8, 9, colorSun),
        PanelUpdate(8, 10, colorSun),
        PanelUpdate(8, 11, colorSun),
        PanelUpdate(8, 12, colorSun),
        PanelUpdate(8, 13, colorSun),
        PanelUpdate(8, 14, colorSun),
        PanelUpdate(8, 15, colorSun),
        PanelUpdate(9, 9, colorSun),
        PanelUpdate(9, 11, colorSun),
        PanelUpdate(9, 13, colorSun)
    ]

    updateRain = [
        PanelUpdate(3, 8, colorRain),
        PanelUpdate(4, 7, colorRain),
        PanelUpdate(4, 8, colorRain),
        PanelUpdate(4, 9, colorRain),
        PanelUpdate(5, 7, colorRain),
        PanelUpdate(5, 8, colorRain),
        PanelUpdate(5, 9, colorRain),

        PanelUpdate(1, 14, colorRain),
        PanelUpdate(2, 13, colorRain),
        PanelUpdate(2, 14, colorRain),
        PanelUpdate(2, 15, colorRain),
        PanelUpdate(3, 13, colorRain),
        PanelUpdate(3, 14, colorRain),
        PanelUpdate(3, 15, colorRain),

        PanelUpdate(5, 14, colorRain),
        PanelUpdate(6, 13, colorRain),
        PanelUpdate(6, 14, colorRain),
        PanelUpdate(6, 15, colorRain),
        PanelUpdate(7, 13, colorRain),
        PanelUpdate(7, 14, colorRain),
        PanelUpdate(7, 15, colorRain),

        PanelUpdate(7, 8, colorRain),
        PanelUpdate(8, 7, colorRain),
        PanelUpdate(8, 8, colorRain),
        PanelUpdate(8, 9, colorRain),
        PanelUpdate(9, 7, colorRain),
        PanelUpdate(9, 8, colorRain),
        PanelUpdate(9, 9, colorRain)
    ]

    updatePartCloud = [
        PanelUpdate(6, 4, colorcloud),
        PanelUpdate(6, 5, colorcloud),
        PanelUpdate(6, 6, colorcloud),
        PanelUpdate(6, 7, colorcloud),
        PanelUpdate(6, 8, colorcloud),
        PanelUpdate(6, 9, colorcloud),
        PanelUpdate(6, 10, colorcloud),
        PanelUpdate(6, 11, colorcloud),
        PanelUpdate(6, 12, colorcloud),
        PanelUpdate(6, 13, colorcloud),
        PanelUpdate(6, 14, colorcloud),
        PanelUpdate(6, 15, colorcloud),
        PanelUpdate(6, 16, colorcloud),
        PanelUpdate(6, 17, colorcloud),
        PanelUpdate(6, 18, colorcloud),
        PanelUpdate(6, 19, colorcloud),
        PanelUpdate(6, 20, colorcloud),

        PanelUpdate(5, 4, colorcloud),
        PanelUpdate(5, 5, colorcloud),
        PanelUpdate(5, 6, colorcloud),
        PanelUpdate(5, 7, colorcloud),
        PanelUpdate(5, 8, colorcloud),
        PanelUpdate(5, 9, colorcloud),
        PanelUpdate(5, 10, colorcloud),
        PanelUpdate(5, 11, colorcloud),
        PanelUpdate(5, 12, colorcloud),
        PanelUpdate(5, 13, colorcloud),
        PanelUpdate(5, 14, colorcloud),
        PanelUpdate(5, 15, colorcloud),
        PanelUpdate(5, 16, colorcloud),
        PanelUpdate(5, 17, colorcloud),
        PanelUpdate(5, 18, colorcloud),
        PanelUpdate(5, 19, colorcloud),
        PanelUpdate(5, 20, colorcloud),

        PanelUpdate(4, 7, colorcloud),
        PanelUpdate(4, 8, colorcloud),
        PanelUpdate(4, 9, colorcloud),
        PanelUpdate(4, 10, colorcloud),
        PanelUpdate(4, 11, colorcloud),
        PanelUpdate(4, 12, colorcloud),
        PanelUpdate(4, 13, colorcloud),
        PanelUpdate(4, 14, colorcloud),
        PanelUpdate(4, 15, colorcloud),
        PanelUpdate(4, 16, colorcloud),
        PanelUpdate(4, 17, colorcloud),

        PanelUpdate(3, 10, colorcloud),
        PanelUpdate(3, 11, colorcloud),
        PanelUpdate(3, 12, colorcloud),
        PanelUpdate(3, 13, colorcloud),
        PanelUpdate(3, 14, colorcloud),
        # Updated Sun
        PanelUpdate(2, 11, colorSun),
        PanelUpdate(2, 12, colorSun),
        PanelUpdate(2, 13, colorSun),
        PanelUpdate(3, 7, colorSun),
        PanelUpdate(3, 8, colorSun),
        PanelUpdate(3, 9, colorSun),
        PanelUpdate(3, 10, colorSun),
        PanelUpdate(3, 11, colorSun),
        PanelUpdate(3, 12, colorSun),
        PanelUpdate(3, 13, colorSun),
        PanelUpdate(3, 14, colorSun),
        PanelUpdate(3, 15, colorSun),
        PanelUpdate(4, 6, colorSun),
        PanelUpdate(4, 7, colorSun),
        PanelUpdate(4, 8, colorSun),

        PanelUpdate(4, 14, colorSun),
        PanelUpdate(4, 15, colorSun),
        PanelUpdate(4, 16, colorSun),
        PanelUpdate(5, 5, colorSun),

        PanelUpdate(5, 17, colorSun),
        PanelUpdate(8, 7, colorSun),
        PanelUpdate(8, 8, colorSun),
        PanelUpdate(8, 9, colorSun),
        PanelUpdate(8, 10, colorSun),
        PanelUpdate(8, 11, colorSun),
        PanelUpdate(8, 12, colorSun),
        PanelUpdate(8, 13, colorSun),
        PanelUpdate(8, 14, colorSun),
        PanelUpdate(8, 15, colorSun),
        PanelUpdate(9, 11, colorSun),
        PanelUpdate(9, 12, colorSun),
        PanelUpdate(9, 13, colorSun),
        PanelUpdate(7, 3, colorcloud),
        PanelUpdate(7, 4, colorcloud),
        PanelUpdate(7, 5, colorcloud),
        PanelUpdate(7, 6, colorcloud),
        PanelUpdate(7, 7, colorcloud),
        PanelUpdate(7, 8, colorcloud),
        PanelUpdate(7, 9, colorcloud),
        PanelUpdate(7, 10, colorcloud),
        PanelUpdate(7, 11, colorcloud),
        PanelUpdate(7, 12, colorcloud),
        PanelUpdate(7, 13, colorcloud),
        PanelUpdate(7, 14, colorcloud),
        PanelUpdate(7, 15, colorcloud),
        PanelUpdate(7, 16, colorcloud),
        PanelUpdate(7, 17, colorcloud),
        PanelUpdate(7, 18, colorcloud),
        PanelUpdate(7, 19, colorcloud)

    ]

    updatecloud = [
        PanelUpdate(6, 4, colorcloud),
        PanelUpdate(6, 5, colorcloud),
        PanelUpdate(6, 6, colorcloud),
        PanelUpdate(6, 7, colorcloud),
        PanelUpdate(6, 8, colorcloud),
        PanelUpdate(6, 9, colorcloud),
        PanelUpdate(6, 10, colorcloud),
        PanelUpdate(6, 11, colorcloud),
        PanelUpdate(6, 12, colorcloud),
        PanelUpdate(6, 13, colorcloud),
        PanelUpdate(6, 14, colorcloud),
        PanelUpdate(6, 15, colorcloud),
        PanelUpdate(6, 16, colorcloud),
        PanelUpdate(6, 17, colorcloud),
        PanelUpdate(6, 18, colorcloud),
        PanelUpdate(6, 19, colorcloud),
        PanelUpdate(6, 20, colorcloud),

        PanelUpdate(5, 4, colorcloud),
        PanelUpdate(5, 5, colorcloud),
        PanelUpdate(5, 6, colorcloud),
        PanelUpdate(5, 7, colorcloud),
        PanelUpdate(5, 8, colorcloud),
        PanelUpdate(5, 9, colorcloud),
        PanelUpdate(5, 10, colorcloud),
        PanelUpdate(5, 11, colorcloud),
        PanelUpdate(5, 12, colorcloud),
        PanelUpdate(5, 13, colorcloud),
        PanelUpdate(5, 14, colorcloud),
        PanelUpdate(5, 15, colorcloud),
        PanelUpdate(5, 16, colorcloud),
        PanelUpdate(5, 17, colorcloud),
        PanelUpdate(5, 18, colorcloud),
        PanelUpdate(5, 19, colorcloud),
        PanelUpdate(5, 20, colorcloud),


        PanelUpdate(4, 7, colorcloud),
        PanelUpdate(4, 8, colorcloud),
        PanelUpdate(4, 9, colorcloud),
        PanelUpdate(4, 10, colorcloud),
        PanelUpdate(4, 11, colorcloud),
        PanelUpdate(4, 12, colorcloud),
        PanelUpdate(4, 13, colorcloud),
        PanelUpdate(4, 14, colorcloud),
        PanelUpdate(4, 15, colorcloud),
        PanelUpdate(4, 16, colorcloud),
        PanelUpdate(4, 17, colorcloud),


        PanelUpdate(3, 10, colorcloud),
        PanelUpdate(3, 11, colorcloud),
        PanelUpdate(3, 12, colorcloud),
        PanelUpdate(3, 13, colorcloud),
        PanelUpdate(3, 14, colorcloud)


    ]


class Nums():
    updatesL9 = [
        # Left 9:
        # top
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        # middle
        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),

        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 7, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        #
        PanelUpdate(4, 7, color),
        PanelUpdate(4, 8, color),
        #
        # PanelUpdate(6,5,color),
        # PanelUpdate(6,6,color),
        #
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
        # bottom right
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color)

    ]

    updatesL8 = [
        # Left eight:
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        #
        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),
        #
        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 7, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        #
        PanelUpdate(4, 7, color),
        PanelUpdate(4, 8, color),
        #
        PanelUpdate(6, 5, color),
        PanelUpdate(6, 6, color),
        #
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
        # bottom right
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color)

    ]

    updatesL7 = [
        # Left seven:
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        #
        # PanelUpdate(5,6,color),
        # PanelUpdate(5,7,color),
        # PanelUpdate(5,8,color),
        # PanelUpdate(5,9,color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),
        #
        # PanelUpdate(7,4,color),
        # PanelUpdate(7,5,color),
        # PanelUpdate(7,6,color),
        # PanelUpdate(7,7,color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        #
        # PanelUpdate(4,7,color),
        # PanelUpdate(4,8,color),
        #
        # PanelUpdate(6,5,color),
        # PanelUpdate(6,6,color),
        #
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
        # bottom right
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color)

    ]

    updatesL6 = [
        # Left eight:
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        #
        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),
        #
        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 7, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        #
        PanelUpdate(4, 7, color),
        PanelUpdate(4, 8, color),
        #
        PanelUpdate(6, 5, color),
        PanelUpdate(6, 6, color),
        #
        # PanelUpdate(4,11,color),
        # PanelUpdate(4,12,color),
        # bottom right
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color)

    ]

    updatesL5 = [
        # Left eight:
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        #
        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),
        #
        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 7, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        #
        PanelUpdate(4, 7, color),
        PanelUpdate(4, 8, color),
        #
        # PanelUpdate(6,5,color),
        # PanelUpdate(6,6,color),
        #
        # PanelUpdate(4,11,color),
        # PanelUpdate(4,12,color),
        # bottom right
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color)

    ]

    updatesL4 = [
        # Left eight:
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        # PanelUpdate(3,10,color),
        # PanelUpdate(3,11,color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        #
        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),
        #
        # PanelUpdate(7,4,color),
        # PanelUpdate(7,5,color),
        # PanelUpdate(7,6,color),
        # PanelUpdate(7,7,color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        #
        PanelUpdate(4, 7, color),
        PanelUpdate(4, 8, color),
        #
        # PanelUpdate(6,5,color),
        # PanelUpdate(6,6,color),
        #
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
        # bottom right
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color)

    ]

    updatesR3 = [
        PanelUpdate(4, 13, color1, 10),
        PanelUpdate(4, 14, color1, 10),
        PanelUpdate(4, 15, color1, 10),
        PanelUpdate(4, 16, color1, 10),
        PanelUpdate(4, 17, color1, 10),
        PanelUpdate(4, 18, color1, 10),

        PanelUpdate(6, 11, color1, 10),
        PanelUpdate(6, 12, color1, 10),
        PanelUpdate(6, 13, color1, 10),
        PanelUpdate(6, 14, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        PanelUpdate(6, 16, color1, 10),

        PanelUpdate(8, 9, color1, 10),
        PanelUpdate(8, 10, color1, 10),
        PanelUpdate(8, 11, color1, 10),
        PanelUpdate(8, 12, color1, 10),
        PanelUpdate(8, 13, color1, 10),
        PanelUpdate(8, 14, color1, 10),

        PanelUpdate(6, 16, color1, 10),

        # PanelUpdate(5, 13, color1, 10),
        # PanelUpdate(5, 12, color1, 10),

        PanelUpdate(5, 17, color1, 10),
        PanelUpdate(5, 16, color1, 10),

        # PanelUpdate(7, 11, color1, 10),
        # PanelUpdate(7, 10, color1, 10),

        PanelUpdate(7, 15, color1, 10),
        PanelUpdate(7, 14, color1, 10),

    ]

    updatesL0 = [
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),

        PanelUpdate(4, 7, color),
        PanelUpdate(4, 8, color),
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),

        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),

        PanelUpdate(6, 5, color),
        PanelUpdate(6, 6, color),
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color),

        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 7, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),

    ]

    updatesL1 = [
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),

        PanelUpdate(4, 9, color),
        PanelUpdate(4, 10, color),


        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),

        PanelUpdate(6, 7, color),
        PanelUpdate(6, 8, color),

        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 7, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color)
    ]

    updatesL2 = [
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),

        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),

        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),

        PanelUpdate(6, 5, color),
        # PanelUpdate(6,7,color),
        PanelUpdate(6, 6, color),

        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color)
    ]

    updatesL3 = [
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),

        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),

        PanelUpdate(5, 6, color),
        PanelUpdate(5, 7, color),
        PanelUpdate(5, 8, color),
        PanelUpdate(5, 9, color),
        PanelUpdate(5, 10, color),
        PanelUpdate(5, 11, color),

        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color),

        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color)
    ]
    #######RIGHT#####

    updatesR9 = [
        PanelUpdate(4, 13, color1),
        PanelUpdate(4, 18, color1),
        PanelUpdate(4, 14, color1),
        PanelUpdate(4, 15, color1),
        PanelUpdate(4, 16, color1),
        PanelUpdate(4, 17, color1),

        PanelUpdate(5, 13, color1),
        PanelUpdate(5, 12, color1),
        PanelUpdate(5, 17, color1),
        PanelUpdate(5, 16, color1),

        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(6, 13, color1),
        PanelUpdate(6, 14, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(6, 16, color1),



        PanelUpdate(7, 15, color1),
        PanelUpdate(7, 14, color1),

        PanelUpdate(8, 14, color1),
        PanelUpdate(8, 13, color1),
    ]

    updatesR6 = [
        PanelUpdate(4, 13, color1),

        PanelUpdate(5, 13, color1),
        PanelUpdate(5, 12, color1),

        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(6, 14, color1),
        PanelUpdate(6, 13, color1),
        PanelUpdate(6, 16, color1),


        PanelUpdate(7, 11, color1),
        PanelUpdate(7, 10, color1),
        PanelUpdate(7, 15, color1),
        PanelUpdate(7, 14, color1),

        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 9, color1),
        PanelUpdate(8, 11, color1),
        PanelUpdate(8, 12, color1),
        PanelUpdate(8, 13, color1),
        PanelUpdate(8, 14, color1),



    ]
    updatesR7 = [
        PanelUpdate(4, 13, color1),
        PanelUpdate(4, 14, color1),
        PanelUpdate(4, 15, color1),
        PanelUpdate(4, 16, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(4, 18, color1),



        PanelUpdate(5, 17, color1),
        PanelUpdate(5, 16, color1),

        PanelUpdate(6, 16, color1),
        PanelUpdate(6, 15, color1),

        PanelUpdate(7, 14, color1),
        PanelUpdate(7, 15, color1),

        PanelUpdate(8, 14, color1),
        PanelUpdate(8, 13, color1),
    ]
    updatesR8 = [
        PanelUpdate(4, 13, color1),
        PanelUpdate(4, 14, color1),
        PanelUpdate(4, 15, color1),
        PanelUpdate(4, 16, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(4, 18, color1),

        PanelUpdate(6, 11, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 13, color1),
        PanelUpdate(6, 14, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(6, 16, color1),

        PanelUpdate(8, 9, color1),
        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 11, color1),
        PanelUpdate(8, 12, color1),
        PanelUpdate(8, 13, color1),
        PanelUpdate(8, 14, color1),

        PanelUpdate(5, 17, color1),
        PanelUpdate(5, 16, color1),
        PanelUpdate(5, 13, color1),
        PanelUpdate(5, 12, color1),


        PanelUpdate(7, 11, color1),
        PanelUpdate(7, 10, color1),
        PanelUpdate(7, 15, color1),
        PanelUpdate(7, 14, color1),
    ]

    updatesR2 = [
        PanelUpdate(4, 13, color1),
        PanelUpdate(4, 14, color1),
        PanelUpdate(4, 15, color1),
        PanelUpdate(4, 16, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(4, 18, color1),

        PanelUpdate(6, 11, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 13, color1),
        PanelUpdate(6, 14, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(6, 16, color1),

        PanelUpdate(8, 9, color1),
        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 11, color1),
        PanelUpdate(8, 12, color1),
        PanelUpdate(8, 13, color1),
        PanelUpdate(8, 14, color1),


        PanelUpdate(5, 17, color1),
        PanelUpdate(5, 16, color1),


        PanelUpdate(7, 11, color1),
        PanelUpdate(7, 10, color1),

    ]

    updatesR0 = [
        PanelUpdate(4, 13, color1),
        PanelUpdate(4, 14, color1),
        PanelUpdate(4, 15, color1),
        PanelUpdate(4, 16, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(4, 18, color1),

        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 16, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 15, color1),

        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 11, color1),
        PanelUpdate(8, 12, color1),
        PanelUpdate(8, 13, color1),
        PanelUpdate(8, 14, color1),
        PanelUpdate(8, 9, color1),

        PanelUpdate(5, 13, color1),
        PanelUpdate(5, 12, color1),

        PanelUpdate(4, 18, color1),
        PanelUpdate(4, 17, color1),

        PanelUpdate(5, 17, color1),
        PanelUpdate(5, 16, color1),


        PanelUpdate(7, 11, color1),
        PanelUpdate(7, 10, color1),


        PanelUpdate(6, 15, color1),
        PanelUpdate(7, 15, color1),
        PanelUpdate(7, 14, color1),

    ]

    updatesR1 = [
        PanelUpdate(4, 13, color1),
        PanelUpdate(4, 14, color1),
        PanelUpdate(4, 15, color1),
        PanelUpdate(5, 14, color1),
        PanelUpdate(5, 15, color1),
        PanelUpdate(4, 16, color1),
        PanelUpdate(6, 13, color1),
        PanelUpdate(6, 14, color1),
        PanelUpdate(7, 13, color1),
        PanelUpdate(7, 12, color1),
        PanelUpdate(8, 12, color1),
        PanelUpdate(8, 11, color1),
        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 9, color1),
        PanelUpdate(8, 13, color1),
        PanelUpdate(8, 14, color1),

    ]
    updatesR4 = [
        PanelUpdate(4, 13, color1, 10),
        PanelUpdate(4, 14, color1, 10),
        # PanelUpdate(4, 15, color1, 10),
        # PanelUpdate(4, 16, color1, 10),
        PanelUpdate(4, 17, color1, 10),
        PanelUpdate(4, 18, color1, 10),

        PanelUpdate(6, 11, color1, 10),
        PanelUpdate(6, 12, color1, 10),
        PanelUpdate(6, 13, color1, 10),
        PanelUpdate(6, 14, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        PanelUpdate(6, 16, color1, 10),
        # anelUpdate(8, 10, color1, 10),
        # PanelUpdate(8, 11, color1, 10),
        # PanelUpdate(8, 12, color1, 10),
        PanelUpdate(8, 13, color1, 10),
        PanelUpdate(8, 14, color1, 10),

        # PanelUpdate(8, 9, color1, 10),


        PanelUpdate(5, 13, color1, 10),
        PanelUpdate(5, 12, color1, 10),
        PanelUpdate(6, 12, color1, 10),
        PanelUpdate(6, 11, color1, 10),

        PanelUpdate(5, 17, color1, 10),
        PanelUpdate(5, 16, color1, 10),

        # PanelUpdate(7, 11, color1, 10),
        # PanelUpdate(7, 10, color1, 10),

        PanelUpdate(7, 15, color1, 10),
        PanelUpdate(7, 14, color1, 10),

    ]

    updatesR5 = [
        PanelUpdate(4, 13, color1, 10),
        PanelUpdate(4, 14, color1, 10),
        PanelUpdate(4, 15, color1, 10),
        PanelUpdate(4, 16, color1, 10),
        PanelUpdate(4, 17, color1, 10),
        PanelUpdate(4, 18, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        PanelUpdate(6, 12, color1, 10),
        PanelUpdate(6, 13, color1, 10),
        PanelUpdate(6, 14, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        PanelUpdate(8, 10, color1, 10),
        PanelUpdate(8, 11, color1, 10),
        PanelUpdate(8, 12, color1, 10),
        PanelUpdate(8, 13, color1, 10),
        PanelUpdate(8, 14, color1, 10),
        PanelUpdate(6, 16, color1, 10),
        PanelUpdate(8, 9, color1, 10),

        PanelUpdate(5, 13, color1, 10),
        PanelUpdate(5, 12, color1, 10),
        PanelUpdate(6, 12, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        PanelUpdate(4, 18, color1, 10),
        PanelUpdate(4, 17, color1, 10),
        # PanelUpdate(5, 17, color1, 10),
        # PanelUpdate(5, 16, color1, 10),
        PanelUpdate(6, 16, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        # PanelUpdate(7, 11, color1, 10),
        # PanelUpdate(7, 10, color1, 10),
        PanelUpdate(8, 10, color1, 10),
        PanelUpdate(8, 9, color1, 10),
        PanelUpdate(6, 15, color1, 10),
        PanelUpdate(7, 15, color1, 10),
        PanelUpdate(7, 14, color1, 10),
        PanelUpdate(8, 14, color1, 10),
        PanelUpdate(8, 13, color1, 10),
    ]

    UpdateC = [
        # celsius:
        PanelUpdate(7, 20, color),
        PanelUpdate(7, 19, color),
        PanelUpdate(7, 18, color),
        PanelUpdate(8, 18, color),
        PanelUpdate(8, 17, color),
        PanelUpdate(9, 17, color),
        PanelUpdate(9, 18, color),
        PanelUpdate(9, 19, color),
    ]

    UpdateC = [
        # celsius:
        PanelUpdate(7, 20, color),
        PanelUpdate(7, 19, color),
        PanelUpdate(7, 18, color),
        PanelUpdate(8, 18, color),
        PanelUpdate(8, 17, color),
        PanelUpdate(9, 17, color),
        PanelUpdate(9, 18, color),
        PanelUpdate(9, 19, color),
    ]

    updateNeg = [
        PanelUpdate(4, 1, color),
        PanelUpdate(4, 2, color),
        PanelUpdate(4, 3, color),
        PanelUpdate(4, 4, color)
    ]


foo = Nums()
cond = Conditions()


def fill(nl, color_fill):
    for i in range(10):
        updates = [PanelUpdate(row, col, color_fill, 10)
                   for row, col in data.panel_positions[i]]
        nl.update(updates)


first_digit = 1

while True:
    conditions = ["sunny", "cloudy", "rainy", "snowy"]
    first_digits = [1, 1, 1, 1]
    second_digits = [4, 5, 4, 3]
    is_negative = [False, False, False, True]
    the_c = foo.UpdateC
    the_updates = []
    the_updatesL = []
    the_updatesR = []
    the_updatesNeg = []

    first_digit = weath.temp_first
    second_digit = weath.temp_second
    weather_cond = weath.temp_condition

    for j in range(2):
        if (j == 1):
            fill_color = "#000080"
        else:
            fill_color = "#47E0ED"

        for i in range(len(conditions)):
            first_digit = first_digits[i]
            second_digit = second_digits[i]
            weather_cond = conditions[i]

            # here
            if first_digit == 1:
                the_updatesL = foo.updatesL1
            elif first_digit == 2:
                the_updatesL = foo.updatesL2
            elif first_digit == 3:
                the_updatesL = foo.updatesL3
            elif first_digit == 4:
                the_updatesL = foo.updatesL4
            elif first_digit == 5:
                the_updatesL = foo.updatesL5
            elif first_digit == 6:
                the_updatesL = foo.updatesL6
            elif first_digit == 7:
                the_updatesL = foo.updatesL7
            elif first_digit == 8:
                the_updatesL = foo.updatesL8
            elif first_digit == 9:
                the_updatesL = foo.updatesL9

            if second_digit == 1:
                the_updatesR = foo.updatesR1
            elif second_digit == 2:
                the_updatesR = foo.updatesR2
            elif second_digit == 3:
                the_updatesR = foo.updatesR3
            elif second_digit == 4:
                the_updatesR = foo.updatesR4
            elif second_digit == 5:
                the_updatesR = foo.updatesR5
            elif second_digit == 6:
                the_updatesR = foo.updatesR6
            elif second_digit == 7:
                the_updatesR = foo.updatesR7
            elif second_digit == 8:
                the_updatesR = foo.updatesR8
            elif second_digit == 9:
                the_updatesR = foo.updatesR9
            elif second_digit == 0:
                the_updatesR = foo.updatesR0

            # here

            # here

            if weather_cond == 'snowy':
                the_updates = cond.UpdateSnow

            if weather_cond == 'rainy':
                the_updates = cond.updateRain

            if weather_cond == 'cloudy':
                the_updates = cond.updatecloud

            if weather_cond == 'party cloudy':
                the_updates = cond.updatePartCloud

            if weather_cond == 'sunny':
                the_updates = cond.updateSun

            # here

            fill(nl, fill_color)
            time.sleep(1)

            if (is_negative[i]):
                the_updatesNeg = foo.updateNeg
                nl.update(the_updatesNeg)

            nl.update(the_updatesL)
            nl.update(the_updatesR)
            nl.update(the_c)

            time.sleep(10)
            fill(nl, fill_color)
            time.sleep(2)
            nl.update(the_updates)
            time.sleep(10)
            fill(nl, fill_color)
            time.sleep(2)


# updates1 = [PanelUpdate(row, col, random.choice(colors), 10) for row, col in data.panel_positions[8]]
