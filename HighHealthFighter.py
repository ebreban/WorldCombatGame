class HighHealthFighter(Hero, pygame.sprite.Sprite):

    def __init__(self, name):
    	self.name = name
        self.health = 300
        self.damage = 25
        self.restTime = 1 
    def damage(self):
    	return self.damage