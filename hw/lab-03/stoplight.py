# stoplight.py : Example code for a stoplight using a state machine
#
# Name(s):
# E-mail(s):
#

import time 
from sense_hat import SenseHat

# lightRider - Function to display a light moving back and forth
def lightRider (SenseHAT, PosLight, PosUp):
    # KnightRider Effect - https://www.youtube.com/watch?v=oNyXYPhnUIs

    # Do you see any subtle bugs in this code?  If so, what are they?
    for i in range(0, 8):
        if i == PosLight:
            sense.set_pixel(PosLight, 7, (255, 0, 0))
            if PosUp == True and PosLight > 0:
                sense.set_pixel(PosLight - 1, 7, (50, 0, 0))
            elif PosUp == False and PosLight < 7:
                sense.set_pixel(PosLight + 1, 7, (50, 0, 0))
        else:
            sense.set_pixel(i, 7, (0, 0, 0))

    if PosUp == True:
        PosLight += 1
        if PosLight == 7:
            PosUp = False 
    else:
        PosLight -= 1
        if PosLight == 0:
            PosUp = True

    return PosLight, PosUp

# Your functions go here



# Main Code is Here

sense = SenseHat()

LoopDelay = 0.25      # 250 ms per loop iteration
PreScalar = 2.00      # Set this higher to speed up for testing purposes
# PreScalar = 1.0

# Extra Code for Demo

PositionLight = 4
PositionUp = True

# 
LoopDelay = LoopDelay / PreScalar


while True:
    # You will replace this code here
    PositionLight, PositionUp = lightRider(sense, PositionLight, PositionUp)

    # Leave this code here
    time.sleep(LoopDelay)