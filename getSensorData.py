#author Yihan Pang 
#this code is the code that triggers the sensor to detect at a speciic range 
#in the demo it is set to detect person within 1 meter of the sensor and it will retake picture every 20 sec if the person continue standing infront the detection range
#the sensor will comunicate with subsciber to tell appriate message that triggers the camera and other fellow code. 
#do not run this program 
#run sudo python publisher.py
#this program contains 2 function getCredentials() and getSensorData(object)
import RPi.GPIO as GPIO
import time
import pika
import json
import signal
import os
import time

"""
GPIO.setmode(GPIO.BCM)
#initial setup
TRIG = 23
ECHO = 24
#assign pins
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

global waitstart
"""
""" Setup host credintial information """
def getCredentials():
	HOST =  'netapps.ece.vt.edu';
	VIRTUAL_HOST ='/2014/fall/immortal';
	NAME = 'immortal';
	PASS = 'N3verEnding)St0ry101';
	return HOST, VIRTUAL_HOST, NAME, PASS
	
def getSensorData(object):
	waitstart=time.time()
 	try:
		pause=0
		while object.getLoopState():
			"""
			#reset the sensor
			GPIO.output(TRIG, False)
			time.sleep(10) 
			#trigger the sensor
			GPIO.output(TRIG, True)
			time.sleep(0.00001)
			GPIO.output(TRIG, False)	
			while GPIO.input(ECHO)==0:
				pulse_start = time.time()
			while GPIO.input(ECHO)==1:
				pulse_end = time.time() 
			pulse_duration = pulse_end - pulse_start
			#calculate the distance
			distance = pulse_duration * 17150
			distance = round(distance, 2)
			#if visitor isn't previous triggered 
			if pause==0 and distance>2 and distance<100:
				pause=1 
				waitstart=time.time()
				message = {}
				message['type']="trigger"
				object.setMessage(message)
				object.setMessageSignal(True)
			#if the distance is greater than 1 meter it means the visitor is walking away retrigger the sensor
			elif pause==1 and distance>100:
				pause=0
			#if the person standing still for more than 20 second , retrigger the sensor
			elif time.time()-waitstart>20:
				pause=0				
			"""
			#send the message to message queue
			if object.getMessageSignal() == True:
				message = json.dumps(object.getMessage(), indent = 2)
				HOST, VIRTUAL_HOST, NAME, PASS = getCredentials();
				MessageBroker = pika.BlockingConnection(pika.ConnectionParameters(host = HOST,
											virtual_host = VIRTUAL_HOST,
											credentials=pika.PlainCredentials(NAME, PASS,True)))
				""" Setup the exchange """
				channel = MessageBroker.channel()
				channel.exchange_declare(exchange="HomeGuard",type="fanout")

				""" Send the message """
				channel.basic_publish(exchange="HomeGuard",
							routing_key="Detection", body= message)
				print message
				""" Close the connection """ 
				MessageBroker.close()
				object.setMessageSignal(False)
			
	except KeyboardInterrupt: 
		#clean GPIO pins
		GPIO.cleanup()
	
		
