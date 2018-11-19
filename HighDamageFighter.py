import pygame
import Hero
class HighDamageFighter(Hero , pygame.sprite.Sprite):

    def __init__(self, name, health, damage):
    	pygame.sprite.Sprite.__init__(self)
        self.health = 200
        self.damage = 50
        self.restTime = 3
    def doDamage(self):
    	return self.damage

