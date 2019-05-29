from mapGenerator import *
import pygame, sys
from pygame.locals import *
from seznamGenerator import *
from tkinter import *
def zacatekHry():
      global hraZacala
      hraZacala=True
def konecHry():
      global hraZacala
      hraZacala=False
def mapa():
      global list
      try:
            load=open('seznam.txt','r',encoding='utf8')
            load=load.read()
      except:
            load=open('generování map/seznam.txt','r',encoding='utf8')
            load=load.read()
      a=""
      list=[]
      list2=[]
      for i in load:
            if i==" ":
                  list2.append(int(a))
                  a=""
            elif i=="\n":
                  list.append(list2)
                  list2=[]
            else:
                  a+=i
      generate(list)
      for i in list:
            for j in i:
                  print(j,end=" ")
            print(" ")
mapa()
BLACK   = (  0,   0,   0)
BLUE    = (  0,   0, 255)
GREEN   = (  0, 200,   0)
WHITE   = (255, 255, 255)
DARKGREEN   = (  0, 100,   0)
screen=Tk()
WIDTH=screen.winfo_screenwidth()
HEIGHT=screen.winfo_screenheight()
screen.destroy()
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Generátor mapy')
x=10
y=10
smer=False
hraZacala=False
mouse=[-100,-100]

font = pygame.font.SysFont("comicsansms", 29)
text = font.render("START", True, WHITE)
font2 = pygame.font.SysFont("comicsansms", 23)
text2 = font2.render("New Map", True, BLACK)

while True:     
      display.fill(BLACK)
      for event in pygame.event.get():
            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()
            if event.type == KEYDOWN:
                        if event.key == K_DOWN:
                              smer=1
                        if event.key == K_UP:
                              smer=2
                        if event.key == K_LEFT:
                              smer=3
                        if event.key == K_RIGHT:
                              smer=4
                        if event.key == K_s:
                              smer=1
                        if event.key == K_w:
                              smer=2
                        if event.key == K_a:
                              smer=3
                        if event.key == K_d:
                              smer=4
                        if event.key == K_e:
                              konecHry()
                        if event.key == K_ESCAPE:
                              pygame.quit()
                              sys.exit()
            if event.type == KEYUP:
                        if event.key == K_s:
                              smer=False
                        if event.key == K_w:
                              smer=False
                        if event.key == K_a:
                              smer=False
                        if event.key == K_d:
                              smer=False
                        if event.key == K_DOWN:
                              smer=False
                        if event.key == K_UP:
                              smer=False
                        if event.key == K_LEFT:
                              smer=False
                        if event.key == K_RIGHT:
                              smer=False
            if event.type == MOUSEBUTTONDOWN:
                  if mouse[0] > 150 and mouse[0] < 250 and mouse[1] > 450 and mouse[1] < 500:
                        zacatekHry()
                  if mouse[0] > 350 and mouse[0] < 450 and mouse[1] > 450 and mouse[1] < 500:
                        generateList(GrafickeRozhrani=0)
                        mapa()
                        x=10
                        y=10
      if hraZacala==True:
            if smer == 1:
                  if y+11>=len(list)*11+10:
                        y=10
                  else:
                        y+=11
            if smer == 2:
                  if y-11<=0:
                        y=len(list)*11-1
                  else:
                        y-=11
            if smer == 3:
                  if x-11<=0:
                        x=len(list)*11-1
                  else:
                        x-=11
            if smer == 4:       
                  if x+11>=len(list)*11+10:
                        x=10
                  else:
                        x+=11
            display.fill(BLACK)
            for i in range(len(list)):
                  for j in range(len(list[i])):
                        if list[i][j]<4:
                              pygame.draw.rect(display,BLUE,(j*11+10,i*11+10,10,10))
                        elif list[i][j]<12:
                              pygame.draw.rect(display,GREEN,(j*11+10,i*11+10,10,10))
                        elif list[i][j]<16:
                              pygame.draw.rect(display,DARKGREEN,(j*11+10,i*11+10,10,10))
                        else:
                              pygame.draw.rect(display,(100, 100, 100),(j*11+10,i*11+10,10,10))
            pygame.draw.rect(display,BLACK,(x+2,y+2,6,6))
      else:
            mouse=pygame.mouse.get_pos()
            if mouse[0] > 150 and mouse[0] < 250 and mouse[1] > 450 and mouse[1] < 500:
                  pygame.draw.rect(display, (0, 255, 0),(150,450,100,50))
            else:
                  pygame.draw.rect(display, (0, 150, 0),(150,450,100,50))
            if mouse[0] > 350 and mouse[0] < 450 and mouse[1] > 450 and mouse[1] < 500:
                  pygame.draw.rect(display, (255, 255, 255),(350,450,100,50))
            else:
                  pygame.draw.rect(display, (100, 150, 100),(350,450,100,50))
            display.blit(text, (150, 454))
            display.blit(text2, (350, 457))
      pygame.display.update()
      clock.tick(10)
