#SpaceInvador Using Pygame
import pygame

#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

running = True        #variable to exit pygame window loop
while running:
	#checking events inside pygame window
	for event in pygame.event.get():    
		if event.type == pygame.QUIT:
			running = False
