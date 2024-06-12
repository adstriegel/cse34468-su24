# Homework 3

| **Aspect** | **Information** |
| --- | --- | 
| **Assigned** | Monday, June 10th - Block 3 | 
| **Due** | Monday, June 17th - 5 PM | 
| **Team** | To be done individually |  
| **Canvas Link** | [Homework 03](https://canvas.nd.edu/courses/92659/assignments/274663) | 
| **Points** | 26 points | 

## Submission

Same [instructions as Homework 2](https://github.com/adstriegel/cse34468-su24/blob/main/hw/hw-02/hw2.md). You may use either Canvas for an attached file or GitHub.

## Question 1 - 6 pts

Suppose we have the following setup where a pressure sensitive strip (e.g. a [soft membrane potentiometer](https://www.sparkfun.com/products/8681)) is used to observe the extent to which a freezer door is properly closed:

* A pressure sensitive resistance strip is attached to an 8 bit A/D
* The resistance of the pressure strip varies from 10 kilo-ohms to 100 kilo-ohms across a distance of 0 to 2 centimeters. No pressure (aka zero) comes across as 10 kilo-ohms.
* The A/D is set up such that it measures from the minimum to maximum value in line with the resistance.

For the respective key parameters of the device and the A/D, identify the following properties:

* The minimum, maximum, range, and step size of the digital value from the A/D measurement
* The minimum, maximum, range, and step size of the analog value from the resistance strip measurement
* The minimum, maximum, range, and step size of the analog value from the distance measurement

## Question 2 - 4 pts

Write a function named `getDistance` that gets the digital A/D value via function named `readADC1`.  Return the distance in centimeters that is registered by the pressure strip using what you derived in Question 1.

## Question 3 - 4 pts

Recall the information at the following URL from Homework 2:

[Python RPi GPIO Example](https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-example)

Using your function from Question 2, execute a loop whereby your code will continually update the state of two LEDs, a red LED and a green LED.  If less than 0.5 centimeters is observed, the red LED should be lit.  If more than 1.5 centimeters is observed, the green LED should be lit.  Otherwise, no LED should be lit.

You may assume that the LEDs are in a current sink configuration and you may choose any appropriate GPIO pin for your output.  

## Question 4 - 2 pts

Why would a motor need to use a digital encoder instead of a potentiometer to verify position of the motor?

## Question 5 - 4 pts

Using the web, identify and explain one case of using a Reed switch to detect liquid flow.  Compare and contrast that to one example of using a hall sensor.  

## Question 6 - 6 pts

Identify two "smart" devices or technologies under the umbrella of the Internet of Things (or Industrial Internet of Things) related to your final project interest.  These should not be the same as the links identified by any of your other potential group members.

Include the link as a URL and write 1-2 sentences about the technology / information at the link.  