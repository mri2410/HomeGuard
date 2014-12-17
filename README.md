ECE 4564 - Network Application Design,
Team Immortal, Final Design Project
Visitor Detection and Alert System
===============================

Project Overview
========================
The Home Visitors Detection and Alert System is designed to detect visitors coming to a house, take their pictures, and send the host (the homeowner) an email message with the pictures. The system also allows the visitor to leave a text message or an email to the host by using a keyboard and a screen monitor that are installed at the entrance door. The goal of this system design is that, while being away from the home, the host can still keep track of his visitors.  When the host is away from the home, there are chances of property theft and/or destruction. This device, if installed properly, can provide the user with valuable information of the suspects. The system automatically triggers the camera to take the pictures of the visitors when the visitors are active in front of the door longer than three seconds and sends them to the host. Then the host can take action, if necessary.

Hardware Requirements
========================
Two Raspberyy Pi
One HC-SRQ4 sensor
One Logitech webcam
Two Wi-Fy dongles

Hardware Setup
========================
Sensor Setup:
Use Wire or dupont cable to connect the HC-SR04 sensor to one raspberry’s GPIO PINs

Camera Setup:
Connect the webcam to a USB port of the other Raspberry Pi




System Setup
===============================
One Raspberry Pi is connected with the webcam and the other one is connected with the sensor. Now, setup the WiFi communication between the Pi using the WiFy dongles. Help of setting up WiFy in a Raspberry Pi device is available online.
    
The System integrates two application modules: Publisher and Subscriber
The sytstem uses AMQP network protocol for message communication between publisher and subscriber applications. To configure AMQP on the system, RabbitMQ must be installed on the both modules.
Instructions for installing RabbitMQ on the system modules:
1. Install Pika
    sudo apt-get install python-pip
    sudo pip install pika

2. Install RabbitMq
    - Add the following line to your /etc/apt/sources.list:     
        deb http://www.rabbitmq.com/debian/ testing main
    - To avoid warnings about unsigned packages, add the public key to the trusted key list using apt-key(8):     
        wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
        sudo apt-key add rabbitmq-signing-key-public.asc
    - Run:  sudo apt-get update
    - Run: sudo apt-get install rabbitmq-server

3. Create user credentials and virtual hosts:
    sudo rabbitmqctl add_user "name" "password"
    sudo rabbitmqctl add_vhost "my_new_vhostname"
    sudo rabbitmqctl set_permissions -p "my_new_vhostname" "name"  ".*" ".*" ".*"

4. In the command prompt/terminal, the user input should be in this format:
    python pistatsd.py [-h] -b message broker [-p virtual host] [-c login:password] [-k routing key]

Note:
    - Message broker can be set to: 127.0.0.1 for local machine.
    - Virtual host must match the "my_new_vhostname" entered during step 3.
    - Login ID also has to match the “name” in step 3.
    - Routing key has to be same in both client and server side to get same output.

i) Publisher: This application module includes the Raspberry Pi that is connected to the sensor.
Instructions for running the application:
This application requires Qt 4.8 application software to be installed either on Raspberry Pi or the Linux host machine such as Ubuntu.
Method A. By installing Qt on the Raspberry Pi
Log into the Raspberry Pi using PuTTy, or similar application.
Follow the instructions to install Qt libraries and compiler from the web link:http://qt-project.org/wiki/RaspberryPi_Beginners_guide
Make a directory in the pi (example, $ mkdir MyCoolSystem)
cd into the directory and clone the project.
    $ git clone https://github.com/mri2410/HomeGuard
    Note: git must be installed before cloning the directory.
    Git installation: $ apt-get install git
      5)  run $ ifconfig to see the Pi’s IP address, note the IP address - it is listed on the second line of ‘wlan0’
      6)  cd into the directory, and open the getSensorData.py
$ nano getSensorData.py
      7)   Navigate to function setCredentials(), set HOST, VIRTUAL_HOST, NAME, PASS fields, and save the file.
8) run $ publisher.py
9) open another terminal and cd into HostInformation
10) run $ qmake and $ make to generate an executable file.
11) run $ ./HostInfoSetup to run the application - host can setup the information as necessary by following the instructions on the application window.
12) open another, cd into VisitorMessageBox and follow instruction 10
13) run $ ./MessageBox to run the application - This will open an application window with a text box where visitors can type their message and send to host by hitting ‘OK’ button.
    
Method B. By installing Qt on the host machine (Ubuntu):
install Qt on the host machine: $ sudo apt-get install build-essential cmake gdb qt5-qmake qttools5-dev-tools
install the fswebcam package:
$ sudo apt-get install fswebcam
Follow instruction 1-5 from Method A and obtain the Pi’s wireless IP address.
open a terminal on Ubuntu and run $ ssh pi@ip_adress to log into the Pi.
cd into the project directory that is recently cloned. 
cd into HostInformation
run $ nano mainwindow.cpp
Change the IP address in IP_Address with the Pi’s IP address
cd into the VisitorMessageBox and follow instructions 6 and 7 above.
run $ publisher.py in the Pi
open two terminals on the host machine and follow instructions 9-13 from Method B

ii) Subscriber.py: This application module includes the Raspberry Pi that is connected to the camera.
This application requires twilio to  be installed on the Pi.
log into the other Raspberyy Pi using PuTTy or similar applicattion or from a Linux host machin such as Ubuntu.
install twilio by running, $ easy_install twilio
cd into the directory and clone the project.
    $ git clone https://github.com/mri2410/HomeGuard
    Note: git must be installed before cloning the directory.
    Git installation: $ apt-get install git
      4)  run $ ifconfig to see the Pi’s IP address, note the IP address - it is listed on the second line of ‘wlan0’
Note: In order for the host user to receive SMS, the host must obtain a twilio account.
5) run $ nano send_sms_twilio.py
6) find "to =_______  from =________" .
Fill in the field with the host’s phone number and the twilio number. Save the file.
7) run $ nano send_image_twilio.py and follow instruction 6 above.
8) cd into subscriber.py, and Navigate to function setCredentials() and set HOST, VIRTUAL_HOST, NAME, PASS fields.
9) open a terminal in the Pi and run $ subscriber.py
10) clone the project in the local host machine too for running recorded sound.
11) follow instruction 8 and run $ playSound.py

The system is ready!
          
Specify Resolution
The webcam used in this example has a resolution of 1280 x 720 so to specify the resolution I want the image to be taken at, use the -r flag:
fswebcam -r 1280x720 image2.jpg
2. Command Line Image Viewer:
$ sudo apt-get install links2
links2 -g <picture.jpg> 
 A window will come up with the captured picture.
 
 

