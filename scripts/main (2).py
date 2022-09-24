from __future__ import annotations

import random
import time
from weather import Weather


import data
from nanoleaf import Nanoleaf, PanelUpdate

# nl = Nanoleaf()
# nl1 = Nanoleaf()
weath = Weather()

# random hex colors
colors = ["#92ac1d", "#58f982", "#bf6070", "#0eff1f", "#8d2b5d", "#db684c", "#FFFFFF"]
color = "#000000"
color1 = "#92ac1d"

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
        PanelUpdate(8, 10, color1, 10),
        PanelUpdate(8, 11, color1, 10),
        PanelUpdate(8, 12, color1, 10),
        PanelUpdate(8, 13, color1, 10),
        PanelUpdate(8, 14, color1, 10),
        PanelUpdate(6, 16, color1, 10),
        PanelUpdate(8, 9, color1, 10),

        PanelUpdate(4, 13, color1, 10),
        # PanelUpdate(5, 13, color1, 10),
        # PanelUpdate(5, 12, color1, 10),
        PanelUpdate(6, 12, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        PanelUpdate(4, 18, color1, 10),
        PanelUpdate(4, 17, color1, 10),
        PanelUpdate(5, 17, color1, 10),
        PanelUpdate(5, 16, color1, 10),
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

    updatesL0 = [
        PanelUpdate(3, 8, color),
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(3, 12, color),
        PanelUpdate(3, 13, color),
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
        PanelUpdate(6, 9, color),
        PanelUpdate(6, 10, color),
        PanelUpdate(7, 4, color),
        PanelUpdate(7, 5, color),
        PanelUpdate(7, 6, color),
        PanelUpdate(7, 7, color),
        PanelUpdate(7, 8, color),
        PanelUpdate(7, 9, color),
        PanelUpdate(6, 5, color),
        PanelUpdate(6, 6, color),
        PanelUpdate(4, 7, color),
        PanelUpdate(4, 8, color)
    ]

    updatesL1 = [
        PanelUpdate(3, 9, color),
        PanelUpdate(3, 10, color),
        PanelUpdate(3, 11, color),
        PanelUpdate(4, 9, color),
        PanelUpdate(4, 10, color),
        PanelUpdate(4, 11, color),
        PanelUpdate(4, 12, color),
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
        PanelUpdate(6, 7, color),
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

    updateR9 = [
        PanelUpdate(4, 13, color1),
        PanelUpdate(5, 13, color1),
        PanelUpdate(5, 12, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(4, 18, color1),
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
        PanelUpdate(4, 18, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(5, 17, color1),
        PanelUpdate(5, 16, color1),
        PanelUpdate(6, 16, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(7, 15, color1),
        PanelUpdate(7, 14, color1),
        PanelUpdate(8, 14, color1),
        PanelUpdate(8, 13, color1),
    ]

    updateR6 = [PanelUpdate(4, 13, color1),
                PanelUpdate(5, 13, color1),
                PanelUpdate(5, 12, color1),
                PanelUpdate(6, 12, color1),
                PanelUpdate(6, 11, color1),
                PanelUpdate(7, 11, color1),
                PanelUpdate(7, 10, color1),
                PanelUpdate(8, 10, color1),
                PanelUpdate(8, 9, color1),
                PanelUpdate(8, 10, color1),
                PanelUpdate(8, 11, color1),
                PanelUpdate(8, 12, color1),
                PanelUpdate(8, 13, color1),
                PanelUpdate(8, 14, color1),
                PanelUpdate(6, 15, color1),
                PanelUpdate(7, 15, color1),
                PanelUpdate(7, 14, color1),
                PanelUpdate(6, 14, color1),
                PanelUpdate(6, 13, color1),
                ]
    updateR7 = [PanelUpdate(4, 13, color1),
                PanelUpdate(5, 13, color1),
                PanelUpdate(5, 12, color1),
                PanelUpdate(6, 12, color1),
                PanelUpdate(6, 11, color1),
                PanelUpdate(4, 18, color1),
                PanelUpdate(4, 17, color1),
                PanelUpdate(5, 17, color1),
                PanelUpdate(5, 16, color1),
                PanelUpdate(6, 16, color1),
                PanelUpdate(6, 15, color1),
                PanelUpdate(7, 14, color1),
                PanelUpdate(8, 14, color1),
                PanelUpdate(8, 13, color1),
                ]
    updateR8 = [PanelUpdate(4, 13, color1),
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
                PanelUpdate(8, 10, color1),
                PanelUpdate(8, 11, color1),
                PanelUpdate(8, 12, color1),
                PanelUpdate(8, 13, color1),
                PanelUpdate(8, 14, color1),
                PanelUpdate(6, 16, color1),
                PanelUpdate(8, 9, color1),

                PanelUpdate(4, 13, color1),
                PanelUpdate(5, 13, color1),
                PanelUpdate(5, 12, color1),
                PanelUpdate(6, 12, color1),
                PanelUpdate(6, 11, color1),
                PanelUpdate(4, 18, color1),
                PanelUpdate(4, 17, color1),
                PanelUpdate(5, 17, color1),
                PanelUpdate(5, 16, color1),
                PanelUpdate(6, 16, color1),
                PanelUpdate(6, 15, color1),
                PanelUpdate(6, 11, color1),
                PanelUpdate(7, 11, color1),
                PanelUpdate(7, 10, color1),
                PanelUpdate(8, 10, color1),
                PanelUpdate(8, 9, color1),
                PanelUpdate(6, 15, color1),
                PanelUpdate(7, 15, color1),
                PanelUpdate(7, 14, color1),
                PanelUpdate(8, 14, color1),
                PanelUpdate(8, 13, color1), ]

    updatesR2 = [
        PanelUpdate(4, 13, color1),
        PanelUpdate(4, 14, color1),
        PanelUpdate(4, 15, color1),
        PanelUpdate(4, 16, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(4, 18, color1),

        PanelUpdate(6, 11, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 15, color1),

        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 11, color1),
        PanelUpdate(8, 12, color1),
        PanelUpdate(8, 13, color1),
        PanelUpdate(8, 14, color1),
        PanelUpdate(6, 16, color1),
        PanelUpdate(8, 9, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(4, 18, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(5, 17, color1),
        PanelUpdate(5, 16, color1),
        PanelUpdate(6, 16, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(7, 11, color1),
        PanelUpdate(7, 10, color1),
        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 9, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(8, 14, color1),
        PanelUpdate(8, 13, color1),
    ]

    updatesR0 = [
        PanelUpdate(4, 13, color1),
        PanelUpdate(4, 14, color1),
        PanelUpdate(4, 15, color1),
        PanelUpdate(4, 16, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(4, 18, color1),

        PanelUpdate(6, 11, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 15, color1),

        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 11, color1),
        PanelUpdate(8, 12, color1),
        PanelUpdate(8, 13, color1),
        PanelUpdate(8, 14, color1),
        PanelUpdate(6, 16, color1),
        PanelUpdate(8, 9, color1),

        PanelUpdate(5, 13, color1),
        PanelUpdate(5, 12, color1),
        PanelUpdate(6, 12, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(4, 18, color1),
        PanelUpdate(4, 17, color1),
        PanelUpdate(5, 17, color1),
        PanelUpdate(5, 16, color1),
        PanelUpdate(6, 16, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(6, 11, color1),
        PanelUpdate(7, 11, color1),
        PanelUpdate(7, 10, color1),
        PanelUpdate(8, 10, color1),
        PanelUpdate(8, 9, color1),
        PanelUpdate(6, 15, color1),
        PanelUpdate(7, 15, color1),
        PanelUpdate(7, 14, color1),
        PanelUpdate(8, 14, color1),
        PanelUpdate(8, 13, color1),
    ]

    updatesR1 = [
        PanelUpdate(4, 14, color1),
        PanelUpdate(4, 15, color1),
        PanelUpdate(5, 14, color1),
        PanelUpdate(5, 14, color1),
        PanelUpdate(6, 14, color1),
        PanelUpdate(6, 13, color1),
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
        # anelUpdate(8, 10, color1, 10),
        # PanelUpdate(8, 11, color1, 10),
        # PanelUpdate(8, 12, color1, 10),
        PanelUpdate(8, 13, color1, 10),
        PanelUpdate(8, 14, color1, 10),
        PanelUpdate(6, 16, color1, 10),
        # PanelUpdate(8, 9, color1, 10),

        PanelUpdate(4, 13, color1, 10),
        PanelUpdate(5, 13, color1, 10),
        PanelUpdate(5, 12, color1, 10),
        PanelUpdate(6, 12, color1, 10),
        PanelUpdate(6, 11, color1, 10),
        PanelUpdate(4, 18, color1, 10),
        PanelUpdate(4, 17, color1, 10),
        PanelUpdate(5, 17, color1, 10),
        PanelUpdate(5, 16, color1, 10),
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

foo  = Nums()

while True:

    first_digit = weath.temp_first
#     first_digit = 1

    nl = update(foo.updateL8)
    nl1 = update(foo.updateR8)
    print(first_digit)





    #updates1 = [PanelUpdate(row, col, random.choice(colors), 10) for row, col in data.panel_positions[8]]

    time.sleep(1)
