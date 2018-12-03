import sys
import pygame
from src import Hero 
from src import HighDamageFighter 
from src import HighHealthFighter 
from src import DamagePowerUp
from src import HealthPowerUp
from src import Arrow
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
        self.state = self.state = "MAIN"

        '''powerup = random.choice(["a","b"])
        if powerup == "a":
            self.healthPower = healthPower.HealthPowerUp()
        elif powerup == "b":
            self.DamagePower = DamagePower.DamagePowerUp()
        self.state = "GAME"'''

    def mainLoop(self):
        while True:
            if(self.state == "MAIN"):
                self.menuLoop()
            elif(self.state == "INFO"):
                self.instructionsLoop()
            elif(self.state == "SELECT"):
                self.SelectLoop()
            elif(self.state == "SCORE"):
                self.ScoreboardLoop()
            elif(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()
    def printMouseCoordinates(self, position):
        mouseFont = pygame.font.SysFont("Helvetica", 32)
        mouseLabel = mouseFont.render(str(position),1,(0,255,255))
        self.screen.blit(mouseLabel, (30,30))
   
    def displayInstructions(self):
        Instructions = pygame.image.load('assets/InstructionsScreen.png')
        self.screen.blit(Instructions, (0,0))

    def displayMainMenu(self):
        title = pygame.image.load('assets/TitleScreen.png')
        self.screen.blit(title, (0,0))

    def pickPlayerScreen(self):

        Select = pygame.image.load('assets/SelectScreen.png')
        self.screen.blit(Select, (0,0))
    def GameScreen(self):
        Background = pygame.image.load('assets/GameScreen.png')
        self.screen.blit(Background, (0,0))
    def ScoreScreen(self):
        scoreBoard = pygame.image.load("assets/ScoreScreen.png")
        self.screen.blit(scoreBoard, (0,0))
        
    def menuLoop(self):
        while self.state == "MAIN":
            mouse = pygame.mouse.get_pos()
            self.displayMainMenu()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if pygame.mouse.get_pressed():
                    if (113+415 > mouse[0] > 113) and (375+45 > mouse[1] > 375):
                    
                        print('click')
                        self.state = "INFO"
                    elif (202+232 > mouse[0] > 202) and (428+40 > mouse[1] > 428):
                    
                        self.state = "SELECT"
                    elif (249+142 > mouse[0] > 249) and (7+32 > mouse[1] > 7):
                    
                        self.state = "SCORE"
    def instructionsLoop(self):
        while self.state == "INFO":
            mouse = pygame.mouse.get_pos()
            self.displayInstructions()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if (19+143 > mouse[0] > 19) and (17+33 > mouse[1] > 17):
                    if pygame.mouse.get_pressed():
                        self.state = "MAIN"
    def ScoreboardLoop(self):
        while self.state == "SCORE":
            mouse = pygame.mouse.get_pos()
            self.ScoreScreen()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if (12+131 > mouse[0] > 12) and (435+32 > mouse[1] > 435):
                    if pygame.mouse.get_pressed():
                        self.state = "MAIN"
    def SelectLoop(self):
        while self.state == "SELECT":
            mouse = pygame.mouse.get_pos()
            self.pickPlayerScreen()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if 13+140 > mouse[0] > 13 and 21+33 > mouse[1] > 21:
                    if pygame.mouse.get_pressed():
                        self.state = "MAIN"
                elif 128+371 > mouse[0] > 128 and 116+80 > mouse[1] > 116:
                    if pygame.mouse.get_pressed():
                        self.state = "GAME"
                        self.player1 = player1.HighHealthFighter()
                        self.player1Arrow = player1Arrow.Arrow()
                        self.player2 = player2.HighDamageFighter()
                        self.player2Arrow = player2Arrow.Arrow()
                elif 128+371 > mouse[0] > 128 and 294+82 > mouse[1] > 294:
                    if pygame.mouse.get_pressed():
                        self.state = "GAME"
                        self.player2 = player2.HighHealthFighter()
                        self.player2Arrow = player2Arrow.Arrow()
                        self.player1 = player1.HighDamageFighter()
                        self.player1Arrow = player1Arrow.Arrow()

                    
    def gameLoop(self):
        while self.state == "GAME":
            self.GameScreen()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    
                    if(event.key == pygame.K_w):
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
                    elif(event.key == pygame.K_m):
                        self.player2Arrow()

            #check for collisions

            #if player = arrow(part of group)(use sprite collide, group kill):
                
            ''' arrowgroup = pygame.sprite.group.add
            arrowgroup.add(arrowobject)
            checking for collisions, call pygame.sprite.spritecollide(player,arrowgroup,True<means the arrow is killed>)
            iterate through the list for block_hit_list = collide for block in list: health -=1
            for player collisions pygame.sprite.collide_rect()
            '''

            #data permanance feature
            timeRunning = font.render('time: '+ str(pygame.time.get_ticks()/1000), False, (250,0,0))
            f = open("highscore.json", "rw")
            highscoreDict = json.load(f)
            scorelist = [highscoreDict.values()]
            for i in range(len(scoreList)):
                if timeRunning < scoreList[i]:
                    scoreList.append(timeRunning)
                    break
            scoreList.sort()
            newdict = {}
            for i in range(10):
                newdict[str(i)] = scorelist[i]
            json.dump(newdict)
            
            

            """redraw screen"""
            #self.screen.blit(self.background, (0, 0))
            '''if(self.hero.health == 0):
                self.state = "GAMEOVER"'''
            #pygame.display.flip()
            


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