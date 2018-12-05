import pygame
class DamagePowerUp(pygame.sprite.Sprite):
    def __init__(self, x , y , img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.dval = 50
        self.rect.centerx  = x
        self.rect.centery  = y

    def applyUpgrade(self , hero):
        """
            adds the damage upgrade
        """
        hero.damage = hero.damage + self.dval


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

