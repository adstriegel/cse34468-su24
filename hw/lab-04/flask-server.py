# flask-base.py : Test code for running a Flask server on a specific port

# Import flask module
#   Look at how we installed MQTT in Lab 3
from flask import Flask
import mqtt_link as mqttnd
import json

# The instance of flask application is the name of our Python file
app = Flask(__name__)

# Global variable to hold temperature info
theTemperatureInfo = []

# home route that returns below text 
# when root url is accessed
@app.route("/")
def hello_world():
    
    # This is where you will put in additional code to work from the SenseHat sensors
    #
    # Make sure this works, then modify the code
    return "<p>Hello, World!</p>"

@app.route("/thermostat")
def do_thermo_info():
    global theTemperatureInfo

    # Return a string with the information that gets served up as

    # You will modify this to return well-formatted information
    theWebString = "<h1>Fancy Information Here</h1>"

    theWebString += "<p>"
    theWebString += "With a dash of JSON, the info is"
    theWebString += "<p>"
    theWebString += str(theTemperatureInfo)

    return str(theWebString)

@app.route("/thermostat/json")
def do_thermo_info_json():
    global theTemperatureInfo

    return str(theTemperatureInfo)


# For your port number, pick 3000 plus the last 4 digits of your student ID
#  In your group, pick the last four digits of whomever is the primary driver
#  for the lab
FlaskPort = 30000 + 1001

# If not responding, modify this to be the IP address of your
# Raspberry Pi where you are running your web server
PiHost = '0.0.0.0'

# Parse a MQTT message
#
#  client : the MQTT client
#  userdata : the user data
#  message : the message that was received
#
def parse_message (client, userdata, message):
    # Global holder
    global theTemperatureInfo

    #global messages
    try:
        m="message received  "  ,str(message.payload.decode("utf-8"))

        # Turn this into a JSON
        theJSON = json.loads(message.payload.decode("utf-8"))

        # You can remove this if you want to later
        print('Got a JSON: ' + str(theJSON))

        # Put the JSON into the global variable
        theTemperatureInfo = theJSON

    except Exception as e:
        print('Issue with the JSON seen - catching it!')
        print('Exception was ' + str(e))
        print('Message was ' + str(message.payload))

        theTemperatureInfo = { 'Error' : 'Unable to process MQTT message'}

    

# Start up the flask server and have it be accessible at:
#
#  http://192.168.0.xxx:FlaskPort 
#   where xxx is the IP address of the Raspberry Pi
#   where FlaskPort is the port number that you selected
#
# For instance, if the port number is 30145 and you are on Raspberry Pi gep-rpi001:
#
# You would browse to:  http://192.168.0.125:30145
#
# Make sure that your laptop or phone is on the cse34468 SSID in order to be 
# able to access the Raspberry Pi and that you are not using any sort of VPN
#  

if __name__ == '__main__':
    theClient = mqttnd.connect_mqtt()

    # Change this code to subscribe to your group's topic
    theClient.subscribe('cse34468-su24/yourgroupname/lab-04/otherinfo/')
    theClient.on_message = parse_message

    theClient.loop_start()

    print('The flask server is running on port ' + str(FlaskPort))

    app.run(port=FlaskPort, host=PiHost)


