
#!/usr/bin/python
import smtplib
from email.mime.text import MIMEText as text

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

def sendSMS(receiver, id, password, message):
	print('work to be done')
