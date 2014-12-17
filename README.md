<p>ECE 4564 - Network Application Design,</p>
<p>Team Immortal, Final Design Project</p>
<p>Visitor Detection and Alert System</p>
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
Please see the file called instruction.txt 





