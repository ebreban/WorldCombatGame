import pygame
class HealthPowerUp(pygame.sprite.Sprite):
    def __init__(self, x , y , img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.hval = 50
        self.rect.centerx  = x
        self.rect.centery  = y
    def applyHealthUpgrade(self , Hero):
        """
            adds the health upgrade
        """
        hero.setHealth(hero.getHealth + hval)

    
    def getPos(self):
        """
            returns the postion of the power-up in a tuple (centerx,centery)
        """
        return (self.rect.centerx,self.rect.centery)

    def setPos(self,x , y):
        """
            sets the position of the power-up 
        """
        self.rect.centerx = x
        self.rect.centery = y    
