from mapGenerator import *
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
zadavani=False
zad=""
# ---------- Třídy ----------
class Hrac:
      def __init__(self,jmeno):
            self.jmeno=jmeno
# ---------- Funkce ---------- 
def ulozVse():
      ulozJmenaHracu(seznamJmenHracu)


def addCharacter(jmeno):
      seznamJmenHracu.append(jmeno)
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
                  if event.type == KEYDOWN:
                        if event.key == K_a: 
                              zad+="a"
                        if event.key == K_b: 
                              zad+="b"
                        if event.key == K_c: 
                              zad+="c"
                        if event.key == K_d: 
                              zad+="d"
                        if event.key == K_e: 
                              zad+="e"
                        if event.key == K_g: 
                              zad+="g"
                        if event.key == K_h: 
                              zad+="h"
                        if event.key == K_i: 
                              zad+="i"
                        if event.key == K_j: 
                              zad+="j"
                        if event.key == K_k: 
                              zad+="k"
                        if event.key == K_l: 
                              zad+="l"
                        if event.key == K_m: 
                              zad+="m"
                        if event.key == K_n: 
                              zad+="n"
                        if event.key == K_o: 
                              zad+="o"
                        if event.key == K_p: 
                              zad+="p"
                        if event.key == K_q: 
                              zad+="q"
                        if event.key == K_r: 
                              zad+="r"
                        if event.key == K_s: 
                              zad+="s"
                        if event.key == K_t: 
                              zad+="t"
                        if event.key == K_u: 
                              zad+="u"
                        if event.key == K_v: 
                              zad+="v"
                        if event.key == K_w: 
                              zad+="w"
                        if event.key == K_x: 
                              zad+="y"
                        if event.key == K_z: 
                              zad+="z"
                        if event.key == K_BACKSPACE: 
                              zad=""
                        if event.key == K_SPACE: 
                              zad+=" "
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
                              if zad!="" and zad not in seznamJmenHracu:
                                    addCharacter(zad)
                              zad=""
                        if mouse[0] > 100 and mouse[0] < 200 and mouse[1] > 110 and mouse[1] < 160 and hraZacala=="Character":
                              rasa="Human"
                        if mouse[0] > 100 and mouse[0] < 200 and mouse[1] > 170 and mouse[1] < 220 and hraZacala=="Character":
                              rasa="Elf"
                        if mouse[0] > 100 and mouse[0] < 200 and mouse[1] > 230 and mouse[1] < 280 and hraZacala=="Character":
                              rasa="Dwarf"
                        if mouse[0] > 210 and mouse[0] < 310 and mouse[1] > 110 and mouse[1] < 160 and hraZacala=="Character":
                              typ="Warior"
                        if mouse[0] > 210 and mouse[0] < 310 and mouse[1] > 170 and mouse[1] < 220 and hraZacala=="Character":
                              typ="Ranger"
                        if mouse[0] > 210 and mouse[0] < 310 and mouse[1] > 230 and mouse[1] < 280 and hraZacala=="Character":
                              typ="Wizzard"
                        if mouse[0] > 450 and mouse[0] < 550 and mouse[1] > 450 and mouse[1] < 500 and hraZacala==False:
                              character()
                        if mouse[0] > 400 and mouse[0] < 800 and mouse[1] > 110 and mouse[1] < 160 and hraZacala=="Character":
                              zadavani=True
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
            if typ=="Warior":
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
            display.blit(fontChar.render("Human",  True, WHITE), (110, 118))
            display.blit(fontChar.render("Elf",    True, WHITE), (130, 178))
            display.blit(fontChar.render("Dwarf",  True, WHITE), (115, 238))
            display.blit(fontChar.render("Warrior",True, WHITE), (215, 118))
            display.blit(fontChar.render("Ranger", True, WHITE), (220, 178))
            display.blit(fontChar.render("Wizzard",True, WHITE), (213, 238))
      pygame.display.update()
      clock.tick(FPS)