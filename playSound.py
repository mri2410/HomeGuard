
import pygame

def play(file):
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
		
