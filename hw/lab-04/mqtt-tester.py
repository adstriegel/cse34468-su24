# mqtt-tester.py : Code for testing out MQTT
#

import time
import mqtt_link as mqttnd

# Connect to the MQTT Broker at Notre Dame
theClient = mqttnd.connect_mqtt()

mqttnd.send_mqtt(theClient, "cse34468-su24/yourgroupname/lab-04/info/", "I am alive!")

TheCount = 0

while True:
    time.sleep(1)

    # Modify this

    print('Sending a MQTT message!')

    theMessage = '{ "Name" : "I am group yourgroupname" }'

    mqttnd.send_mqtt(theClient, "cse34468-su24/yourgroupname/lab-04/info/", theMessage)
    TheCount += 1


