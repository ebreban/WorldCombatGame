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
        """
            adds the damage upgrade
        """
        hero.setDamage(hero.getDamage + dval)


    def setPos(self,x , y):
        """
            sets the position of the power-up 
        """
        self.rect.centerx = x
        self.rect.centery = y    
    def getPos(self):
        """
            returns the postion of the power-up in a tuple (centerx,centery)
        """
        return (self.rect.centerx,self.rect.centery)

