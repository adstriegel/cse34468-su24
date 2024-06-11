# thermostat-start.py
#
# Name(s):
# E-mail(s):
#

import time
from sense_hat import SenseHat

# Your functions go here



# The main body of the code

sense = SenseHat()

LoopDelay = 0.25      # 250 ms per loop iteration

while True:
    # Is the joystick doing anything?
    events = sense.stick.get_events()
    for event in events:
        # Skip releases
        if event.action == "pressed" and event.direction == "middle":
            sense.set_pixel(0,0, (255,255, 255))

        if event.action == "released" and event.direction == "middle":
            sense.set_pixel(0,0, (0,0,0))


    # Read the temperature

    # Do we need to do anything in response to the temperature?

    # Is it more than 1 degree away?

    # If it is more than 1 degree away, how far away is it?

    time.sleep(LoopDelay)

