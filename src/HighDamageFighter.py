import pygame
from src import Hero
class HighDamageFighter(Hero.Hero):
    def __init__(self,name,img_file, health, damage):
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        Hero.__init__(self)
        self.name = name
        self.health = 200
        self.damage = 50
        self.restTime = 3
 

