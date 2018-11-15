import pygame
import Hero
class HighDamageFighter(Hero , pygame.sprite.Sprite):

    def __init__(self, name, health, damage):
        self.health = 200
        self.damage = 50
        self.restTime = 3
    def damage(self):
    	return self.damage

