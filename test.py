from mapGenerator import *
import pygame, sys
from pygame.locals import *
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
      print("")

BLACK   = (  0,   0,   0)
BLUE    = (  0,   0, 255)
GREEN   = (  0, 255,   0)
WHITE   = (255, 255, 255)
BROWN   = (150,  50,  50)
WIDTH   = 20+len(list)*11
HEIGHT  = 20+len(list)*11
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Generátor mapy')
display.fill(BLACK)
x=10
y=10
smer=False
while True:
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
                        if event.key == K_ESCAPE:
                              pygame.quit()
                              sys.exit()
      if x<=0:
            x=len(list)*11-1
      if y<=0:
            y=len(list)*11-1
      if x>=len(list)*11+10:
            x=10
      if y>=len(list)*11+10:
            y=10
      if smer == 1:
            y+=11
            smer=False
      if smer == 2:
            y-=11
            smer=False
      if smer == 3:
            x-=11
            smer=False
      if smer == 4:
            x+=11
            smer=False
      display.fill(BLACK)
      for i in range(len(list)):
            for j in range(len(list[i])):
                  if list[i][j]<4:
                        pygame.draw.rect(display,BLUE,(j*11+10,i*11+10,10,10))
                  elif list[i][j]<12:
                        pygame.draw.rect(display,GREEN,(j*11+10,i*11+10,10,10))
                  elif list[i][j]<16:
                        pygame.draw.rect(display,BROWN,(j*11+10,i*11+10,10,10))
                  else:
                        pygame.draw.rect(display,WHITE,(j*11+10,i*11+10,10,10))
      pygame.draw.rect(display,BLACK,(x+2,y+2,6,6))
      pygame.display.update()
      clock.tick(15)
