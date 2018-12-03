import pygame
from src import Hero
class HighHealthFighter(Hero.Hero):
    def __init__(self, name):
        Hero.__init__(self)
        self.name = name
        self.health = 300
        self.damage = 25
        self.restTime = 1 
    