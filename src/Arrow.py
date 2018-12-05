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
        self.fired = False
        

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
    def jump(self):
        """
            tests to make sure the arrow isnt already jumping , then assigns a yVel(the highest point in the jump) and sets isJumping to true 
        """
        #if (self.isJumping == False):
        #   self.yVel = -15
        #   self.isJumping = True
        self.rect.centery -= 80
        self.isJumping = True
    
    def moveRight(self):
        """
            moves the arrow to the right
        """
        self.rect.centerx += 10
    
    def moveLeft(self):
        """
            moves the arrow to the left
        """
        self.rect.centerx -= 10    

    def update(self):
        #implements the flip
        if(self.fired):    
            self.rect.centerx  += self.speed

        
