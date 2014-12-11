
# Created by Arun Rai
# 11/25/2014

import sys
from smsAndEmailToHost import sendEmailToHost

""" Receive the visitor's message, set it in
	a dictionary """
def setVisitorMessage(setHostInfo, message):
	""" parse string to receive message body """
	visitorMsg = message[3:len(message)]
	message = {}
	""" Set message type """
	message['type'] = 'VisitorMessage'
	""" Set main message body """
	message['body'] = visitorMsg;
	""" Set message for publishing it to the subscriber"""
	setHostInfo.setMessage(message)
	""" Set message signal true """
	setHostInfo.setMessageSignal(True);
	
			
