#!/usr/bin/env python

# This file sends a sms of the visitor's image to the cell phone number using twilio account. 
# Download the twilio-python library from http://twilio.com/docs/libraries

# Import the necessary modules
import twilio
from twilio.rest import TwilioRestClient

# Sends a picture of the visitor to the host's phone
def sendTwilioImage(image_url):
	# Account Sid and Auth Token from twilio.com/user/account
	account_sid = "AC76d77770817e9ad7884f16430d23fbdf"	# Account ID
	auth_token  = "7575b18d79cee2797c1ccf35360cb09c"	# Authentication Token
	client = TwilioRestClient(account_sid, auth_token)	# Creating a client
 
	print image_url

	# If the url link is empty, then it shouldn't send a sms
	if not image_url:
		print "Error: URL not found for the sms."
		print "URL is needed to send the sms to the user's phone.\n"
		#sys.exit()
	
	else:
		body_url = "Visitor spotted: " + image_url
		print body_url
		message = client.sms.messages.create(body=body_url,\
			# Cell number, Twilio Number
			to = "+15712652653", from_= "+15054046300")
		print message.sid

sendTwilioImage('https://github.com/mri2410/HomeGuard/blob/master/snapshots/visitor_8:51:38_11:26:2014.jpg')
#lease?! I love you <3",
#    to="+15712652653",    # Replace with your phone number
#    from_="+15054046300") # Replace with your Twilio number
#print message.sid
