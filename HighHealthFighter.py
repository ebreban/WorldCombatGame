import pygame
import Hero
class HighHealthFighter(Hero, pygame.sprite.Sprite):

    def __init__(self, name):
    	pygame.sprite.Sprite.__init__(self)
	    	self.name = name
	        self.health = 300
	        self.damage = 25
	        self.restTime = 1 
    def doDamage(self):
    	return self.damage