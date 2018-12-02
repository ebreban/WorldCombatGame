import sys
import pygame
import Hero
import HighDamageFighter
import HighHealthFighter
import DamagePowerUp
import HealthPowerUp
import Arrow
import random
class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        pygame.font.init()
        self.Title = pygame.sprite.Group()
        self.state = self.state = "GAME"

        if pygame.mouse.get_pressed() and pygame.mouse.get_pos() == x,y:
            self.displayMainMenu()
            if pygame.mouse.get_pressed() and pygame.mouse.get_pos() == x,y:
                self.pickPlayerScreen()
                if pygame.mouse.get_pressed() and pygame.mouse.get_pos() == x,y:
                    self.player1 = player1.HighHealthFighter()
                    self.player1Arrow = player1Arrow.Arrow()
                    self.player2 = player2.HighDamageFighter()
                    self.player2Arrow = player2Arrow.Arrow()
                elif pygame.mouse.get_pressed() and pygame.mouse.get_pos() == x,y:
                    self.player2 = player2.HighHealthFighter()
                    self.player2Arrow = player2Arrow.Arrow()
                    self.player1 = player1.HighDamageFighter()
                    self.player1Arrow = player1Arrow.Arrow()

        elif pygame.mouse.get_pressed() and pygame.mouse.get_pos() == x,y:
            self.displayInstructions()
            #lets the user go back to main menu From instruction screen
            if pygame.mouse.get_pressed() and pygame.mouse.get_pos() == x,y:
                self.displayMainMenu()

        powerup = random.choice(["a","b"])
        if powerup == "a":
            self.healthPower = healthPower.HealthPowerUp()
        elif powerup == "b":
            self.DamagePower = DamagePower.DamagePowerUp()



    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def displayMainMenu():
        title = pygame.image.load('assets/titlescreen.png')
        pygame.surface.blit()

    def dislayInstructions():
        temp = pygame.image.load(temp)
        pygame.surface.blit()

    def pickPlayerScreen():
        temp = pygame.image.load()
        pygame.surface.blit(temp)

    def gameLoop(self):
          """This is the Main Loop of the Game"""

        #what is the point of this
        pygame.key.set_repeat(1,50)

        while self.state == "GAME":
            pygame.surface.blit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif(event.key == pygame.K_w):
                    self.player1.jump()
                elif(event.key == pygame.K_a):
                    self.player1 .moveLeft()
                elif(event.key == pygame.K_d):
                    self.player1 .moveRight()
                elif(event.key == pygame.K_UP):
                    self.player2.jump()
                elif(event.key == pygame.K_LEFT):
                    self.player2.moveLeft()
                elif(event.key == pygame.K_RIGHT):
                    self.player2.moveRight()
                elif(event.key == pygame.K_e):
                    self.player1Arrow()
                elif(event.key == pygame.K_RCTRL):
                    self.player2Arrow()

            #check for collisions





            #data permanance feature
            timeRunning = font.render('time: '+ str(pygame.time.get_ticks()/1000), False, (250,0,0))
            f = open("highscore.json", "r")
            highscoreDict = json.loads(f)
            keys = highscoreDict.keys()
            for key in highscoreDict:
                if timeRunning > lowestScore :
                    lowestScore = highscoreDict[key]
                    lowestScoreKey = key
            z.write()

            """redraw screen"""
            self.screen.blit(self.background, (0, 0))
            if(self.hero.health == 0):
                self.state = "GAMEOVER"
    def gameOver(self):
        self.player1.kill()
        self.player1Arrow.kill()
        self.player2.kill()
        self.player2Arrow.kill()
        self.healthPower.kill()
        self.DamagePower.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0,0,0))
        self.screen.blit(message, (self.width/2,self.height/2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
