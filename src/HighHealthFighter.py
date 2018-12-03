import pygame
from src import Hero
class HighHealthFighter(Hero.Hero):
    def __init__(self, name, img_file , heaalth,damage):
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        Hero.__init__(self)
        self.name = name
        self.health = 300
        self.damage = 25
        self.restTime = 1 
    