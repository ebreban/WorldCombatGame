import sys
import pygame
from src import Hero 
from src import HighDamageFighter 
from src import HighHealthFighter 
from src import DamagePowerUp
from src import HealthPowerUp
from src import Arrow
import random
import json
import os

def pathname(dir):
    return os.path.join(os.getcwd(),dir)

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
        self.temp = "0"
        self.powerup = random.choice(["a","b"])
        

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
    def printJSON(self, word,x,y,size,r,g,b):
        mouseFont = pygame.font.SysFont("Helvetica", size)
        mouseLabel = mouseFont.render(str(word),1,(r,g,b))
        self.screen.blit(mouseLabel, (x,y))
   
    def displayInstructions(self):
        Instructions = pygame.image.load(pathname('assets/InstructionsScreen.png'))
        self.screen.blit(Instructions, (0,0))

    def displayMainMenu(self):
        title = pygame.image.load(pathname('assets/TitleScreen.png'))
        self.screen.blit(title, (0,0))

    def pickPlayerScreen(self):

        Select = pygame.image.load(pathname('assets/SelectScreen.png'))
        self.screen.blit(Select, (0,0))
    def GameScreen(self):
        Background = pygame.image.load(pathname('assets/GameScreen.png'))
        self.screen.blit(Background, (0,0))
    def ScoreScreen(self):
        scoreBoard = pygame.image.load(pathname("assets/ScoreScreen.png"))
        self.screen.blit(scoreBoard, (0,0))
        f = open("highscore.json", "r")
        HD = json.load(f)
        sList = list(HD.values())
        temp = 120
        self.printJSON("In Seconds",420,93,20,0,0,0)
        for i in range(1,11):    
            self.printJSON(str(i),220,temp,20,250,250,250)
            self.printJSON(HD[str(i)],260,temp,20,250,250,250)
            temp +=34
    def menuLoop(self):
        while self.state == "MAIN":
            mouse = pygame.mouse.get_pos()
            self.displayMainMenu()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (113+415 > mouse[0] > 113) and (375+45 > mouse[1] > 375):
                    
                        print('click')
                        self.state = "INFO"
                    elif (202+232 > mouse[0] > 202) and (428+40 > mouse[1] > 428):
                    
                        self.state = "SELECT"
                    elif (249+142 > mouse[0] > 249) and (7+32 > mouse[1] > 7):
                    
                        self.state = "SCORE"
            pygame.display.update()
    def instructionsLoop(self):
        while self.state == "INFO":
            mouse = pygame.mouse.get_pos()
            self.displayInstructions()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (19+143 > mouse[0] > 19) and (17+33 > mouse[1] > 17):
                        self.state = "MAIN"
    def ScoreboardLoop(self):
        while self.state == "SCORE":
            mouse = pygame.mouse.get_pos()
            self.ScoreScreen()
            #self.printJSON("oof",283,155,20,0,255,255)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (12+131 > mouse[0] > 12) and (435+32 > mouse[1] > 435):
                        self.state = "MAIN"
            pygame.display.update()
    def SelectLoop(self):
        while self.state == "SELECT":
            mouse = pygame.mouse.get_pos()
            self.pickPlayerScreen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 13+140 > mouse[0] > 13 and 21+33 > mouse[1] > 21:
                    
                        self.state = "MAIN"
                    elif 128+371 > mouse[0] > 128 and 116+80 > mouse[1] > 116:
                    
                        self.state = "GAME"
                        self.player1 = HighHealthFighter.HighHealthFighter("player 1",30,320,"left",pathname("assets/healthwarrior.png"))
                        self.player1Arrow = Arrow.Arrow(40,360,"left",pathname("assets/arrow.png"))
                        self.player2 = HighDamageFighter.HighDamageFighter("player 2",400,320,"right",pathname("assets/damagewarrior.png"))
                        self.player2Arrow = Arrow.Arrow(390,360,"right",pathname("assets/arrow.png"))
                        self.player2Arrow.speed = -10
                        
                    elif 128+371 > mouse[0] > 128 and 294+82 > mouse[1] > 294:
                    
                        self.state = "GAME"
                        self.player2 = HighHealthFighter.HighHealthFighter("player 2",400,320,"right",pathname("assets/healthwarrior.png"))
                        self.player2Arrow = Arrow.Arrow(390,320,"right",pathname("assets/arrow.png"))
                        self.player1 = HighDamageFighter.HighDamageFighter("player 1",30,320,"left",pathname("assets/damagewarrior.png"))
                        self.player1Arrow = Arrow.Arrow(40,320,"left",pathname("assets/arrow.png"))
                        self.player2Arrow.speed = -10
                        
            #if self.temp == "y":
            #    self.screen.blit(self.player1.image, (30,30))
            #    pygame.display.flip()
            #elif self.temp == "z":
            #    self.screen.blits(self.player1.image,(30,30)),(self.player2.image,(0,0)),(self.player1Arrow.image,(0,0)),(self.player2Arrow.image,(0,0))
            pygame.display.update()             

                    
    def gameLoop(self):
        #pygame.key.set_repeat(10,10)
        while self.state == "GAME":
            self.GameScreen()
            self.screen.blit(self.player1.image,(self.player1.rect.centerx,self.player1.rect.centery))
            self.screen.blit(self.player2.image,(self.player2.rect.centerx,self.player2.rect.centery))
            #self.screen.blit(self.player1Arrow.image,(self.player1Arrow.rect.centerx,self.player1Arrow.rect.centery))
            #self.screen.blit(self.player2Arrow.image,(self.player2Arrow.rect.centerx,self.player2Arrow.rect.centery))
            if self.powerup == "a":
               self.HealthPower = HealthPowerUp.HealthPowerUp(240,270,pathname("assets/DamagePowerUp.png"))
               self.screen.blit(self.HealthPower.image,(self.HealthPower.rect.centerx,self.HealthPower.rect.centery))
            elif self.powerup == "b":
                self.DamagePower = DamagePowerUp.DamagePowerUp(240,270,pathname("assets/HealthPowerUp.png"))
                self.screen.blit(self.DamagePower.image,(self.DamagePower.rect.centerx,self.DamagePower.rect.centery))
            pygame.display.flip()
            pygame.display.update() 
                    
            self.printJSON("PLAYER 1: ",30,80,30,0,0,255)
            self.printJSON(str(self.player1.getHealth()),30,110,30,0,0,255)

            self.printJSON("PLAYER 2: ",340,80,30,255,0,0)
            self.printJSON(str(self.player2.getHealth()),340,110,30,255,0,0)
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
                        pygame.display.update()
                    elif(event.key == pygame.K_UP):
                        self.player2.jump()
                    elif(event.key == pygame.K_LEFT):
                        self.player2.moveLeft()
                    elif(event.key == pygame.K_RIGHT):
                        self.player2.moveRight()
                    elif(event.key == pygame.K_e):
                        self.player1Arrow.update()
                    elif(event.key == pygame.K_m):
                        self.player2Arrow.update()

            if self.player2.rect.centerx < self.player1.rect.centerx:
                if 640-self.player2.rect.centerx > 150 and self.player1.rect.centerx > 150:
                    self.player2.rect.centerx += 150
                    self.player1.rect.centerx -= 150
                elif 640-self.player2.rect.centerx > 150 and self.player1.rect.centerx < 150:
                    self.player2.rect.centerx += 150
                elif 640-self.player2.rect.centerx < 150 and self.player1.rect.centerx > 150:
                    self.player1.rect.centerx -= 150
            self.player1.update()
            self.player2.update()
            pygame.display.update()

                 

            #check for collisions

            #if player = arrow(part of group)(use sprite collide, group kill):
                
            ''' arrowgroup = pygame.sprite.group.add
            arrowgroup.add(arrowobject)
            checking for collisions, call pygame.sprite.spritecollide(player,arrowgroup,True<means the arrow is killed>)
            iterate through the list for block_hit_list = collide for block in list: health -=1
            for player collisions pygame.sprite.collide_rect()
            '''

        #data permanance feature
            timeRunning = pygame.time.get_ticks()/1000
            f = open("highscore.json", "r")
            highscoreDict = json.load(f)
            scoreList = list(highscoreDict.values())
            for i in range(len(scoreList)):
                if timeRunning < scoreList[i]:
                    scoreList.append(timeRunning)
                    break
            scoreList.sort()
            newdict = {}
            for i in range(10):
                newdict[str(i)] = scoreList[i]
            json.dumps(newdict)
            

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