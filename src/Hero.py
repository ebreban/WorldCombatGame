import pygame
class Hero():
    def __init__(self, name, x, y, direction, img_file, health):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx  = x
        self.rect.centery  = y
        self.direction = direction
        self.yVel = 0
        self.gravity = 1.2
        self.isJumping = false
        self.health = 100
        self.damage = 100
    
        #flips the character
        if(self.direction == "right"):
            self.image = pygame.transform.flip(self.image)

    def jump():
        """
            tests to make sure the hero isnt already jumping , then assigns a yVel(the highest point in the jump) and sets isJumping to true 
        """
        if (isJumping == false):
        	self.yVel = -15
        	self.isJumping = true
    
    
    def moveRight(self):
        """
            moves the character to the right
        """
        self.rect.x += self.speed
    
    def moveLeft(self):
        """
            moves the character to the left
        """
        self.rect.x -= self.speed
    
    def fight(self, opponent):
        """
            deals damage and returns true if the attack was fatal and false if the hero is still alive
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
            sets the health of the hero
        """
        self.health = x
    def setDamage(self, x):
        """
            sets the damage of the hero
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
        return (self.rect.centerx,self.rect.centery)

    def setPos(self,x , y):
        """
            sets the position of the hero 
        """
        self.rect.centerx = x
        self.rect.centery = y
    
    def update(self):
        
        #implements switching the direction the character faces
        if direction == "right" :
            self.rect.centerx  += 10
            self.rect.centery  += 10
        
        #implements the isJump
        if (isJumping):
            yVel += gravity
            self.rect.y += yVel
            if (self.rect.y > characterGround): 
                self.rect.y = characterGround
                yVel = 0
                isJumping = false


#use function to make them face each other
