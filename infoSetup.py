
# Created by Arun Rai
# 11/25/2014

import time

""" Receive the host user information from the Graphical User Interface
	,place the information in a dictionary, trigger the message siganl for
	publishing the message to the subscriber. 
	The subscriber refers to the application in the camera side that receives
	camera host user information, visitor's message, and camera trigger signal."""

def infoSetup(setHostInfo, message):
	if message[0] == '<' and message[1] == '<' and message[2] == '<':
		email = message[3:len(message)]
		""" This is an email id of the host user. """
		setHostInfo.setEmail(email);
	elif message[0] == '>' and message[1] == '>' and message[2] == '>':
		phone = message[3:len(message)]
		""" This is a phone number of the the host user. """
		setHostInfo.setPhoneNumber(phone);
	elif message[0] == '-' and message[1] == '-' and message[2] == '-':
		extractMessage = message[3:len(message)]
		i = 0; loop = True;
		email = '' ; phone = ''
		while (loop):
			if extractMessage[i] == '+':
				loop = False
			else:
				email = email + extractMessage[i];
				i +=1;
		phone = extractMessage[(i + 1):len(extractMessage)];
		""" Both email id and phone number of the host user.
			This is the case when the user wants to receive 
			messages via both media."""
		setHostInfo.setBoth(email, phone);
	message = {}
	""" A dictionary is created that is sent as a json object to the camera side program
		which contains subscriber file. the object cotains message type and body
		messae types are host user info, visitor's message, and camera trigger signal."""
	""" set message type """
	message['type'] = 'HostInfo'
	body = {}
	""" Set host user number if available"""
	body['number'] = setHostInfo.getReceiverNumber();
	""" Set user email id if available """
	body['email'] = setHostInfo.getReceiverEmail();
	""" message body contains the email and phone number of the host user """
	message['body'] = body
	""" Set cases weather the host user wants to receive the message via
		email, sms, or both """
	if setHostInfo.messageInBoth():
		message['media'] = 'both'
	else:
		if setHostInfo.messageInEmail():
			message['media'] = 'emailOnly'
		elif setHostInfo.messageInSms():
			message['media'] = 'smsOnly'
		else:
			message['media'] = 'emailOnly'
	print 'Host info setup message received as, '
	""" Set message for publishing it to the subscriber """
	setHostInfo.setMessage(message)
	""" Set message signal true """
	setHostInfo.setMessageSignal(True)
