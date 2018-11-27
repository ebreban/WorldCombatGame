import pygame
from Hero import Hero
class HighHealthFighter(Hero):
    def __init__(self, name):
        Hero.__init__(self)
        self.name = name
        self.health = 300
        self.damage = 25
        self.restTime = 1 
    def doDamage(self):
    	return self.damage
