# Syllabus - CSE 34468 - Internet of Things Summer 2024

## Course Motivation

Over the past decade, there has been tremendous growth in the availability of highly capable low-cost devices capable of sensing and actuating our environment under the guise of Cyber-Physical Systems (CPS). When coupled with improvements in wireless communications, the Internet of Things (IoT) has emerged with the potential for transforming our modern society, instrumenting everything from ourselves via wearable computing (smart watches, health sensors) to our houses (home automation) to our environment (smart cities) to transportation (driverless cars).

## Overview

This course will introduce the basic building blocks of the Internet of Things (IoT). The course will introduce students to Python, embedded systems (Raspberry Pi), sensing, actuation, and introductory networking. The course will begin with a brief overview of Python and will then work through the basic IoT components. Specific components to be covered include I/O (input / output), timing (measuring time, time-based output (ex. PWM)), analog interactions (A/D, D/A), communication buses (serial, parallel), and networking (IP, wireless). The course will be a hands-on course with various skill building lab modules and projects.

## Instructor

Prof. Aaron Striegel, Computer Science and Engineering, striegel@nd.edu

## Pre-Requisites

None besides prior programming via MATLAB or other introductory coursework.  EG 10117 / EG 10118 is sufficient.

## Textbook

None - all materials will be on-line / available via slides

## On-line Resources

[Canvas](https://canvas.nd.edu/)

[GitHub](https://github.com/adstriegel/cse34468-su24) - this website

## Course Objectives

At the end of the course, students should be able to:

* Describe the fundamental components of a microcontroller and the basic components of a system on a chip (SoC)
* Recognize and understand the basics of well-written / well-structured Python code
* Describe and articulate how an embedded system reads and writes digital I/O (input via a key press, output to a LED)
* Understand how time works on a computer (real-time) and how time can be measured (Input Capture) or used to manipulate I/O (PWM)
* Understand how analog signals are discretely captured and how basic environmental values can be measured (temperature, pressure)
* Understand basic communications to access such sensors including serial interactions (SPI)
* Understand broadly basic networking concepts with regards to wireless communications and Internet networking (IP)
* Describe and articulate a complex embedded system 
* Be able to articulate rough prototypes of various canonical IoT systems

## Lecture

Lectures will be held on Monday and Wednesday morning from 9 AM - 12 PM.  A tenative schedule can be found on the class GitHub repository.  Lecture will generally be divided into three blocks consisting of a lecture, lab, and closing lecture.  Wednesday lectures will generally include a quiz at the end of lecture.  

## Grading

| **Item** | **Weight** | **Item** | **Weight** | 
|---|---|---|---|
| **Pre-Assignment** | 5% | **Group Evaluation** | 5% | 
| **Homework** | 10% | **Final Project** | 10% |  
| **Labs** | 25% | **Lab Practical** | 10% |   
| **Quizzes** | 10% | **Final Exam** | 25% | 

* Labs are within class assignments due at the end of the next class day (5 PM) from the last scheduled portion for the lab.  For example, a Monday lab would be due by the end of the day on Wednesday (5 PM). Most labs will include a code submission as well as a demonstration of the working lab.  
   * After the first two labs which are to be completed individually, all subsequent labs may be done in groups of up to three students.
* Homework will be small programming assignments that can be done on your computer and will be submitted via Canvas. Homework assignments will be done individually.
* Quizzes will be given in Weeks 1-5. Quizzes will be done on-line via Canvas, typically at the end of lecture on Wednesdays.
* The final exam is slated for the last day of class and will be cumulative.
* A lab practical will be slated on the second to last day and will be done individually.  
* Grades will be recorded via Canvas. Grading will follow the normal Canvas grading scale from A-F.
* Late assignments will be docked 25% per day from the maximum possible score. A five minute grace period is afforded from the official time listed whereby a late penalty will not be assessed.
* The group evaluation will be conducted twice in the session and will be used for final grade assignments.  Provided that you submit the evaluation, you will initially receive full marks after which the evaluations will be considered when arriving at your final grade.  
* The final project will be an extended report and presentation about relevant Internet of Things applications, ideally with an eye towards our study abroad location here in Berlin. 
* Outstanding final projects, final exams, and / or group evaluations may warrant a grade bump for those who are extremely close to the next grade level (0.3% or less).

## Course Policies

### Diversity and Inclusion

The University of Notre Dame is committed to social justice and diversity. I share that commitment and strive to maintain a positive learning environment based on open communication, mutual respect, and non-discrimination. In this class we will not discriminate on the basis of race, sex, age, economic class, disability, veteran status, religion, sexual orientation, color, or national origin. Any suggestions as to how to further such a positive and open environment will be appreciated and given serious consideration.

### Honor Code

As a member of the Notre Dame community, you acknowledge that it is your responsibility to learn and abide by principles of intellectual honesty and academic integrity, and therefore you will not participate in nor tolerate academic dishonesty.

As we will be doing relatively introductory Python for the course, many AI tools tend to be quite capable of writing code (ChatGPT, Co-Pilot). We will at times look at these tools and their capabilities in class. However, since these tools tend to do nearly all of the work, one can often arrive at solutions without truly understanding the why underneath them. Since the goal of the class is to understand the why, you cannot use AI solutions for your homework or labs. There will be a **zero** tolerance policy for AI-based solutions. A first violation will be a zero for that assignment and any subsequent cases will result in failing the course.

### Other Notes

This class is meant to be interactive.  We will be doing both lecture content as well as a fair amount of coding so make sure to bring a laptop with you to class.  

Keep in mind as well that we will interact with a wide variety of embedded system components that may or may not always work as intended.  There will be weird and obscure bugs that will at times test your savviness in taking advantage of all of the various public resources (Google, StackOverflow, etc.).  Much of the course will be group-oriented so you will be encouraged to take advantage of the knowledge of your peers as well.  Advising / asking questions is OK, sharing code is not beyond your group for a given assignment.  


