import pygame
class HealthPowerUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, hval, x , y , direction)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.hval = hval
        self.rect.centerx  = x
        self.rect.centery  = y
    def applyHealthUpgrade(self , hero):
            self.hero.health += hval 
    def update(self):
        