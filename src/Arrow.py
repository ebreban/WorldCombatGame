import pygame
class Arrow(pygame.sprite.Sprite):
    def __init__(self, x , y , direction, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx  = x
        self.rect.centery  = y
        self.direction = direction
        self.speed = 10
        self.shoot = False
        

        if(self.direction == "right"):
                self.image = pygame.transform.flip(self.image,True,False)
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

    def update(self):
        #implements the flip
        self.rect.centerx  += self.speed
