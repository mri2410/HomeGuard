HomeGuard
=========

ECE 4564: Raspberry Pi Project
To run the program, first open a terminal, create a directory and clone the directory in your local machine: $ git clone https://github.com/mri2410/HomeGuard

First user need to set their own email address 

This can be done by cd into the HostInformation Folder and run the excutable HostInformation. Select the appropriate option and enter the desired information

open the first terminal, cd into the directory run python playSound.py
open another terminal, cd into HomeGuard, run $ python publisher.py

open next terminal, cd into HomeInformation, run $ qmake $ make run the executable. choose email and enter your email id and phone number. Hit OK.

Note: the phone number must be registed to twillo.
cd into VisitorMessageBox, run $ qmake $ make run the executable. type a test message and hit OK. (Qt4 should be installed before these projects are run) Check you email, a message will be in your email inbox.

When finished, close the GUIs, and go back to terminal that you run the python file and enter Ctrl + c to exit the program.
