# -*- coding: utf-8 -*-
from mapGenerator import *
# ---------- Třídy ----------
class Hrac:
      def __init__(self,jmeno,rasa,typ,level,zivoty,zivoty2,mana,mana2,hlaska):
            self.jmeno=jmeno
            self.rasa=rasa
            self.typ=typ
            self.level=level
            if level==0:
                  self.level=1
                  if typ=="Wizzard":
                        self.zivoty=[20,20] 
                        self.mana=[80,80]
                  elif typ=="Ranger":      
                        self.zivoty=[80,80]
                        self.mana=[20,20]
                  elif typ=="Warrior":
                        self.zivoty=[100,100] 
                        self.mana=[0,0]
            else:
                  self.zivoty=[zivoty,zivoty2] 
                  self.mana=[mana,mana2]
            self.hlaska=hlaska 
            self.save()
      def save(self):
            ulozHrace(self.jmeno,self.rasa,self.typ,self.level,self.zivoty,self.mana,self.hlaska)
      def __str__(self):
            return self.jmeno + "\n" + self.rasa + "\n" + self.typ + "\n" + str(self.level) + "\n" + self.hlaska 
# ---------- proměné ----------
FPS=100
rasa=""
typ=""
x=10
y=10
smer=False
hraZacala=False
BLACK       = (  0,   0,   0)
BLUE        = (  0,   0, 255)
GREEN       = (  0, 200,   0)
WHITE       = (255, 255, 255)
DARKGREEN   = (  0, 120,   0)
seznamJmenHracu=nactiJmenaHrace()
seznamHracu=[]
for i in seznamJmenHracu:
      seznamHracu.append(Hrac(i,nactiHrace(i)[0],nactiHrace(i)[1],nactiHrace(i)[2],nactiHrace(i)[3],nactiHrace(i)[4],nactiHrace(i)[5],nactiHrace(i)[6],nactiHrace(i)[7]))
zadavani=False
zad=""
var=""
nextChar="m"
cisloHrace=0
# ---------- Funkce ---------- 
def ulozVse():
      ulozJmenaHracu(seznamJmenHracu)


def addCharacter(jmeno,rasa,typ):
      seznamJmenHracu.append(jmeno)
      seznamHracu.append(Hrac(jmeno,rasa,typ,0,0,0,0,0,""))


def character():
      global hraZacala
      hraZacala="Character"


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
      global x
      global y
      x=10
      y=10
      while list[(y-10)//11][(x-10)//11]<4:
            if x+11<len(list)*11+10:
                  x+=11
            else:
                  x=10
                  y+=11

def posledni(prom):
      a=len(prom)
      prom2=""
      for i in range(a-1):
            prom2+=prom[i]
      return prom2


def hracVypis(cisloHrace):
      global seznamHracu
      global display
      a=seznamHracu[cisloHrace]
      z=""
      ret=[]
      for i in a.__str__():
            if i=="\n":
                  ret.append(z)
                  z=""
            else:
                  z+=i
      ret.append(z)
      return ret
# ---------- Zadání funkcí a vytvoření okny pygame ----------
mapa()

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode([0,0],pygame.FULLSCREEN)
pygame.display.set_caption('Test #3')

# ---------- načtení fontů a textůr ----------
font = pygame.font.SysFont("comicsansms", 29)
text = font.render("START", True, WHITE)
font2 = pygame.font.SysFont("comicsansms", 23)
text2 = font2.render("New Map", True, BLACK)
font3 = pygame.font.SysFont("comicsansms", 34)
text3 = font3.render("EXIT", True, WHITE)
font4 = pygame.font.SysFont("comicsansms", 20)
text4 = font4.render("New", True, WHITE)
text5 = font4.render("Character", True, WHITE)
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
# ---------- Hlavní herní smička ----------
while True:     
      display.fill(BLACK)
      mouse=pygame.mouse.get_pos()
      for event in pygame.event.get():
            if event.type == QUIT:
                  ulozVse()
                  pygame.quit()
                  sys.exit()
            if zadavani==True:
                  if event.type == KEYUP:
                        if event.key == K_RSHIFT or event.key == K_LSHIFT:
                              nextChar="m"
                  if event.type == KEYDOWN:
                        if event.key == K_RSHIFT or event.key == K_LSHIFT:
                              nextChar="V"
                        if event.key == K_a: 
                              if nextChar=="V":
                                    zad+="A"
                              else:
                                    zad+="a"
                        if event.key == K_b: 
                              if nextChar=="V":
                                    zad+="B"
                              else:
                                    zad+="b"
                        if event.key == K_c: 
                              if nextChar=="V":
                                    zad+="C"
                              else:
                                    zad+="c"
                        if event.key == K_d: 
                              if nextChar=="V":
                                    zad+="D"
                              else:
                                    zad+="d"
                        if event.key == K_e: 
                              if nextChar=="V":
                                    zad+="E"
                              else:
                                    zad+="e"
                        if event.key == K_g: 
                              if nextChar=="V":
                                    zad+="G"
                              else:
                                    zad+="g"
                        if event.key == K_h: 
                              if nextChar=="V":
                                    zad+="H"
                              else:
                                    zad+="h"
                        if event.key == K_i: 
                              if nextChar=="V":
                                    zad+="I"
                              else:
                                    zad+="i"
                        if event.key == K_j: 
                              if nextChar=="V":
                                    zad+="J"
                              else:
                                    zad+="j"
                        if event.key == K_k: 
                              if nextChar=="V":
                                    zad+="K"
                              else:
                                    zad+="k"
                        if event.key == K_l: 
                              if nextChar=="V":
                                    zad+="L"
                              else:
                                    zad+="l"
                        if event.key == K_m: 
                              if nextChar=="V":
                                    zad+="M"
                              else:
                                    zad+="m"
                        if event.key == K_n: 
                              if nextChar=="V":
                                    zad+="N"
                              else:
                                    zad+="n"
                        if event.key == K_o: 
                              if nextChar=="V":
                                    zad+="O"
                              else:
                                    zad+="o"
                        if event.key == K_p: 
                              if nextChar=="V":
                                    zad+="P"
                              else:
                                    zad+="p"
                        if event.key == K_q: 
                              if nextChar=="V":
                                    zad+="Q"
                              else:
                                    zad+="q"
                        if event.key == K_r: 
                              if nextChar=="V":
                                    zad+="R"
                              else:
                                    zad+="r"
                        if event.key == K_s: 
                              if nextChar=="V":
                                    zad+="S"
                              else:
                                    zad+="s"
                        if event.key == K_t: 
                              if nextChar=="V":
                                    zad+="T"
                              else:
                                    zad+="t"
                        if event.key == K_u: 
                              if nextChar=="V":
                                    zad+="U"
                              else:
                                    zad+="u"
                        if event.key == K_v: 
                              if nextChar=="V":
                                    zad+="V"
                              else:
                                    zad+="v"
                        if event.key == K_w: 
                              if nextChar=="V":
                                    zad+="W"
                              else:
                                    zad+="w"
                        if event.key == K_x: 
                              if nextChar=="V":
                                    zad+="X"
                              else:
                                    zad+="x"
                        if event.key == K_y: 
                              if nextChar=="V":
                                    zad+="Z"
                              else:
                                    zad+="z"
                        if event.key == K_z: 
                              if nextChar=="V":
                                    zad+="Y"
                              else:
                                    zad+="y"
                        if event.key == K_f: 
                              if nextChar=="V":
                                    zad+="F"
                              else:
                                    zad+="f"
                        if event.key == K_BACKSPACE: 
                              zad=posledni(zad)
                        if event.key == K_SPACE: 
                              zad+=" "
                        if event.key == K_1:
                              if nextChar=="V":
                                    zad+="1"
                              else:
                                    zad+="1"
                        if event.key == K_2:
                              if nextChar=="V":
                                    zad+="2"
                              else:
                                    zad+="2"
                        if event.key == K_3:
                              if nextChar=="V":
                                    zad+="3"
                              else:
                                    zad+="3"
                        if event.key == K_4:
                              if nextChar=="V":
                                    zad+="4"
                              else:
                                    zad+="4"
                        if event.key == K_5:
                              if nextChar=="V":
                                    zad+="5"
                              else:
                                    zad+="5"
                        if event.key == K_6:
                              if nextChar=="V":
                                    zad+="6"
                              else:
                                    zad+="6"
                        if event.key == K_7:
                              if nextChar=="V":
                                    zad+="7"
                              else:
                                    zad+="7"
                        if event.key == K_8:
                              if nextChar=="V":
                                    zad+="8"
                              else:
                                    zad+="8"
                        if event.key == K_9:
                              if nextChar=="V":
                                    zad+="9"
                              else:
                                    zad+="9"
                        if event.key == K_0:
                              if nextChar=="V":
                                    zad+="0"
                              else:
                                    zad+="0"
                  if event.type == MOUSEBUTTONDOWN:
                        zadavani=False
            else:
                  if event.type == KEYDOWN and zadavani==False:
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
                                    ulozVse()
                                    pygame.quit()
                                    sys.exit()
                  if event.type == MOUSEBUTTONDOWN:
                        if mouse[0] > 150 and mouse[0] < 250 and mouse[1] > 450 and mouse[1] < 500 and hraZacala==False:
                              zacatekHry()
                        if mouse[0] > 300 and mouse[0] < 400 and mouse[1] > 450 and mouse[1] < 500 and hraZacala==False:
                              generateList(GrafickeRozhrani=0)
                              mapa()
                        if mouse[0] > 300 and mouse[0] < 400 and mouse[1] > 450 and mouse[1] < 500 and hraZacala=="Character":
                              konecHry()
                        if mouse[0] > 600 and mouse[0] < 700 and mouse[1] > 450 and mouse[1] < 500 and (hraZacala==False or hraZacala=="Character"):     
                              ulozVse()
                              pygame.quit()
                              sys.exit()
                        if mouse[0] > 750 and mouse[0] < 850 and mouse[1] >  10 and mouse[1] <  60 and hraZacala==True:
                              konecHry()
                        if mouse[0] > 150 and mouse[0] < 250 and mouse[1] > 450 and mouse[1] < 500 and hraZacala=="Character":
                              if zad in seznamJmenHracu:
                                    zad=""
                                    var="Zadané jméno již existuje"
                              elif len(zad)<3:
                                    var="Zadané jméno je příliš krátké"
                              elif len(zad)>20:
                                    var="Zadané jméno je příliš dlouhé"
                              elif rasa not in ['Human','Elf','Dwarf']:
                                    var="Nezadal jsi rasu postavy"
                              elif typ not in ['Warrior','Ranger','Wizzard']:
                                    var="Nezadal jsi classu postavy"
                              else:
                                    addCharacter(zad,rasa,typ)
                                    konecHry()
                                    var=""
                                    rasa=""
                                    typ=""
                        if mouse[0] > 100 and mouse[0] < 200 and mouse[1] > 110 and mouse[1] < 160 and hraZacala=="Character":
                              rasa="Human"
                        if mouse[0] > 100 and mouse[0] < 200 and mouse[1] > 170 and mouse[1] < 220 and hraZacala=="Character":
                              rasa="Elf"
                        if mouse[0] > 100 and mouse[0] < 200 and mouse[1] > 230 and mouse[1] < 280 and hraZacala=="Character":
                              rasa="Dwarf"
                        if mouse[0] > 210 and mouse[0] < 310 and mouse[1] > 110 and mouse[1] < 160 and hraZacala=="Character":
                              typ="Warrior"
                        if mouse[0] > 210 and mouse[0] < 310 and mouse[1] > 170 and mouse[1] < 220 and hraZacala=="Character":
                              typ="Ranger"
                        if mouse[0] > 210 and mouse[0] < 310 and mouse[1] > 230 and mouse[1] < 280 and hraZacala=="Character":
                              typ="Wizzard"
                        if mouse[0] > 450 and mouse[0] < 550 and mouse[1] > 450 and mouse[1] < 500 and hraZacala==False:
                              character()
                        if mouse[0] > 400 and mouse[0] < 800 and mouse[1] > 110 and mouse[1] < 160 and hraZacala=="Character":
                              zadavani=True
                        if mouse[0] > 900 and mouse[0] < 1100 and mouse[1] > 10 and mouse[1] <  60 and hraZacala==True:
                              if cisloHrace+1!=len(seznamHracu):
                                    cisloHrace+=1
                              else:
                                    cisloHrace=0
      if hraZacala==True:
            seznam=hracVypis(cisloHrace)
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
            if mouse[0] > 900 and mouse[0] < 1100 and mouse[1] > 10 and mouse[1] < 60:
                  pygame.draw.rect(display, (0, 255, 0),(900,10,200,50))
            else:
                  pygame.draw.rect(display, (0, 150, 0),(900,10,200,50))
            display.blit(font3.render("Next Player",True,WHITE),(905,10))
            poz=0
            for i in seznam:
                  display.blit(font3.render(i,True,WHITE),(755,70+poz))
                  poz+=50
      elif hraZacala==False:
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
            if mouse[0] > 600 and mouse[0] < 700 and mouse[1] > 450 and mouse[1] < 500:
                  pygame.draw.rect(display, (100, 100, 100),(600,450,100,50))
            else:
                  pygame.draw.rect(display, (50, 50, 50),(600,450,100,50))
            display.blit(nazev, (150, 200))
            display.blit(text, (150, 454))
            display.blit(text2, (300, 457))
            display.blit(text4, (477, 450))
            display.blit(text5, (453, 470))
            display.blit(text3, (605, 450))
      elif hraZacala=="Character":
            if mouse[0] > 600 and mouse[0] < 700 and mouse[1] > 450 and mouse[1] < 500:
                  pygame.draw.rect(display, ( 100, 100, 100),( 600, 450, 100,  50))
            else:
                  pygame.draw.rect(display, (  50,  50,  50),( 600, 450, 100,  50))
            if mouse[0] > 300 and mouse[0] < 400 and mouse[1] > 450 and mouse[1] < 500:
                  pygame.draw.rect(display, ( 100, 100, 100),( 300, 450, 100,  50))
            else:
                  pygame.draw.rect(display, (  50,  50,  50),( 300, 450, 100,  50))
            if mouse[0] > 150 and mouse[0] < 250 and mouse[1] > 450 and mouse[1] < 500:
                  pygame.draw.rect(display, ( 100, 100, 100),( 150, 450, 100,  50))
            else:
                  pygame.draw.rect(display, (  50,  50,  50),( 150, 450, 100,  50))

      
            if rasa=="Human":
                  pygame.draw.rect(display, (100, 100, 100),(100, 110, 100, 50))
            else:
                  pygame.draw.rect(display, ( 50,  50,  50),(100, 110, 100, 50))
            if rasa=="Elf":
                  pygame.draw.rect(display, (100, 100, 100),(100, 170, 100, 50))
            else:
                  pygame.draw.rect(display, ( 50,  50,  50),(100, 170, 100, 50))
            if rasa=="Dwarf":
                  pygame.draw.rect(display, (100, 100, 100),(100, 230, 100, 50))
            else:
                  pygame.draw.rect(display, ( 50,  50,  50),(100, 230, 100, 50))
            if typ=="Warrior":
                  pygame.draw.rect(display, (100, 100, 100),(210, 110, 100, 50))
            else:
                  pygame.draw.rect(display, ( 50,  50,  50),(210, 110, 100, 50))
            if typ=="Ranger":
                  pygame.draw.rect(display, (100, 100, 100),(210, 170, 100, 50))
            else:
                  pygame.draw.rect(display, ( 50,  50,  50),(210, 170, 100, 50))
            if typ=="Wizzard":
                  pygame.draw.rect(display, (100, 100, 100),(210, 230, 100, 50))
            else:
                  pygame.draw.rect(display, ( 50,  50,  50),(210, 230, 100, 50))
            if zadavani==True:
                  pygame.draw.rect(display, (100, 100, 100),(400, 110, 400, 50))
            else:
                  pygame.draw.rect(display, ( 50,  50,  50),(400, 110, 400, 50))
            display.blit(font3.render("Add",True,WHITE), (165, 450))
            display.blit(textInGame                    , (305, 450))
            display.blit(text3                         , (605, 450))


            fontChar=pygame.font.SysFont("comicsansms", 23)
            display.blit(fontChar.render(zad,  True, WHITE), (400, 118))        
            display.blit(fontChar.render(var,  True, WHITE), (400, 168))
            display.blit(fontChar.render("Human",  True, WHITE), (110, 118))
            display.blit(fontChar.render("Elf",    True, WHITE), (130, 178))
            display.blit(fontChar.render("Dwarf",  True, WHITE), (115, 238))
            display.blit(fontChar.render("Warrior",True, WHITE), (215, 118))
            display.blit(fontChar.render("Ranger", True, WHITE), (220, 178))
            display.blit(fontChar.render("Wizzard",True, WHITE), (213, 238))
      pygame.display.update()
      clock.tick(FPS)