# Lab 1 - Introduction to the Raspberry Pi

| **Aspect** | **Information** |
| --- | --- | 
| **Assigned** | Monday, May 27th - Block 2 | 
| **Due** | Wednesday, May 29th - 5 PM | 
| **Team** | To be done individually |  
| **Canvas Link** | Lab 01 | 
| **Points** | 15 points | 

The purpose of this lab is to get you familiar with the Raspberry Pi and how we will be logging in to the Raspberry Pi and executing code. The goal of this lab is to get familiar with the following tools:

* `ssh`: SSH or Secure Shell is how we securely login to via a terminal to one of the six primary Raspberry Pi nodes that will be there on-site.  The recommended tool is [PuTTy](https://www.putty.org) for Windows or the Terminal for Mac (Applications / Utilities / Terminal).

* `scp`: scp or Secure Copy is how we will move files back and forth between the Raspberry Pi and your laptop. The recommended tool is [WinSCP](https://winscp.net/eng/index.php) for Windows or the Terminal for Mac or [Transmit](https://panic.com/transmit/) for Mac if you want a GUI.  

* Python + Git: We will be running our code from the pre-assignment on an actual Raspberry Pi. It is highly recommended that you install Python on your laptop.   

**Note:** We may modify the first week of labs depending on how smoothly WiFi and Internet access go at the classroom location.  

## Login Information

The full set of login information for the access point and the Raspberry Pi nodes can be found [here](https://docs.google.com/spreadsheets/d/1tQAg5t4ALLMz1rIG7U2OnAQE7PebsSOAPRozVkSFll4/edit?usp=sharing) via a [Google Sheet](https://docs.google.com/spreadsheets/d/1tQAg5t4ALLMz1rIG7U2OnAQE7PebsSOAPRozVkSFll4/edit?usp=sharing).

## End Result

Your submission will have files in the following locations in your private repository:

* `/hw/lab-01/hello.mine.py`
* `/hw/lab-01/sense-real.py`

## Setup - Logging In

For labs that we will be doing on-site, we have a total of six Raspberry Pi 5's as well as two Raspberry Pi 2 Zero's.  The Pi 5's are a bit faster while the Pi 2 Zero's are quite small / compact.  Both run a full blown operating system (a derivative of Debian for the Pi which is a type of Linux).  Both also support hardware interactions through the typical 40 pin header that we use to connect the Sense HAT that you had accessed via emulation in the pre-assignment.

Since transporting over an accompanying monitor, keyboard, and mouse is a bit tricky for each Raspberry Pi, we will be interfacing with the various Raspberry Pi nodes over WiFi and logging into them using a mechanism called ssh.  Long story short, ssh gives us what is known as a terminal which is essentially a login to the Rasbperry Pi.  

An individual can support multiple logins via ssh.  Now, for those of you doing the quick math, we have roughly 30+ students in the class and anywhere from six to eight nodes.  That means that we will be doing a bit of time sharing when using the actual hardware output as well as leaning heavily on the emulator that we used in the pre-assignment.  

### Get the Software

For now though, we are focusing on just being able to login to the Raspberry Pi nodes themselves.  To wit, you will need to do the following:

* If you are on Windows, download and install PuTTy as well as WinSCP.  For those of you familiar with other tools, you are welcome to use those as well.  
* If you are on a Mac, you can use the Terminal to do ssh.  It is recommended to get a GUI for doing file copying and Transmit is a fantastic app.  
* As an aside, some of you may have used Visual Studio to directly log-in / run code if you are a CSE student. Please avoid doing this as the Raspberry Pi and in particular the hardware can be a bit finicky.  

### Join the Access Point

Once you have the requisite software, join the `cse34468` access point.  You can find the relevant information about the password on Canvas for the access point as well as the relevant login information for the Raspberry Pi nodes.  In theory if everything is working, the real Internet will be bridged by Prof. Striegel's notebook and life will be grand.  If not, well, you may need to switch back and forth on WiFi for actual Internet access during the labs.   

We have a total of eight Raspberry Pi nodes at the following IP addresses:

| **Host Name** | **IP Address** | **Unit Type** |
| gep-rpi001 | 192.168.0.125 | Raspberry Pi 5 |
| gep-rpi002 | 192.168.0.126 | Raspberry Pi 5 |
| gep-rpi003 | 192.168.0.127 | Raspberry Pi 5 |
| gep-rpi004 | 192.168.0.128 | Raspberry Pi 5 |
| gep-rpi005 | 192.168.0.129 | Raspberry Pi 5 |
| gep-rpi006 | 192.168.0.130 | Raspberry Pi 5 |
| gep-rpi007z | 192.168.0.131 | Raspberry Pi 5 |
| gep-rpi008z | 192.168.0.132 | Raspberry Pi 5 |

You should pick one of the nodes to log in. To log in to the node, use the username `iotgep` 

For Windows, the user name is `iotgep` and you should enter the appropriate password (see in class or Canvas).  For the hostname, it is recommended that you enter the IP address of the host (e.g. 192.168.0.127).

For Mac, you would `ssh` in to `gep-rpi005` using the following command:

`ssh iotgep@192.168.0.129`

Whether or not you are using a Windows or Mac laptop, you should accept the key / identity for the Raspberry Pi.  Each time that you connect to a new Pi, you will see this same warning. Within a given lab, you should generally use the same Raspberry Pi.  You may switch between different Raspberry Pi nodes across different lab sessions as you will always have a copy of any source code files on your laptop.

### Find your Home 

Next, your task is to locate an appropriate directory to do a bit of work. There should be two directories present on each of the Rasbperry Pi nodes, a `solo` directory and a `group` directory.  Since this lab is an individual lab, you would be working under the `solo` directory. If there is not a `solo` or `group` present, go ahead and create those directories. 

Go to the `solo` directory and then create a directory using your Net ID as the directory name.

```
% cd solo
% mkdir striegel
% cd striegel
% pwd
% ls
```

`cd` stands for change directory which is how we move around when logged in.  `mkdir` makes a directory.  `pwd` prints the current directory or path where you are located.

Let's make sure Python runs next:

```
% python

exit()
```

### Uploading a File to the Pi

So now we know that we can run Python.  Now we are going to do a bit work combining a few things: making a file on our laptop, uploading the file to the Rasbperry Pi, and then running the file on the Raspberry Pi. 

1. Go to the public class repository and find the `hello.py` file that is located in `hw/lab-01`.
2. Create a new folder in your local repository (the one that has `student` in it) named `lab-01` and in that folder, create a file named `hello-mine.py`. 
3. Copy / past the content from `hello.py` into `hello-mine.py` and change `World` to be your first name.  
4. Save the file.
5. Use WinSCP or Transmit and copy the `lab-01` directory to the same Raspberry Pi where you are / were logged in.  
6. Go to the terminal and then run the code via `python hello-mine.py` noting that you will need to change into the appropriate directory `cd lab-01` before running the code.  

**Checkpoint**: Demonstrate this code working to Prof. Striegel.

### Commit / Push to GitHub

Commit the change to your local repository and then push it to GitHub starting your commit message with `lab-01`, e.g. `lab-01 Pushing hello world`. The initial `lab-01` helps for grading and identifying which commits go with which labs or homework.  

## Test the Sense HAT

Now that we have things working, our next task is to run / confirm that we have use the [Sense HAT](https://pythonhosted.org/sense-hat/).  This is where things get a bit trickier due to class numbers as we have more students than Rasbperry Pi nodes and these early labs are being done individually.

1. Figure out where the Raspberry Pi that you are logged into is physically located
2. Find your code from the pre-assignment that drove the LEDs with a N and a D and copy that same code into the `lab-01` directory on your local repository.  Name the file `sense-real.py`.
3. Modify the code to include your name and e-mail at the top of the file (see the commented lines at the top of the `hello.py` file for an example).  
4. Copy the file (your pre-assignment code) to the Raspberry Pi in the `lab-01` directory where you had previously uploaded the code. 
5. **Important:** Confirm that no-one else is using the Sense HAT (LEDs on the Pi) via Prof. Striegel.  Prof. Striegel will have sheets of paper and whomever has the sheet of paper for a Pi has rights for the Pi for the next 5-10 minutes.  
6. Run / demonstrate your code running live on the Rasbperry Pi for Prof. Striegel.
7. Return the sheet of paper.  
8. Commit the change to your local repository and then push it to GitHub starting your commit message with `lab-01`, e.g. `lab-01 Sense HAT code as demonstrated`.
9. Submit the hash associated with the last commit on Canvas.  

## Grading

The lab is worth a total of 15 points, five points for each of the demonstrations and then five points for correct formatting / file locations:

* 5 pts each - Demonstrated successfully for Prof. Striegel
* 1 pt - Files are in the `lab-01` folder in your repository
* 1 pt - Files are named correctly
* 2 pt - Commit messages start with `lab-01`
* 1 pt - Correct hash submitted via Canvas

The lab is due by Wednesday afternoon at 5 PM. 
