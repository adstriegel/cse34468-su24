# Lab 4 - Smart Thermostat

| **Aspect** | **Information** |
| --- | --- | 
| **Assigned** | Monday, June 17th - Block 2 | 
| **Due** | Monday, June 24th - 5 PM (two class periods to work on it) | 
| **Team** | May be done in a group of up to three |  
| **Canvas Link** | Lab 04 | 
| **Points** | 38 points | 

## Overview

Your task is to build a smart thermostat for capturing and reacting to various analog signals as well as providing various mechanisms for digital input and digital output. If you are familiar with the Google Nest thermostat, you can use that as a reference point. While we do not have a touch screen or the ability to run our devices 24/7, we do have a reasonable set of analog inputs, digital outputs (8x8 matrix), and network connectivity.

## Goals

Your code should provide the following properties:

* **Temperature with setpoint:** Your thermostat should periodically poll the temperature as well as evaluate that temperature versus the setpoint.  The default display should be the current temperature.

* **Setpoint-based control:** Your thermostat should activate either the heat or cooling functions any time the temperature is more than 1 C from the set-point.  
   * The intensity of the response should vary based on the gap away from the setpoint. The intensity of the response should vary between 25% to 100% as the distance from the setpoint varies between 1 to 5 degrees away. If the setpoint is more than 5 degrees away, it should be at 100%.   
   * To start, leave the LEDs at 100% and vary the intensity once you have it working. 

* **Control LEDs:** The bottom row will be used to emulate digital output.  The following LEDs should be used either at the top row or at the bottom row (your choice):
   * Heating – Column 0: This LED should vary between 25 to 100% intensity for Red to mimic the intensity of the heating control.  
   * Cooling – Column 1: This LED should vary between 25 to 100% intensity for Blue to mimic the intensity of the cooling control.
   * Unused – Column 2
   * Fan – Column 3: This LED should vary between 25% and 100% when on.  You should use Yellow for the fan to differentiate it versus heating and cooling.
   * Unused – Columns 4-6
   * Power – Column 7: This LED should be lit to denote that your code is running and should stay continuously on. You should use Green for the power LED.  
   * Each of these LEDs are excellent outputs to put into a function, e.g. `setHeatingLED`. 

* **Display:** You should display either the current temperature or the current setpoint subject to what the user is currently doing.  You may either use the built-in libraries or your own custom display approach provided that the bottom row stays preserved (see earlier).  
   * For example, you could mimic a [7 segment display](https://www.sparkfun.com/products/11441) for the two digits of the temperature that will be displayed (you can safely presume that the temperature will always be between 0 and 99 C).  Could you write a `set_tens` function and a `set_ones` function that drives the LEDs?  
   * Think of the test as a set of `if` statements where you pass in the value to display and then set the pixels appropriately.  If you are working in a group, you might have one person write the `set_tens` function and another write the `set_ones` function to divide up the work. Remember to also clear and LEDs that are not being used whenever setting the number (just the individual LEDs, not the entire LED matrix). 

* **Setpoint Manipulation:** The joystick should be able to move the setpoint (target temperature) either up or down.  The joystick button should be pressed before setpoint manipulation can be entered and should be pressed again when exiting (committing) to the new setpoint.  Keep in mind that your control of the heating, cooling, and fan should not stop while you are in the setpoint manipulation mode.  

* **Unit Selection:** If the left direction is pressed, change the display to be in Celsius.  If the right direction is pressed, change the display to be in Farenheit. You may assume that you cannot select units while changing the setpoint.  You may choose whatever default setting that you would like to use. 
   * You will need to look at the documentation to see what units that you get when reading the Sense HAT.  
   * Be careful when changing units with your setpoint. Think about what would / should happen. It might be a good idea to always have your setpoint using a certain scale and then to change / convert it when displaying only.  

## Part 1 - Initial Structure / Core Thermostat

As with many embedded systems, we will stick with the typical structure of a brief set of functions followed by an infinite `while` loop. You can take a look at the `thermostat-start.py` code. 

Test your code using the Sense HAT emulator.  Note that you will need to use the arrow key on your keyboard to mimic the joystick as well as the enter key.  The `thermostat-start.py` code shows determining if the middle button is pressed and then lighting a LED.  You will want to modify / remove this code as appropriate. 

**Task:** Get the basic code for your thermostat testing / working in the emulator. Demonstrate your working code on the Raspberry Pi to Prof. Striegel.

## Part 2 - Extending MQTT

**When copying over the mqtt-config.json file, make sure to define a `.gitignore` file that does not add the `mqtt-config.json` file.  You can copy over the `.gitignore` file in the class repository for Lab 4 as a reference**

Mimicking what we did in Lab 3, add in a JSON message that is sent each time that your loop executes if any of the values have changed. Include the temperature, humidity, and the settings for the respective heating and cooling elements (on or off) only if the temperature or humidity has changed.  The JSON should only include the units in Celsius (do not write C, just known that the number is in Celsius). 

You should publish your information to the following topic:

`cse34468-su24/yourgroupname/lab-04/info/`

Add the JSON functionality to your code. Confirm that everything is working using the MQTT-Explorer.  Remember that you will only be able to run this code on the Raspberry Pi, not on the emulator.  Fortunately, your code should be running well from Part 1. 

**Task:** Get the code running.  You do not need to demonstrate this part of the code to Prof. Striegel.

## Part 3 - Parsing MQTT / Feeding a Web Server

For the last part, we will be parsing the MQTT values with a *client* and then displaying the values on the console (e.g. the `ssh` terminal) as well as being able to access the values as a web server.  There is a little bit of extra Python in the mix where we are using `global` variables.  The file named `flask-server.py` provides a web server where the code is present to both listen to MQTT and then to store that information in a global variable. 

Install `flask` using a similar approach to what you did with Lab 3 and `paho-mqtt`.  

1. Modify the `flask-server.py` code to pick a port (see instructions) in the file and also to pick the correct MQTT topic. 
2. Modify the `mqtt-tester.py` code to use the appropriate topic with your group name.
2. Log in with two separate `ssh` sessions to your choice of the Raspberry Pi. This can be the same Raspberry Pi where you are running your other code or it can be a different Raspberry Pi. 
3. On one of the sessions, run the `flask-server.py` code. 
4. On the other session, run the `mqtt-tester.py` code.
5. Browse to the Raspberry Pi using the IP address of the Pi together with the port number, e.g. `http://192.168.0.125:31001` picking the correct Raspberry Pi where you code is running and the right port number. You can do this from your phone or your laptop provided that you are on the `cse34468` SSID.
6. Try browsing to `http://192.168.0.125:31001/thermostat` and `http://192.168.0.125:31001/thermostat` also correcting for the right port number and the right Raspberry Pi. 

The code as provided in `mqtt-tester.py` pushes a piece of JSON information to the MQTT server at the specified topic.  The `flask-server.py` code waits for messages at the specified topic and then returns information based on the most recent JSON.  

Provided that your code is sending a valid JSON, you no longer need to use `mqtt-tester.py`.  However, you will need to modify the `flask-server.py` code to *beautify* what is reported via the `/thermostat` URI.  Using a bit of HTML, create an appropriate string that looks reasonable containing all relevant information for the thermostat in a human-accessible format (e.g. not a JSON).  

**Task**: Complete this step and then demonstrate a web browser on your laptop (or phone) browsing to that particular page to Prof. Striegel.  

## End Result

Your GitHub submission will have a several files in the `hw/lab-04` sub-directory for one of the group members. Your code must have the following files to receive credit for the demos in the repository of the primary submitter:

* `/hw/lab-04/thermostat.py`
* `/hw/lab-04/flask-server.py`

If you are not submitting for your repository but are part of a different team, submit on Canvas the name of the person who is submitting for your group.

## Grading

The lab is worth a total of 45 points as described below:

* 30 pts - Successful demonstrations for Prof. Striegel of Parts 1 and 3 (15 pts each)
* 1 pt - Files are in the `lab-04` folder in your repository
* 1 pt - Files are named correctly
* 2 pt - Commit messages start with `lab-04`
* 1 pt - Correct hash submitted via Canvas or identification of group member name
* 3 pts - Code is reasonably commented and formatted with appropriate variable names

The lab is due by Monday afternoon on June 24 at 5 PM. 




