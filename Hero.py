import pygame
class Hero():
	def __init__(self, name, x, y, direction, img_file, health):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.centerx  = x
        self.rect.centery  = y
        self.image = pygame.image.load(img_file).convert_alpha()
        self.direction = direction
       	self.yVel = 0
        self.gravity = 1.2
    	self.isJumping = false
        self.health = 100
    	if(self.direction == "right"):
            self.image = pygame.transform.flip()
	def jump():
		if (isJumping == false) 
        	self.yVel = -15
        	self.isJumping = true
    def move_right(self):
    	self.rect.x += self.speed
    def move_left(self):
    	 self.rect.x -= self.speed
    def fight(self, opponent):
        if(self.health - opponent.damage() > 0):
            self.health -= opponent.damage()
            print("attack failed. Remaining Health: ", self.health)
            return False
        else:
            print("successful attack")
            return True
    def update(self):
        if direction == "right" :
            self.rect.centerx  += 10
            self.rect.centery  += 10
        if (isJumping) {
            yVel += gravity
            self.rect.y += yVel
            if (self.rect.y > characterGround) 
                self.rect.y = characterGround
                yVel = 0
                isJumping = false