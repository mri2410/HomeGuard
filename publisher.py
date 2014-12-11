"""
ECE 4564
Final Project
Team: Immortal
Title: HomeGuard - Home Visitors Detection and Alert System
Filename: publisher.py
Members: Arun Rai, Mohammad Islam, and Yihan Pang
Date: 11/26/2014

---------------------------------------------------------------------
Description:
1. Receive host user information, and send it to the subscriber.
2. Receive visitors' message and send it to the subscriber.
3. Receive sensor reading, and send trigger signal to camera to the subscriber.

Network protocols: TCP/IP and AMQP
---------------------------------------------------------------------
"""

#!/usr/bin/python

import sys
import threading
from infoSetup import infoSetup
from getSensorData import getSensorData
from setVisitorMessage import setVisitorMessage
import time
import signal
import socket
import json

""" Default host IP address and port number """
HOST = "127.0.0.1"
PORT = 9000

class HostInformation:
	def __init__(self):
		self.senderNumber = '';
		self.receiverNumber = ''
		self.receiverEmail = 'sangpang20@gmail.com';
		self.loop = True;
		self.s = '';
		self.emailOnly = True;
		self.smsOnly = False;
		self.both = False;
		self.Message = {};
		self.msgSignal = False;
		
	""" Set receiver's phone number """
	def setPhoneNumber(self, number):
		self.receiverNumber = number;
		self.smsOnly = True;
		self.emailOnly = False;
		self.both = False;
	""" Set receiver's email id """
	def setEmail(self, email):
		self.receiverEmail = email;
		self.emailOnly = True;
		self.smsOnly = False;
		self.both = False;
		
	""" Set both email and phone nubmer """
	def setBoth(self, email, phone):
		self.receiverEmail = email;
		self.receiverNumber = phone;
		self.both = True;
		self.emailOnly = False;
		self.smsOnly = False;
		
	def getReceiverNumber(self):
		return self.receiverNumber;
		
	def getReceiverEmail(self):
		return self.receiverEmail;
		
	def getSenderEmail(self):
		return self.senderEmail;
		
	def getSenderEmailPass(self):
		return self.senderPassword;
		
	def messageInEmail(self):
		return self.emailOnly;
		
	def messageInSms(self):
		return self.smsOnly;
		
	def messageInBoth(self):
		return self.both;
		
	def setLoopState(self, signal=None, frame=None):
		print 'Gracefully closing the socket .................'
		self.loop = False;
		self.s.close();
	
	""" Here, the message is of type dictionary """
	def setMessage(self, message):
		self.Message = message;
		
	def getMessage(self):
		return self.Message;
		
	def setMessageSignal(self, sig):
		self.msgSignal = sig;
	
	def getMessageSignal(self):
		return self.msgSignal;
		
	def getLoopState(self):
		return self.loop;
	
	""" The function is called before the program exits
		for gracefully closing the socket when user enters
		Ctrl + c. """
	def closeSocket(self, s):
		self.s = s;


def main():
	setHostInfo = HostInformation()
	""" Sensor thread: sensor reading is performed"""
	sensorThread = threading.Thread(target = getSensorData, args = [setHostInfo,]);
	""" start the thread """
	sensorThread.start()
	""" Setup signal handlers to shutdown this app when SIGINT 
		or SIGTERM is sent to this app """
	signal_num = signal.SIGINT
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((HOST, PORT))
		s.listen(1)
		""" main thread """
		while setHostInfo.getLoopState():
			try:
				setHostInfo.closeSocket(s);
				signal.signal(signal_num, setHostInfo.setLoopState)
				signal_num = signal.SIGTERM
				signal.signal(signal_num, setHostInfo.setLoopState)
			except ValueError as error1:
				print "Warning: Greceful shutdown may not be possible: Unsupported"
				print "Signal: " + signal_num
			
			conn, addr = s.accept()
			message = conn.recv(1024)
			if len(message) > 3:
				if message[0] == '$' and message[1] == '$' and message[2] == '$':
					setVisitorMessage(setHostInfo, message)
				else:
					infoSetup(setHostInfo, message)
		
	except socket.error, se:
		print 'connection failed/socket closed. \n', se
		if s:
			s.close();
			
	sensorThread.join()
	
if __name__ == '__main__':
	main();

