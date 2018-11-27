import pygame
class DamagePowerUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, dval, x , y , direction, img_file)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.dval = dval
        self.rect.centerx  = x
        self.rect.centery  = y
    def applyDamageUpgrade(self , Hero):
            self.hero.damageDone += dval
