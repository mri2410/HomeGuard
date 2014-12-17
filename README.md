<p>ECE 4564 - Network Application Design,</p>
<p>Team Immortal, Final Design Project</p>
<p>Visitor Detection and Alert System</p>
<p>Authors: Yihan Pang, Mohammad Islam, and Arun Rai </p>
===============================

Project Overview
========================
The Home Visitors Detection and Alert System is designed to detect visitors coming to a house, take their pictures, and send the host (the homeowner) an email message with the pictures. The system also allows the visitor to leave a text message or an email to the host by using a keyboard and a screen monitor that are installed at the entrance door. The goal of this system design is that, while being away from the home, the host can still keep track of his visitors.  When the host is away from the home, there are chances of property theft and/or destruction. This device, if installed properly, can provide the user with valuable information of the suspects. The system automatically triggers the camera to take the pictures of the visitors when the visitors are active in front of the door longer than three seconds and sends them to the host. Then the host can take action, if necessary.

Hardware Requirements
========================
<p>Two Raspberyy Pi</p>
<p>One HC-SRQ4 sensor</p>
<p>One Logitech webcam</p>
<p>Two Wi-Fy dongles</p>

Hardware Setup
========================
<p>Sensor Setup:</p>
<p>Use Wire or dupont cable to connect the HC-SR04 sensor to one raspberry’s GPIO PINsv

<p>Camera Setup:</p>
<p>Connect the webcam to a USB port of the other Raspberry Pi</p>

Required Python Library
========================
<p>json</p>
<p>os</p>
<p>pika</p>
<p>pygame</p>
<p>RPi</p>
<p>signal</p>
<p>socket</p>
<p>smtplib</p>
<p>sys</p>
<p>threading</p>
<p>time</p>
<p>twilio</p>

Program Step by Step Setup
========================
Please see instruction.txt file

Troubleshooting
========================
Please see instruction.txt file

File Manifest
========================
<p>Folder:</p>
  <p>HostInformation: contains the qt application and executable HostInformation for setting the email address and sending options</p> 
  <p>VisitorMessageBox: contains the qt application and executable VisitorMessageBox for visitor to send messages to user</p>
  <p>snapshots>: contains the uploaded photo </p>
<p> File:</p>
<p>README.md: a typical read me file</p>
<p>ThanksYou.mp3: recording played after the visitor sent the message </p>
<p>getSensorData.py: contains the functions that the sensor uses to detect human presence </p>
<p>getVisitorMessage.py: contains the function that get the message that the visitor wrote </p>
<p>infoSetup.py: receive the host user infomration from the HostInformation executable</p>
<p>instruction.txt: step by step walkthrough on how to run the program</p>
<p>welcome.mp3:welcome message when a visitor is detected by the sensor</p>
<p>instruction1.mp3: following message after welcome.mp3 is played</p>
<p>playSound.py:play different sound based on the message it received from message queue</p>
<p>publisher.py: </p>
<p>1. Receive host user information, and send it to the subscriber.</p>
<p>2. Receive visitors' message and send it to the subscriber.</p>
<p>3. Receive sensor reading, and send trigger signal to camera to the subscriber.</p>
<p>send_image_twilio.py: sends a sms of the visitor's image to the cell phone number using twilio account. </p>
<p>send_sms_twilio.py: sends a sms of the visitor's image to the cell phone number using twilio account. </p>
<p>setVisitorMessage.py:set the visitor entered message to be published to subscriber</p>
<p>smsAndEmailToHost.py:sends visitor message to text or email</p>
<p>subscriber.py:</p>
<p>1. Receive host user information.</p>
<p>2. Receive visitors' message.</p>
<p>3. Receive camera trigger signal.</p>
<p>webcame_pi.py: triggers the webcam after getting a signal from the publisher pi.</p>


Contacts
========================
<p>If you want to be informed about sensor:</p>
    <p> - email pyihan1@vt.edu</p>
<p>If you want to be informed about webcam:</p>
     <p>- email mri2410@vt.edu</p>
<p>If you want to be informed about GUI Interface and network communication :</p>
<p> - email raiarun52@gmail.com</p>

Acknowledgement
========================
We would like to use this opportunity to thanks Dr. William Plymale and Thaddeus Czauski for approving us to work on this project as our final team project as we learned and enhanced our knowledge on programming network applications. We also like to thank ECE Department of Virginia Tech for generously supporting us with the equipment we need for this project.  In the end, we also thanks the our entire classmates who generously help us on class forum on questions that we encountered in this project. Thanks you all and hope you all have a good winter break. 
<p>-Yihan Evan and Arun</p> 

