import pygame
class DamagePowerUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, dval, x , y , direction)
	        self.image = pygame.image.load(img_file).convert_alpha()
	        self.rect = self.image.get_rect()
	        self.dval = dva;
	        self.rect.centerx  = x
	        self.rect.centery  = y
    def applyDamageUpgrade(self , hero):
            self.hero.damageDone += dval
    def update(self):