# Homework 1

| **Aspect** | **Information** |
| --- | --- | 
| **Assigned** | Monday, May 27th - Block 3 | 
| **Due** | Monday, June 3rd - 5 PM | 
| **Team** | To be done individually |  
| **Canvas Link** | Homework 01 | 
| **Points** | 21 points | 

## Aside - Homework Purpose

As noted in the first lecture, homework assignments are a way for you to dive a bit deeper on the topics as well as reinforce key topics from the class.  Early on, we will have a fair amount of Python programming to help reinforce Python and as the course goes on, we will shift over to more broadly looking at IoT and our surroundings, particularly here in Berlin.

## Submission

To submit the homework, create a `hw-01` sub-directory in your Git repository. Place the respective files as noted in the instructions in that sub-directory.  Make sure to `commit` and `push` the files and then note the submission hash via Canvas.  Your `commit` message should start with `hw-01: YOUR MESSAGE`. 

You are welcome to do a single commit and push with everything or to do individual commits on each problem (recommended) followed by a push.  

## Problem 1 - Examine a JSON

Take a look at the code on the class repository named `fetch-score.py` in the `hw/hw-01` sub-directory.  This code uses HTTP (e.g. a web fetch) to retrieve content from a server sitting back in Prof. Striegel's office.  The particular URL in question is below:

http://ns-mn1.cse.nd.edu/cse34468/hw-01/score.json

Put that URL in your web browser and look at the content that comes back.  The content is in the format of what is known as a JSON or Java Serialized Object Notation.  Long story short, it is a way to encode data in a way that is easy to understand / parse.  Python has a fantastic set of tools to help do this.

**Task:** Copy / past the content that comes back from the website and create a file named `score-dl.json` in your private repository in the `hw/hw-01` directory.  

## Problem 2 - Parse the JSON

If you take a lookat the Python code, it does most of the hard work for you in terms of fetching the website and then turning that content into a set of Python dictionaries and arrays.  Remember, a dictionary uses keys while an array uses numeric indices  

Your next task is to write code that parses JSON to compute the win-loss record for Notre Dame.  To do this, think about how you might iterate over an array (for loop) and then what keys (fields) appear consistent (`ScoreND`, `ScoreOpp`).  Think about the logic of what you might want to tally and don't forget to initialize it, e.g. which score was greater?  

Output the win-loss record in the format of (XX-YY) where the XX is the number of wins and YY is the number of losses.  We will presume that there cannot be a tie. 

**Note:** This code will not work in a Jupyter notebook since you cannot do web fetches inside of a notebook on the remote Jupyter site. You can however run this locally inside of a notebook on your laptop.

**Task:** Modify the `fetch-score.py` code appropriately and place the updated version in your `hw/hw-01` directory.  Make sure that the header information is updated and that you modify the code in the appropriate locations as denoted in the file.

## Problem 3 - Berlin IoT / Embedded Examples

Take a look at the two of the following items:

* Any stoplight at any intersection 
* Display for the next arriving tram / subway stations
* The ambient environment in the Lindebrau (the restaurant we ate at on Saturday for lunch)
* The ticket validation system (public transport)
* The microwave / oven in your apartment
* The refrigerator in your apartment

Answer / consider the following questions for each of the two systems (recall from Lecture 1 - Block 3):

* Is the system an embedded system? Why or why not?
* Can / should the system be connected to the Internet (aka Internet of Things)?

Write several sentences on each question and upload your answers into a file named `IoT-Eval.md` in your `hw/hw-01` sub-directory in your private repository.

## Problem 4 - The Future or Too Much?

Watch the following Kickstarter video:

https://www.kickstarter.com/projects/meticulous/meticulous-espresso

To what extent is the Internet (not with respect to crowd sourcing but rather the technology approach) involved as to this particular thing? Is this a good concept or a bad concept? Is the price point reasonable? 

Write your small paragraph in a file named `meticulous.md` in your `hw/hw-01` sub-directory in your private repository.

## Rubric / Double Check

Your submission should have four files:

* `hw/hw-01/score-dl.json`
* `hw/hw-01/fetch-score.py`
* `hw/hw-01/IoT-Eval.md`
* `hw/hw-01/meticulous.md`

The problems are worth the following amounts:

| **Problem** | **Points** |
|---|---|
| 1 | 2 pts |
| 2 | 8 pts | 
| 3 | 6 pts | 
| 4 | 5 pts |

Note that points are only appropriately weighted within a given Canvas category.  
