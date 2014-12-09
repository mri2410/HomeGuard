"""
ECE 4564
Final Project
Team: Immortal
Title: HomeGuard - Home Visitors Detection and Alert System
Filename: subscriber.py
Members: Arun Rai, Mohammad Islam, and Yihan Pang
Date: 11/27/2014

---------------------------------------------------------------------
Description:
1. Receive host user information.
2. Receive visitors' message.
3. Receive camera trigger signal.

Network protocols: TCP/IP and AMQP
---------------------------------------------------------------------
"""

import pika
import json
import signal
from smsAndEmailToHost import sendEmailToHost
from playSound import play
import time

# User defined modules
from webcam_pi import snapshot
from webcam_pi import uploadFileToGit
from send_sms_twilio import sendTwilioSMS
from send_image_twilio import sendTwilioImage

def getCredentials():
	HOST =  '127.0.0.1' #'172.31.174.47';
	VIRTUAL_HOST ="mycomputer";
	NAME = 'arun';
	PASS = 'rai'#"1";
	return HOST, VIRTUAL_HOST, NAME, PASS

class HostInformation:
	def __init__(self):
		self.senderNumber = '555';
		self.receiverNumber = '666'
		self.senderEmail = 'homeguard96@gmail.com';
		self.senderPassword = 'detectionsystem'
		self.receiverEmail = 'sangpang20@gmail.com';
		self.twilloID = ''
		self.twilloPass = ''
		self.host = 'smtp.gmail.com'
		self.port = '587'
		self.emailOnly = True;
		self.smsOnly = False;
		self.both = False;
		
	""" Set receiver's phone number """
	def setPhoneNumber(self, number):
		self.smsOnly = True;
		self.emailOnly = False;
		self.both = False;
		self.receiverNumber = number;
		
	""" Set receiver's email id """
	def setEmail(self, email):
		self.emailOnly = True;
		self.smsOnly = False;
		self.both = False;
		self.receiverEmail = email;
		
	""" Set both email and phone nubmer """
	def setBoth(self, email, phone):
		self.receiverEmail = email;
		self.receiverNumber = phone;
		self.both = True;
		self.emailOnly = False;
		self.smsOnly = False;
		
	def getSenderNumber(self):
		return self.senderNumber;
		
	def getReceiverNumber(self):
		return self.receiverNumber;
		
	def getReceiverEmail(self):
		return self.receiverEmail;
		
	def getSenderEmail(self):
		return self.senderEmail;
		
	def getSenderEmailPass(self):
		return self.senderPassword;
		
	def getTwilloID(self):
		return self.twilloID;
		
	def getTwilloPass(self):
		return self.twilloPass;
		
	def messageInEmail(self):
		return self.emailOnly;
		
	def messageInSms(self):
		return self.smsOnly;
		
	def messageInBoth(self):
		return self.both;
		
	def getHost(self):
		return self.host;
		
	def getPort(self):
		return self.port;
		
class stopChannel:
    def __init__(self, channel):
        if isinstance(channel, pika.channel.Channel):
            self.__channel = channel;
        else:
            raise ValueError("No valid channel to manage was passed in")
    def stop_stats_client(self, signal=None, frame=None):
		""" stop the blocking consume operation """ 
		self.__channel.stop_consuming()
		
def messageHandler(info, message):
	if message['type'] == 'VisitorMessage':
		""" Receive the visitor's message """
		if info.messageInEmail():
			print 'send message via email'
			sendEmailToHost(info.getHost(), info.getPort(), info.getSenderEmail(), 
							info.getSenderEmailPass(), 
							info.getReceiverEmail(), message['body'],
							'Message from visitor')
			print info.getReceiverEmail()

		elif info.messageInSms():
			print ' send messageg via sms'
		elif info.messageInBoth():
			print 'send message via sms and email'
		
		# Sends a sms containing the visitor's message which will be sent to the host
		sendTwilioSMS(message['body'])
		
		print 'TWICE : ', info.getReceiverEmail()

		play('ThankYou.mp3');
		
	elif message['type'] == 'HostInfo':
		""" Receive host user information """
		if message['media'] == 'emailOnly':
			info.setEmail(message['body']['email'])
			print 'email and sms'
		elif message['media'] == 'smsOnly':
			info.setPhoneNumber(message['body']['number'])
			print 'sms only'
		elif message['media'] == 'both':
			info.setPhoneNumber(message['body']['number'])
			info.setEmail(message['body']['email'])
			print 'email only'
		print "HOST INFO CHECK\n"

	elif message['type'] == 'trigger':
		""" Receive the camera trigger signal and take action!"""
		print 'trigger the camera'
		""" Call function here"""
		# Calls the webcam function that takes a picture
		image = snapshot()	
				
		# Uploads the image file to Github account
		uploadFileToGit()		
		
		githubLink = 'https://github.com/mri2410/HomeGuard/blob/master/snapshots/'
		# Sends a sms containing the visitor's picture to the host's phone/email
		sendTwilioImage(githubLink + image)
			
def main():
	info = HostInformation();
	# print info.getHost(), " ", info.getPort(), " ", info.getSenderEmail()
	def messageFromBroker(channel, method, properties, message):
		print message
		""" load message """
		message = json.loads(message)
		messageHandler(info, message)
		
	HOST, VIRTUAL_HOST, NAME, PASS = getCredentials();
	""" Connect to the message broker """
	MessageBroker = pika.BlockingConnection(pika.ConnectionParameters(host = HOST,
											virtual_host = VIRTUAL_HOST,
											credentials=pika.PlainCredentials(NAME, PASS,True)))
	print "Succesfully connected to the publisher."

	""" Setup the exchange """
	channel = MessageBroker.channel()
	channel.exchange_declare(exchange="HomeGuard",type="fanout")

	""" Create a exclusive queue for receiving message """
	ch = MessageBroker.channel()
	MyQueue = ch.queue_declare(exclusive = True)

	""" Bind the queue to the chat room exchange """
	ch.queue_bind(exchange="HomeGuard", routing_key="Detection", queue=MyQueue.method.queue)

	""" Setup the callback for when a subscribed message is received """
	ch.basic_consume(messageFromBroker,  queue = MyQueue.method.queue, no_ack=True)
	print "Ready to receive message ........... "
	
	signal_num = signal.SIGINT
	try:
		channel_manager = stopChannel(ch)
		signal.signal(signal_num, channel_manager.stop_stats_client)
		signal_num = signal.SIGTERM
		signal.signal(signal_num, channel_manager.stop_stats_client)
	except ValueError, ve:
		print "Warning: Greceful shutdown may not be possible: Unsupported " \
			  "Signal: " + signal_num
				  
	""" Start a blocking consume operation """
	ch.start_consuming()


if __name__ == '__main__':
	main()
