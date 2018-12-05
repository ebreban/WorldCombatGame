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
        self.highscore=False
        

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
                        self.player1 = HighHealthFighter.HighHealthFighter("player 1",30,360,"left",pathname("assets/healthwarrior.png"))
                        self.player1Arrow = Arrow.Arrow(50,387,"left",pathname("assets/arrow.png"))
                        self.player2 = HighDamageFighter.HighDamageFighter("player 2",400,360,"right",pathname("assets/damagewarrior.png"))
                        self.player2Arrow = Arrow.Arrow(390,387,"right",pathname("assets/arrow.png"))
                        self.player2Arrow.speed = -10
                        
                    elif 128+371 > mouse[0] > 128 and 294+82 > mouse[1] > 294:
                    
                        self.state = "GAME"
                        self.player2 = HighHealthFighter.HighHealthFighter("player 2",400,360,"right",pathname("assets/healthwarrior.png"))
                        self.player2Arrow = Arrow.Arrow(390,387,"right",pathname("assets/arrow.png"))
                        self.player1 = HighDamageFighter.HighDamageFighter("player 1",30,360,"left",pathname("assets/damagewarrior.png"))
                        self.player1Arrow = Arrow.Arrow(50,387,"left",pathname("assets/arrow.png"))
                        self.player2Arrow.speed = -10
                        
           
            pygame.display.update()             
    def inScreen(self, player):
        if player.rect.centerx < 11 or player.rect.centerx > 639:
            return False
        elif player.rect.centery < 11 or player.rect.centery > 469:
            return False
        else:
            return True

    def displayHealth(self):
        self.printJSON("PLAYER 1: ",39,80,22,0,0,255)
        self.printJSON(str(self.player1.getHealth()),169,80,22,0,0,255)
        self.printJSON("Damage Power: ",39,100,22,0,0,255)
        self.printJSON(str(self.player1.getDamage()),199,100,22,0,0,255)
        self.printJSON("PLAYER 2: ",349,80,22,255,0,0)
        self.printJSON(str(self.player2.getHealth()),499,80,22,255,0,0)
        self.printJSON("Damage Power: ",349,100,22,255,0,0)
        self.printJSON(str(self.player2.getDamage()),509,100,22,255,0,0)
    def gameLoop(self):
        pygame.key.set_repeat(10,10)
        timeRunning = pygame.time.get_ticks()
        powerupGroup = pygame.sprite.Group()

        arrow1group = pygame.sprite.Group()
        arrow2group = pygame.sprite.Group()

        arrow1group.add(self.player1Arrow)
        arrow2group.add(self.player2Arrow)

        spawn_time = timeRunning
        while self.state == "GAME":
            self.powerup = random.choice(["a","b"])
            self.GameScreen()
            self.players = pygame.sprite.Group(self.player1,self.player2)
            

            if (pygame.time.get_ticks()-spawn_time)/1000 > 15:
                if self.powerup == "b":
                   powerupGroup.add(HealthPowerUp.HealthPowerUp(290,270,pathname("assets/HealthPowerUp.png")))
                elif self.powerup == "a":
                    powerupGroup.add(DamagePowerUp.DamagePowerUp(290,270,pathname("assets/DamagePowerUp.png")))
                spawn_time = pygame.time.get_ticks()
            self.displayHealth()      
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_w):
                        self.player1.jump()
                    elif(event.key == pygame.K_a):   
                        self.player1.moveLeft()    
                    elif(event.key == pygame.K_d):
                        self.player1.moveRight()                  
                    if(event.key == pygame.K_UP):
                        self.player2.jump()
                    elif(event.key == pygame.K_LEFT):
                        self.player2.moveLeft()
                        
                    elif(event.key == pygame.K_RIGHT):
                        self.player2.moveRight()
                        
                    elif(event.key == pygame.K_e):
                        self.player1Arrow.fired =True
                        
                    elif(event.key == pygame.K_m):
                        self.player2Arrow.fired =True



            if self.player2Arrow.fired == False:
                self.player2Arrow.setPos(self.player2.rect.centerx,self.player2.rect.centery+20)
            if self.player1Arrow.fired == False:
                self.player1Arrow.setPos(self.player1.rect.centerx,self.player1.rect.centery+20)
            if self.player2Arrow.rect.centerx < 0 or self.player2Arrow.rect.centerx > 640: 
                self.player2Arrow.setPos(self.player2.rect.centerx+20,self.player2.rect.centery+20)
                self.player2Arrow.fired = False
            if self.player1Arrow.rect.centerx < 0 or self.player1Arrow.rect.centerx > 640: 
                self.player1Arrow.setPos(self.player1.rect.centerx+20,self.player1.rect.centery+20)
                self.player1Arrow.fired = False

            if (self.player2.rect.centerx-19)  < self.player1.rect.centerx + 25:
                if 640-self.player2.rect.centerx > 150 and self.player1.rect.centerx > 150:
                    self.player2.rect.centerx += 150
                    self.player1.rect.centerx -= 150
                elif 640-self.player2.rect.centerx > 150 and self.player1.rect.centerx < 150:
                    self.player2.rect.centerx += 150
                elif 640-self.player2.rect.centerx < 150 and self.player1.rect.centerx > 150:
                    self.player1.rect.centerx -= 150
                else:
                    self.player1.rect.centerx -= 10
            
            if pygame.sprite.collide_rect(self.player1,self.player2):
                print("Collision!!!")

            #collisions
            for player in [self.player2,self.player1]:
                powerlist = pygame.sprite.spritecollide(player,powerupGroup,True)
                for i in powerlist:
                    print(player.health)
                    print(player.damage)
                    i.applyUpgrade(player)
                    print(player.health)
                    print(player.damage)
            self.displayHealth()      
            arrow1_hit_list = pygame.sprite.spritecollide(self.player2,arrow1group, False)
            arrow2_hit_list = pygame.sprite.spritecollide(self.player1,arrow2group, False)

            if(arrow1_hit_list != []):
                for i in arrow1_hit_list:
                    i.setPos(self.player1.rect.centerx+20,self.player1.rect.centery+20)
                    i.fired = False
                    self.player2.health-=self.player1.damage         

            if(arrow2_hit_list != []):
                for i in arrow2_hit_list:
                    i.setPos(self.player2.rect.centerx+20,self.player2.rect.centery+20)
                    i.fired = False
                    self.player1.health-=self.player2.damage 

            if self.player1.health <= 0:
                self.player1.kill()
                self.update_scores(pygame.time.get_ticks()-timeRunning)
                self.state="GAMEOVER"

            if self.player2.health <= 0:
                self.player2.kill()
                self.update_scores(pygame.time.get_ticks()-timeRunning)
                self.state="GAMEOVER"


            self.players.update()
            self.player2Arrow.update()
            self.player1Arrow.update()
            self.players.draw(self.screen)
            arrow1group.draw(self.screen)
            arrow2group.draw(self.screen)
            powerupGroup.draw(self.screen)
            pygame.display.flip()

                 


        #data permanance feature
    def update_scores(self,timeRunning):
        timeRunning /= 1000
        f = open("highscore.json", "r")
        highscoreDict = json.load(f)
        f.close()
        scoreList = list(highscoreDict.values())
        print("now printing list")
        print(scoreList)
        scoreList.append(timeRunning)
        scoreList.sort()
        print(scoreList)
        newdict = {}
        for i in range(10):
            newdict[str(i+1)] = scoreList[i]
        f = open("highscore.json", "w")
        json.dump(newdict,f)
        f.close()
        if timeRunning in list(newdict.values()):
            self.highscore=True
            


    def gameOver(self):
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (255,255,255))
        self.screen.blit(message, (self.width/2,self.height/2))
        if self.highscore:
            scoreMessage = myfont.render("Top 10 score has been set!!!", False, (255,255,255))
            self.screen.blit(scoreMessage,(300,300))

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()