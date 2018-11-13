class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, pos , direction)
        self.image = pygame.image.load("arrow.png")
        self.rect = self.image.get_rect()
        self.rect.centerx  = pos[0]
        self.rect.centery  = pos[1]
        self.direction = direction
        if(self.direction == "right"):
            self.image = pygame.transform.flip()
    def update(self):
        if direction == "right" 
            self.rect.centerx  += 10
            self.rect.centery  += 10