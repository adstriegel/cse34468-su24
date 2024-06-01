# mqtt-test.py : Code for testing out MQTT
#
# Name(s):
# E-mail(s):
#

import time
import mqtt_link as mqttnd

# Connect to the MQTT Broker at Notre Dame
theClient = mqttnd.connect_mqtt()

mqttnd.send_mqtt(theClient, "cse34468-su24/awesome/lab-03/test/status", "I am alive!")

TheCount = 0

while True:
    time.sleep(1)
    print('Sending a MQTT message!')
    mqttnd.send_mqtt(theClient, "cse34468-su24/awesome/lab-03/test/status", "I have been alive for " + str(TheCount) + " seconds")
    TheCount += 1


