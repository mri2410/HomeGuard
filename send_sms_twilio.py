#!/usr/bin/env python

# This file sends a sms of the visitor's image to the cell phone number using twilio account. 
# Download the twilio-python library from http://twilio.com/docs/libraries

# Import the necessary modules
import twilio
from twilio.rest import TwilioRestClient

# Sends a picture of the visitor to the host's phone
def sendTwilioSMS(sms_body):
	# Account Sid and Auth Token from twilio.com/user/account
	account_sid = "AC76d77770817e9ad7884f16430d23fbdf"	# Account ID
	auth_token  = "7575b18d79cee2797c1ccf35360cb09c"	# Authentication Token
	
	try:
		client = TwilioRestClient(account_sid, auth_token)	# Creating a client
 
		print sms_body

		# If the url link is empty, then it shouldn't send a sms
		if not sms_body:
			print "Error: No content found to send the SMS."
			print "Visitor needs to type a message to send it to the host.\n"
			#sys.exit()
	
		else:
			sms_body = "Visitor spotted: " + sms_body
			print sms_body
			message = client.sms.messages.create(body=sms_body,\
				# Cell number, Twilio Number
				to = "+15712652653", from_= "+15054046300")
			print message.sid

	except twilio.TwilioRestException as errorSMS:
		print errorSMS

#sendTwilioSMS('Testing message.')


#    to="+15712652653",    # Replace with your phone number
#    from_="+15054046300") # Replace with your Twilio number
#print message.sid
