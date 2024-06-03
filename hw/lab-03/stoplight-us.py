# stoplight-us.py : Example code for a stoplight for a N-S US style stoplight
#
# Name(s):
# E-mail(s):
#

import time 
from sense_hat import SenseHat

# Your functions go here

# Set the stoplight to a specific setting
#   theHAT - the SenseHat object
#   theSetting - the setting to set the stoplight to
#     which is either red, yellow, or green
def setStoplight (theHAT, theSetting):
    if theSetting == 'Red':
        # Turn the red light on
        sense.set_pixel(2, 5, (255, 0, 0)) 
        # Turn off the yellow and green lights       
        sense.set_pixel(2, 6, (0, 0, 0))
        sense.set_pixel(2, 7, (0, 0, 0))
    elif theSetting == 'Yellow':
        # Turn the yellow light on
        sense.set_pixel(2, 6, (255, 255, 0))
        # Turn off the red and green lights       
        sense.set_pixel(2, 5, (0, 0, 0)) 
        sense.set_pixel(2, 7, (0, 0, 0))
    elif theSetting == 'Green':
        # Turn the green light on
        sense.set_pixel(2, 7, (0, 255, 0))
        # Turn off the red and yellow lights       
        sense.set_pixel(2, 5, (0, 0, 0)) 
        sense.set_pixel(2, 6, (0, 0, 0))

##################################################
# Main Code is Here

sense = SenseHat()

LoopDelay = 0.25      # 250 ms per loop iteration
PreScalar = 10.00      # Set this higher to speed up for testing purposes
# PreScalar = 1.0

# Compute how long to wait on each loop
LoopDelay = LoopDelay / PreScalar

# Define each of the states
#
# Start at Red, go to Green, then Yellow, then back to Red
#
# State         Means What                   Next State      Ticks
# 
# Light-Red     Stay red for 35 seconds      Light-Green     35*4
# Light-Green   Stay green for 30 seconds    Light-Yellow    30*4
# Light-Yellow  Stay yellow for 5 seconds    Light-Red        5*4


TheState = 'Light-Red'
TicksToWait = 35 * 4

while True:
    # Decrease the counter - when we get to zero, we change
    TicksToWait -= 1

    if TheState == 'Light-Red':
        # Set the stoplight to red
        setStoplight(sense, 'Red')
    elif TheState == 'Light-Yellow':
        # Set the stoplight to yellow
        setStoplight(sense, 'Yellow')
    elif TheState == 'Light-Green':
        setStoplight(sense, 'Green')

    # Should we transition?
    if TicksToWait == 0:
        # Yes - but what to?

        if TheState == 'Light-Red':
            TheState = 'Light-Green'
            TicksToWait = 30 * 4
        elif TheState == 'Light-Green':
            TheState = 'Light-Yellow'
            TicksToWait = 5 * 4
        elif TheState == 'Light-Yellow':
            TheState = 'Light-Red'
            TicksToWait = 35 * 4

    # All done - sleep and keep counting

    # Leave this code here
    time.sleep(LoopDelay)