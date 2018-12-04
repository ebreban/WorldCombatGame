import pygame
from src import Hero
class HighHealthFighter(Hero.Hero):
    def __init__(self, name, x, y, direction, img_file):
        Hero.Hero.__init__(self, name, x, y, direction, img_file)
        self.health = 300
        self.damage = 25
        self.restTime = 1 
      
    
    
    