class Hero:
	def __init__(self, name, pos, direction, image):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.centerx  = pos[0]
        self.rect.centery  = pos[1]
        self.image = pygame.image.load()
        self.direction = direction
   		self.yVel = 0
        self.gravity = 1.2
		self.isJumping = false;
		if(self.direction == "right"):
            self.image = pygame.transform.flip()
	def jump():
		if (isJumping == false) 
        	self.yVel = -15
        	self.isJumping = true
    def moveRight(self):
    	self.rect.x += self.speed
    def moveLeft(self):
    	 self.rect.x -= self.speed
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