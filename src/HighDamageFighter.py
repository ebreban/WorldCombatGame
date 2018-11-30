import pygame
from Hero import Hero
class HighDamageFighter(Hero):
    def __init__(self,name, health, damage):
        Hero.__init__(self)
        self.name = name
        self.health = 200
        self.damage = 50
        self.restTime = 3
 

