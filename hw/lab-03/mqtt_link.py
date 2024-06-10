# mqtt-link.py : Linkage for the MQTT Broker
#
# Provided as part of the Lab 3 Starter Code

from paho.mqtt import client as mqtt
import json
from pathlib import Path

# This code is provided for you

def load_mqtt_auth():
    auth_path = Path("mqtt-config.json")
    timeout_s = 60
    while not auth_path.is_file():
        print('Oh no - no mqtt-config.json file found - bailing out!')
        exit(-1)

    with open(auth_path, "r") as file:
        return json.load(file)

def connect_mqtt ():
    client = mqtt.Client()
#        callback_api_version=mqtt.CallbackAPIVersion.VERSION1)

    auth = load_mqtt_auth()
    client.username_pw_set(auth['username'], auth['password'])
    client.connect(auth['broker_addr'], int(auth['broker_port']), 60)

    return client 

def send_mqtt (client, topic, message):
    client.publish(topic, message)
