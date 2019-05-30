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
      x=10
      y=10
      while list[(y-10)//11][(x-10)//11]<4:
            if x+11<len(list)*11+10:
                  x+=11
            else:
                  x=10
                  y+=11
mapa()
BLACK   = (  0,   0,   0)
BLUE    = (  0,   0, 255)
GREEN   = (  0, 200,   0)
WHITE   = (255, 255, 255)
DARKGREEN   = (  0, 120,   0)
screen=Tk()
WIDTH=screen.winfo_screenwidth()
HEIGHT=screen.winfo_screenheight()
screen.destroy()
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode([0,0],pygame.FULLSCREEN)
pygame.display.set_caption('Test #3')
x=10
y=10
smer=False
hraZacala=False
mouse=[-100,-100]

font = pygame.font.SysFont("comicsansms", 29)
text = font.render("START", True, WHITE)
font2 = pygame.font.SysFont("comicsansms", 23)
text2 = font2.render("New Map", True, BLACK)
font3 = pygame.font.SysFont("comicsansms", 34)
text3 = font3.render("EXIT", True, WHITE)
fontnazev = pygame.font.SysFont("comicsansms", 80)
textInGame = font3.render("BACK",True,(WHITE))
nazev = fontnazev.render("Nazev této hry (logo)", True, WHITE)
try:
      grass=pygame.image.load('textury/travnik.png')
      water=pygame.image.load('textury/voda.png')
      mountine=pygame.image.load('textury/hora.png')
      tree=pygame.image.load('textury/les.png')
except:
      grass=pygame.image.load('generování map/textury/travnik.png')
      water=pygame.image.load('generování map/textury/voda.png')
      mountine=pygame.image.load('generování map/textury/hora.png')
      tree=pygame.image.load('generování map/textury/les.png')
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
            if event.type == MOUSEBUTTONDOWN:
                  if mouse[0] > 150 and mouse[0] < 250 and mouse[1] > 450 and mouse[1] < 500 and hraZacala==False:
                        zacatekHry()
                  if mouse[0] > 300 and mouse[0] < 400 and mouse[1] > 450 and mouse[1] < 500 and hraZacala==False:
                        generateList(GrafickeRozhrani=0)
                        mapa()
                  if mouse[0] > 450 and mouse[0] < 550 and mouse[1] > 450 and mouse[1] < 500 and hraZacala==False:
                        pygame.quit()
                        sys.exit()
                  if mouse[0] > 750 and mouse[0] < 850 and mouse[1] > 10 and mouse[1] < 60 and hraZacala==True:
                        konecHry()
      if hraZacala==True:
            if smer == 1:
                  if y+11>=len(list)*11+10:
                        if list[0][(x-10)//11]>3:
                              y=10
                  else:
                        if list[(y+1)//11][(x-10)//11]>3:
                              y+=11
                  smer=False
                  # Pohyb směrem Dolů


            if smer == 2:
                  if y-11<=0:
                        if list[len(list)-1][(x-10)//11]>3:
                              y=len(list)*11-1
                  else:
                        if list[(y-21)//11][(x-10)//11]>3:
                              y-=11
                  smer=False
                  # Pohyb směrem Nahoru


            if smer == 3:
                  if x-11<=0:
                        if list[(y-10)//11][len(list)-1]>3:
                              x=len(list)*11-1
                  else:
                        if list[(y-10)//11][(x-21)//11]>3:
                              x-=11
                  smer=False
                  # Pohyb směrem Vleva


            if smer == 4:       
                  if x+11>=len(list)*11+10:
                        if list[(y-10)//11][0]>3:
                              x=10
                  else:
                        if list[(y-10)//11][(x+1)//11]>3:
                              x+=11
                  smer=False
                  # Pohyb směrem Vpravo


            display.fill(BLACK)
            for i in range(len(list)):
                  for j in range(len(list[i])):
                        if list[i][j]<4:
                              display.blit(water,(j*11+10,i*11+10,10,10))
                        elif list[i][j]<12: 
                              display.blit(grass,(j*11+10,i*11+10,10,10))
                        elif list[i][j]<16:
                              display.blit(tree,(j*11+10,i*11+10,10,10))
                        else:
                              display.blit(mountine,(j*11+10,i*11+10,10,10))
            pygame.draw.rect(display,BLACK,(x+2,y+2,6,6))
            mouse=pygame.mouse.get_pos()
            if mouse[0] > 750 and mouse[0] < 850 and mouse[1] > 10 and mouse[1] < 60:
                  pygame.draw.rect(display, (0, 255, 0),(750,10,100,50))
            else:
                  pygame.draw.rect(display, (0, 150, 0),(750,10,100,50))
            display.blit(textInGame,(755,10))
      else:
            mouse=pygame.mouse.get_pos()
            if mouse[0] > 150 and mouse[0] < 250 and mouse[1] > 450 and mouse[1] < 500:
                  pygame.draw.rect(display, (0, 255, 0),(150,450,100,50))
            else:
                  pygame.draw.rect(display, (0, 150, 0),(150,450,100,50))
            if mouse[0] > 300 and mouse[0] < 400 and mouse[1] > 450 and mouse[1] < 500:
                  pygame.draw.rect(display, (255, 255, 255),(300,450,100,50))
            else:
                  pygame.draw.rect(display, (100, 150, 100),(300,450,100,50))
            if mouse[0] > 450 and mouse[0] < 550 and mouse[1] > 450 and mouse[1] < 500:
                  pygame.draw.rect(display, (255, 0, 0),(450,450,100,50))
            else:
                  pygame.draw.rect(display, (150, 0, 0),(450,450,100,50))
            display.blit(nazev, (150, 200))
            display.blit(text, (150, 454))
            display.blit(text2, (300, 457))
            display.blit(text3, (455, 450))
      pygame.display.update()
      clock.tick(100)
