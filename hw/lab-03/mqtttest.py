# mqtt-test.py : Code for testing out MQTT
#
# Name(s):
# E-mail(s):
#

import time
import mqtttest as mqttnd

theClient = mqttnd.connect_mqtt()

mqttnd.send_mqtt(theClient, "I am alive!", "cse34468-su24/awesome/lab-03/test/status")

TheCount = 0

while True:
    time.sleep(1)
    print('Sending a MQTT message!')
    mqttnd.send_mqtt(theClient, "I have been alive for " + int(TheCount) + "seconds", "cse34468-su24/awesome/status")



