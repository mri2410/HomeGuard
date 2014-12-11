
# Created by Arun Rai
# 11/25/2014

#!/usr/bin/python
import smtplib
from email.mime.text import MIMEText as text
from send_sms_twilio import sendTwilioSMS
from send_image_twilio import sendTwilioImage

""" Send message to the host via email """
def sendEmailToHost(host, port, sender, password, receiver, message = 'No message content.', subject = 'No subject'):
	try:
		mail = smtplib.SMTP(host, port)
		mail.ehlo()
		mail.starttls()
		mail.login(sender, password);
		msg = text(message)
		msg['Subject'] = subject
		mail.sendmail(sender, receiver, msg.as_string())      
		mail.close()
	except smtplib.SMTPRecipientsRefused:
		print 'Receipient refused to receive the message.'
	except smtplib.SMTPAuthenticationError:
		print 'User authentication error. \nServer did not accept username/password.'
	except smtplib.SMTPConnectError:
		print 'Unknown error while connecting to the host.'
	except Exception:
		print 'Unable to connect to the host. \nCheck the host address.'

def sendSMS(message, type):
	if type == 'VisitorMessage':
		sendTwilioSMS(message)
	elif type == 'VisitorImage':
		sendTwilioImage(message);
