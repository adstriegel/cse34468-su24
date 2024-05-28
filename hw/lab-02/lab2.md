# Lab 2 - Working with Datasets

| **Aspect** | **Information** |
| --- | --- | 
| **Assigned** | Wedenesday, May 29th - Block 2 | 
| **Due** | Monday, June 3rd - 5 PM | 
| **Team** | To be done individually |  
| **Canvas Link** | Lab 02 | 
| **Points** | 20 points | 

In Lab 1, we focused on getting logged into the Raspberry Pi and trying to run our initial sets of Python code.  Needless to say, it was a bit hectic but now after running code that was largely pre-written, the goal of this lab is to write a bit more Python code and to bring in some of your newly learned Python knowledge.

## Pre-Check / Pre-Review

For this lab, you will have the option of running your code either on the Raspberry Pi or to run the code directly on your laptop.  By now, you should have the following software components working / installed correctly on your laptop:

* **A good code editor:** First and foremost, having a good code editor or a full Integrated Development Environment (IDE) is essential.  Generally, you are recommended to use Visual Studio Code which comes with built-in Python syntax highlighting.
* **GitHub Software:** You should have a good idea now where your code "lives" on your notebook and how to add files / edit files on your laptop.  You should also have a good idea how to check what is up in the cloud (GitHub) and what the difference is between `commit` (saving a local version) and `push` (pushing any committed changes to the cloud).  
   * Remember, to check what the instructor sees (and to get the commit hash), go to your private repository on GitHub.  The content that you see there is what we will see when we go to clone your repository for grading purposes.
   * Be sure to remember how to label your commit messages, generally those will start with the assignment associated with that commit, e.g. `lab-02`.
* **Tools for the Raspberry Pi**: You should be able to do two key interactions with the Rasbperry Pi.  First, you should be able to login using `ssh` which is what gives you the terminal for running your code.  Second, you should be able to copy files up to the Raspberry Pi using an appropriate client.  For Windows, WinSCP works great. For Mac, you can use CyberDuck or FileZilla.
   * When logged into the Raspberry Pi, recall the UNIX commands that we used the last time.  `cd` changes to a different directory.  `mkdir` creates (makes) a new directory.  `pwd` (print working directory) will print your curent location and to run your code, type `python YOUR-PYTHONFILE.py` to run your code. `ls` lists the files present in your current directory (folder).  
   * Your files should go in the `solo/NETID` directory when working individually and most likely in a sub-directory related to the particular lab that you are working on.  When we are doing group work starting next week, we will use the `group` directory.
   * If you get lost of where exactly you are at, you can type `cd ~` which will take you back to the home directory of the `iotgep` user. `pwd` will tell you where you are at in terms of the directory. The `~` refers to the current user.
   * You do not have to type out everything always.  If you press tab, the shell (what you are logged into), will try to auto-complete.  For instance, if your file is named `hello-mine.py`, you can just type `he` and then press tab to complete the filename.   

### Available Nodes

We have a total of eight Raspberry Pi nodes at the following IP addresses:

| **Host Name** | **IP Address** | **Unit Type** |
|---|---|---|
| gep-rpi001 | 192.168.0.125 | Raspberry Pi 5 |
| gep-rpi002 | 192.168.0.126 | Raspberry Pi 5 |
| gep-rpi003 | 192.168.0.127 | Raspberry Pi 5 |
| gep-rpi004 | 192.168.0.128 | Raspberry Pi 5 |
| gep-rpi005 | 192.168.0.129 | Raspberry Pi 5 |
| gep-rpi006 | 192.168.0.130 | Raspberry Pi 5 |
| gep-rpi007z | 192.168.0.131 | Raspberry Pi 5 |
| gep-rpi008z | 192.168.0.132 | Raspberry Pi 5 |

The last two nodes (the two Rasbperry Pi 2W Zero nodes) will be brought up if needed but likely will not be needed for this lab.  The username / password as well as the SSID / password will be displayed on the projector during the lab.  

For this lab, you can run the code either locally on your laptop or on the Raspberry Pi.

## Lab Overview

In this lab, we will be computing several basic statistics on a set of data retrieved from a remote web server.  This data (formatted as a CSV) is drawn from an Internet performance measurement node (also a Raspberry Pi) that has been measuring the Internet speed at Prof. Striegel's house since the end of December last year. 

Your task is to fetch the CSV (Comma Separated Values) content from the remote website and then to iterate through it to figure out various statistical properties (min, max, average, median, standard deviation). You will be given helper code similar to Homework 1 that will help you fetch the data. You may run this code either on your laptop or run it on one of the Raspberry Pi nodes. 

The data format looks something like this:

~~~
timestamp,mac,test_uuid,type,direction,interface,host,isp,duration_s,transfered_mbytes,tput_mbps,std_tput_mbps,max_tput_mbps,min_tput_mbps,median_tput_mbps
2024-05-03T02:26:16-04:00,DC-A6-32-1D-A4-E0,93f8e208-2425-4e9f-b4c7-17d77b1c211a,iperf,downlink,eth0,ns-mn1.cse.nd.edu:5212,unknown,5.000101,495.1798,792.2716761121426,25.984215820781476,814.9305375808235,741.7217525614017,799.9386373617318
2024-04-18T01:13:18-04:00,DC-A6-32-1D-A4-E0,e549a432-b63a-4b93-bc21-3b45d80e238b,iperf,downlink,eth0,ns-mn1.cse.nd.edu:5220,unknown,5.000069,496.684272,794.683868562614,32.79899940964683,828.6531652356962,734.8740876469949,796.491628151176
~~~

As you can see from the data, the first line is the name of the individual field.  For the purposes of this lab, we care about three specific fields in the file:

* *direction:* The direction of the specific test.  There are two different values, `downlink` which measured the speed from the Internet to the node and `uplink` which measured the speed from the node to the Internet. This field is a string.  
* *interface:* The particular interface that was being with there being two different types in the file: `eth0` which is the wired (Ethernet) interface and `wlan0` which is the built-in WiFi link of the Rasbperry Pi. This field is a string.  
* *tput_mbps:* The measured throughput across the entirety of the specific test measured in megabits per second. This field is a floating point value.

There are four files present both in the class public GitHub repository as well as via the web server that we accessed from the first lab.

* `data-100.csv`: This is the first 100 lines of data in the file (total of 101 lines).
* `data-1k.csv`: This is the first 1000 lines of data in the file.
* `data-10k.csv`: This is the first 10k lines of data in the file (about 2.3 MB).
* `data-all.csv`: This is the full set of data with a total of 7.5MB of data.  

There is a fairly significant difference in the sizes of the files.  You should generally do your initial testing with the smaller files and then graduate to the "bigger" files with your final result coming from the `data-all.csv` file.  

**Note**: To get a sense of the file, update your version of the class GitHub repository or download one of the files from the class GitHub repository and open the file in either Excel (Windows or Mac) or Numbers (Mac OS X). There are also extensions for Visual Studio Code though those are not quite as easy as Excel or Numbers.

### Your Tasks

You will be writing code to accomplish the following tasks:

* *Fetch the data:* This code is provided for you to fetch the CSV file from a website and then to convert the received data into a CSV DictReader (a dictionary whereby the field names from the first row can be used to access the data).
* *Parse the CSV:* A small bit of example code is included that shows how to access the data demonstrating a printout of the `interface` and `tput_mbps` fields.  You will need to use the relevant fields (`interface`, `direction`) to put the relevant observed values (`tput_mbps`) into one or more of the appropriate lists (`allSpeeds`, `wiredSpeeds`, `wifiSpeeds`). 
   * Think about the test(s) that you might want to evaluate and what goes into what list. A partial example is already provided for `allSpeeds`. 
* *Compute the statistics:* Modify the `compute_stats` function to add in a computation for the relevant statistics (max, min, median, standard deviation) to the dictionary element using [NumPy](https://numpy.org)
* *Print the statistics:* Modify the `print_stats` function to print out the statistics that you just computed in the `compute_stats` function.
* *Finish the results:* Add in appropriate code to use only the downlink tests and to appropriately do separate statistics for the wired and wireless links by putting the data into an appropriate list.  

**Complete:** Show your code running correctly to Prof. Striegel for credit.

### Extensions

While not required, you are welcome to enhance the code in several ways including:

* *Better formatting:* By default, Python includes all of the digits when it comes to the respective floating point values.  Trim down the number of displayed digits to a reasonable amount and add in units to the various derived measurements.
* *Monthly statistics:* Compute monthly averages for the data starting in January of 2024 and working through May of 2024.  
* *Leaner code:* Modify the code to operate on a line by line basis as the data streams through for filtering rather than fetching all of the data and then processing all of data as a big blob.  
* *Cross over:* For a reasonable window of time (e.g. within an hour), does the WiFi speed ever get "close" to the wired speed? See if this ever happens within the data.

## End Result

Your GitHub submission will have a single file in the following location in your private repository:

* `/hw/lab-02/compute-stats.mine.py`

## Grading

The lab is worth a total of 15 points, ten points for each of the demonstrations and then five points for correct formatting / file locations:

* 10 pts each - Demonstrated successfully for Prof. Striegel
* 1 pt - Files are in the `lab-02` folder in your repository
* 1 pt - Files are named correctly
* 2 pt - Commit messages start with `lab-02`
   * This will be strictly enforced now.  At worst case, at a line to your code and then add in an additional comment.  
* 1 pt - Correct hash submitted via Canvas

The lab is due by Monday afternoon on June 3rd at 5 PM. 
