import sys
import pygame
from src import Hero
from src import HighDamageFighter
from src import HighHealthFighter
from src import DamagePowerUp
from src import HealthPowerUp
from src import Arrow

class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        pygame.font.init() 

        typestore = ""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if two player
                	#allow player1 to choose which fighter to use
                	#create an instance of that fighter
                	#allow player2 to choose which fighter to use
                	#create an instance of that fighter

                if single player
                		#allow player to choose which fighter to use
                		#create an instance of that fighter
                		#create an instance of the opposite fighter to serve as an enemy
                   
                        
    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
        """This is the Main Loop of the Game"""
        pygame.key.set_repeat(1,50)
        while self.state == "GAME":
            self.background.fill((250, 250, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.jump()
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move_right()