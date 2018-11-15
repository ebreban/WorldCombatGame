import pygame
class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, x , y , direction)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx  = x
        self.rect.centery  = y
        self.direction = direction
        if(self.direction == "right"):
            self.image = pygame.transform.flip()
    def update(self):
        if direction == "right" 
            self.rect.centerx  += 10
            self.rect.centery  += 10