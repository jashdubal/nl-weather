import random
import time

import data
from nanoleaf import Nanoleaf, PanelUpdate, Color

nl = Nanoleaf()
nl2 = Nanoleaf()
# nl3 = Nanoleaf()
# nl4 = Nanoleaf()



# random hex colors
colors = ["#92ac1d", "#58f982", "#bf6070", "#0eff1f", "#8d2b5d", "#db684c", "#FFFFFF"]

i = 7
while True:
    j= i-1
    updates = [
        PanelUpdate(row,col, "#0000FF", 5) for row,col in data.panel_positions[j]
        
    ]
    updates2 = [
        PanelUpdate(row, col, "#FFFFFF", 5) for row, col in data.panel_positions[i]
    ]
    # updates3 = [
    #     PanelUpdate(row, col, random.choice(colors), 5) for row, col in data.panel_positions[9]
    # ]
    i +=1 
    nl.update(updates)
    nl2.update(updates2)
    # nl3.update(updates3)
    time.sleep(0.5)
