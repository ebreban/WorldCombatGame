import pygame
class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, direction, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx  = x
        self.rect.centery  = y
        self.direction = direction
        self.yVel = 0
        self.gravity = 4
        self.isJumping = False
        self.health = 100
        self.damage = 100
        self.characterGround = y


        if(self.direction == "right"):
            self.image = pygame.transform.flip(self.image,True,False)

    def jump(self):
        """
            tests to make sure the hero isnt already jumping , then assigns a yVel(the highest point in the jump) and sets isJumping to true
        """
        #if (self.isJumping == False):
        #	self.yVel = -15
        #	self.isJumping = True
        self.rect.centery -= 40
        self.isJumping = True

    def moveRight(self):
        """
            moves the character to the right by changing their x coordinate
            returns nothing
        """
        self.rect.centerx += 10

    def moveLeft(self):
        """
            moves the character to the left by changing their x coordinate
            returns nothing
        """
        self.rect.centerx -= 10

    def fight(self, opponent):
        """
            takes the opponent character as a parameter
            deals damage to the opponent character
            returns true if the attack was fatal and false if the hero is still alive
        """
        if(self.health - opponent.getDamage() > 0):
            self.health -= opponent.getDamage()
            print("attack failed. Remaining Health: ", self.health)
            return False
        else:
            print("successful attack")
            return True

    def getHealth(self):
        """
            returns the health of the hero
        """
        return self.health
    def setHealth(self, x):
        """
            takes x as a parameter, which is the health value for the hero
            sets the health of the hero
            returns nothing
        """
        self.health = x
    def setDamage(self, x):
        """
            takes x as a parameter, which is the damage value for the hero
            sets the damage of the hero
            returns nothing
        """
        self.damage = x
    def getDamage(self):
        """
            returns the damage the hero does to opponents
        """
        return self.damage

    def getPos(self):
        """
            returns the postion of the hero in a tuple (centerx,centery)
        """
        return (self.rect.centery,self.rect.centerx)

    def setPos(self,x , y):
        """
            sets the position of the hero
        """
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        """
            implements the isJumping functionality
            returns nothing
        """
        #implements switching the direction the character faces
        #if self.direction == "right" :
        #    self.rect.centerx  += 10
        #    self.rect.centery  += 10
        #implements the isJump

        if (self.isJumping):
            self.rect.centery += self.gravity
            if(self.rect.centery == self.characterGround):
                self.isJumping = False


#use function to make them face each other
