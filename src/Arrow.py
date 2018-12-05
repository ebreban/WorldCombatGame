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
        self.damage = 10


        if(self.direction == "right"):
                self.image = pygame.transform.flip(self.image,True,False)
    def getPos(self):
        """
            returns the postion of the power-up in a tuple (centerx,centery)
        """
        return (self.rect.centerx,self.rect.centery)

    def setPos(self,x , y):
        """
            takes x and y coordinates as the paremeter
            sets the position of the power-up
            returns nothing
        """
        self.rect.centerx = x
        self.rect.centery = y
    def getDamage(self):
        """
            returns the damage the arrow does to opponents
        """
        return self.damage
    def jump(self):
        """
            tests to make sure the arrow isnt already jumping , then assigns a yVel(the highest point in the jump) and sets isJumping to true
            returns nothing
        """
        
        self.rect.centery -= 80
        self.isJumping = True

    def moveRight(self):
        """
            moves the arrow to the right
            returns nothing
        """
        self.rect.centerx += 10

    def moveLeft(self):
        """
            moves the arrow to the left
            returns nothing
        """
        self.rect.centerx -= 10

    def update(self):
        """
            updates the arrow's speed if it is being fired
            returns nothing
        """
        if(self.fired):
            self.rect.centerx  += self.speed
