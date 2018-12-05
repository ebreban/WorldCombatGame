import pygame
class HealthPowerUp(pygame.sprite.Sprite):
    def __init__(self, x , y , img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.hval = 50
        self.rect.centerx  = x
        self.rect.centery  = y
    def applyUpgrade(self , hero):
        """
            takes one parameter, the hero which is receiving the upgrade
            applies the health upgrade to the correct character
            returns nothing
        """
        hero.health = hero.health + self.hval


    def getPos(self):
        """
            returns the postion of the power-up in a tuple (centerx,centery)
        """
        return (self.rect.centerx,self.rect.centery)

    def setPos(self,x , y):
        """
            takes x and y coordinates as parameters
            sets the position of the power-up
            returns nothing
        """
        self.rect.centerx = x
        self.rect.centery = y
