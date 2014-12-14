# Created by Arun Rai
# 11/25/2014
# Edited on 12/14/2014

import pygame
import pika
import json
import signal
import time

from subscriber import getCredentials

def play(file):
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
		
class stopChannel:
    def __init__(self, channel):
        if isinstance(channel, pika.channel.Channel):
            self.__channel = channel;
        else:
            raise ValueError("No valid channel to manage was passed in")
    def stop_stats_client(self, signal=None, frame=None):
		""" stop the blocking consume operation """ 
		self.__channel.stop_consuming()
		
def main():
	def messageFromBroker(channel, method, properties, message):
		print message
		if message == 'trigger':
			""" Visitor is detected, welcome the visitor """
			play('welcome.mp3');
			sleep(2);
			play('instruction1.mp3');
		elif message == 'VisitorMessage':
			""" Visitor's message received. Thank visitor for the message !"""
			play('ThankYou.mp3');
		""" load message """
		
	HOST, VIRTUAL_HOST, NAME, PASS = getCredentials();
	""" Connect to the message broker """
	MessageBroker = pika.BlockingConnection(pika.ConnectionParameters(host = HOST,
											virtual_host = VIRTUAL_HOST,
											credentials=pika.PlainCredentials(NAME, PASS,True)))
	print "Succesfully connected to the publisher."

	""" Setup the exchange """
	channel = MessageBroker.channel()
	channel.exchange_declare(exchange="Play",type="fanout")

	""" Create a exclusive queue for receiving message """
	ch = MessageBroker.channel()
	MyQueue = ch.queue_declare(exclusive = True)

	""" Bind the queue to the chat room exchange """
	ch.queue_bind(exchange="Play", routing_key="Sound", queue=MyQueue.method.queue)

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

"""
play('welcome.mp3');
time.sleep(2);
play('instruction1.mp3');
play('ThankYou.mp3');
"""
