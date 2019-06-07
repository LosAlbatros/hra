# -*- coding: utf-8 -*
from mapGenerator import *
# ---------- Třídy ----------
class Town:
      def __init__(self,pozY,pozX):
            global jmenaMest
            self.sourednice=[pozX,pozY]
            x=randint(1,20)
            self.jmeno=jmenaMest[x]
            self.hospod=randint(0,5)
            self.mise=[]
            for i in range(self.hospod):
                  while True:
                        randomMise=randint(0,len(nazvyMisi)-1)
                        if randomMise == 6:
                              if randint(1,20)==1:
                                    break
                        elif randomMise not in self.mise:
                              break

                  self.mise.append(randomMise)
            self.itemsToSell=[]
            for i in range(randint(0,5)):
                  randomItem=randint(0,len(ItemsID.keys())-1)
                  while randomItem in self.itemsToSell:
                        randomItem=randint(0,len(ItemsID.keys())-1)
                  self.itemsToSell.append(randomItem)
      def __str__(self):
            return self.jmeno + "\n"+"For sale:\n"
      def getItems(self):
            return self.itemsToSell
      def additem(self):
            if len(self.itemsToSell)<5:
                  randomItem=randint(0,len(ItemsID.keys())-1)
                  while randomItem in self.itemsToSell:
                        randomItem=randint(0,len(ItemsID.keys())-1)
                  self.itemsToSell.append(randomItem)
      def addMission(self):
            if self.hospod<5:
                  self.hospod+=1
                  while True:
                        randomMise=randint(0,len(nazvyMisi)-1)
                        if randomMise not in self.mise:
                              break
                  self.mise.append(randomMise)
            
class NPC:
      def __init__(self,jmeno,rasa,typ,level,zivoty,zivoty2,mana,mana2,hlaska):
            self.hlaska=hlaska
            self.jmeno=jmeno
            self.rasa=rasa
            self.typ=typ
            self.level=level
            self.zivoty=[int(zivoty),int(zivoty2)]
            self.mana=[int(mana),int(mana2)]
            if level == 0:
                  level=1
                  if typ=="Wizzard":
                        self.zivoty=[0,0] 
                        self.mana=[50,50]
                  elif typ=="Ranger":      
                        self.zivoty=[30,30]
                        self.mana=[20,20]
                  elif typ=="Warrior":
                        self.zivoty=[50,50] 
                        self.mana=[0,0]
                  if rasa=="Human":
                        self.zivoty[1]+=10
                        self.zivoty[0]+=10
                        self.mana[1]+=40
                        self.mana[0]+=40
                  if rasa=="Elf":
                        self.zivoty[1]+=25
                        self.zivoty[0]+=25
                        self.mana[1]+=25
                        self.mana[0]+=25
                  if rasa=="Dwarf":
                        self.zivoty[1]+=50
                        self.zivoty[0]+=50
                        self.mana[1]+=0
                        self.mana[0]+=0
      def __str__(self):
            return str(self.jmeno) + ":" + str(self.rasa) + ":" + str(self.typ) + ":" + str(self.level) + ":" + str(self.zivoty[0]) + "/" + str(self.zivoty[1]) + ":" + str(self.mana[0]) + "/" + str(self.mana[1])

      def getToAttack(self):
            vypocet=1
            self.level=int(self.level)
            if self.level>=100000:
                  vypocet=20
            elif self.level>=50000:
                  vypocet=19
            elif self.level>=35000:
                  vypocet=18
            elif self.level>=30000:
                  vypocet=17
            elif self.level>=26000:
                  vypocet=16
            elif self.level>=22000:
                  vypocet=15
            elif self.level>=18000:
                  vypocet=14
            elif self.level>=15000:
                  vypocet=13
            elif self.level>=12000:
                  vypocet=12
            elif self.level>=10000:
                  vypocet=11
            elif self.level>=8000:
                  vypocet=10
            elif self.level>=6500:
                  vypocet=9
            elif self.level>=5000:
                  vypocet=8
            elif self.level>=3500:
                  vypocet=7
            elif self.level>=2500:
                  vypocet=6
            elif self.level>=1500:
                  vypocet=5
            elif self.level>=1000:
                  vypocet=4
            elif self.level>=500:
                  vypocet=3
            elif self.level>=200:
                  vypocet=2
            return ["Lives:"+str(self.zivoty[0])+"/"+str(self.zivoty[1]),"Mana:"+str(self.mana[0])+"/"+str(self.mana[1]),self.hlaska,"Level:"+str(vypocet),"XP:"+str(self.level)]

class Hrac:
      def __init__(self,jmeno,rasa,typ,level,zivoty,zivoty2,mana,mana2,hlaska,penize=0,attackBonus=-1,inventar=[],equipped=[],equippedtype=[0,0,0,0,0],bonus=[0,0,0]):
            self.attackBonus=int(attackBonus)
            self.bonus=[[0,25],[0,25],[0,10]]
            for i in range(len(bonus)):
                  self.bonus[i][0]=int(bonus[i])
            self.mise=[]
            self.attacks=["Smash -10lives -0mana"]
            if jmeno in ["Albatros","TEST"]:
                  self.pohyb=9999999999999999999999999999999999999999900
                  self.presVodu=100
                  pomProm=1
            else:
                  self.pohyb=10
                  self.presVodu=0
                  pomProm=0
            if penize!=0:
                  self.penize=int(penize)
            else:
                  self.penize=0
            self.x=10
            self.y=10
            self.jmeno=jmeno
            self.rasa=rasa
            self.typ=typ
            self.level=level  
            self.equipped=[]
            for i in equipped:
                  self.equipped.append(int(i))
            self.equippedType=[[0,1],[0,1],[0,10],[0,2],[0,1],[0,pomProm]]
            for i in range(len(equippedtype)):
                  self.equippedType[i][0]=int(equippedtype[i])
            if level==0:
                  self.level=1
                  if typ=="Wizzard":
                        self.zivoty=[0,0] 
                        self.mana=[50,50]
                  elif typ=="Ranger":      
                        self.zivoty=[30,30]
                        self.mana=[20,20]
                  elif typ=="Warrior":
                        self.zivoty=[50,50] 
                        self.mana=[0,0]
                  if rasa=="Human":
                        self.zivoty[1]+=10
                        self.zivoty[0]+=10
                        self.mana[1]+=40
                        self.mana[0]+=40
                  if rasa=="Elf":
                        self.zivoty[1]+=25
                        self.zivoty[0]+=25
                        self.mana[1]+=25
                        self.mana[0]+=25
                  if rasa=="Dwarf":
                        self.zivoty[1]+=50
                        self.zivoty[0]+=50
                        self.mana[1]+=0
                        self.mana[0]+=0
            else:
                  self.zivoty=[int(zivoty),int(zivoty2)] 
                  self.mana=[int(mana),int(mana2)]
            if self.zivoty[0]<=0:
                  self.zivoty[0]=self.zivoty[1]
            self.hlaska=hlaska 
            self.inventar=[]
            if inventar not in [[],"",0]:
                  for i in inventar:
                        self.inventar.append(int(i))
            for i in self.equipped:
                  self.addBonus(i)
            self.save()
            self.attack()

      def edit(self,zivoty,mana,hlaska,attackBonus,bonus):
            self.zivoty=zivoty
            self.mana=mana
            self.hlaska=hlaska
            self.attackBonus=attackBonus
            self.bonus=bonus

      def getToEdit(self):
            return [self.zivoty,self.mana,self.hlaska,self.attackBonus,self.bonus,self.rasa,self.typ]
      
      def testMise(self,miseSplnena=0):
            global hraZacala
            if miseSplnena==1:
                  a=mise(self.mise[0],self,[True])
            else:
                  a=mise(self.mise[0],self,self.mise[1]) 
                  if a not in [True,False]:      
                        hraZacala=a

      def addBonus(self,ID):
            if ID==0:
                  self.presVodu+=1
            if ID==1:
                  self.pohyb+=5
            if ID==2:
                  self.zivoty[0]+=50
                  self.zivoty[1]+=50
            if ID==3:
                  self.mana[0]+=50
                  self.mana[1]+=50
            if ID==6:
                  self.attacks.append("Knife attack -20lives -0mana") 
            if ID==7:
                  self.attacks.append("Bow attack -30lives -0mana") 
            if ID==8:
                  self.attacks.append("Stick strike -20lives -0mana")
                  self.attacks.append("Firebolt -25lives -25mana") 
                  self.attacks.append("Fireball -50lives -60mana")
                  self.attacks.append("ignition -35lives -40mana")
            if ID==9:
                  self.attacks.append("Sword swing -40lives -0mana") 
            if ID==10:
                  self.attacks.append("Crossbow shoot -35lives -0mana") 
            if ID==11:
                  self.attacks.append("Hammer slam -30lives -0mana") 
            if ID==12:
                  self.attacks.append("Axe slash -30lives -0mana") 
            if ID==13:
                  self.attacks.append("Destruction -10000lives -5000mana")
            if ID==14:
                  self.attacks.append("Server Kick -100000000000lives -0mana")

      def remuveBounus(self,ID):
            pomSez=[]
            if ID==0:
                  self.presVodu-=1
            if ID==1:
                  self.pohyb-=5
            if ID==2:
                  self.zivoty[0]-=50
                  self.zivoty[1]-=50
            if ID==3:
                  self.mana[0]-=50
                  self.mana[1]-=50
            if ID==6:
                  for i in self.attacks:
                        if i!="Knife attack -20lives -0mana":
                              pomSez.append(i)
                  self.attacks=pomSez
                  pomSez=[]
            if ID==7:
                  for i in self.attacks:
                        if i!="Bow attack -30lives -0mana":
                              pomSez.append(i)
                  self.attacks=pomSez
                  pomSez=[]
            if ID==8:
                  for i in self.attacks:
                        if i not in ["Stick strike -20lives -0mana", "Firebolt -25lives -25mana", "Fireball -50lives -60mana", "ignition -35lives -40mana"]:
                              pomSez.append(i)
                  self.attacks=pomSez
                  pomSez=[]
            if ID==9:
                  for i in self.attacks:
                        if i!="Sword swing -40lives -0mana":
                              pomSez.append(i)
                  self.attacks=pomSez
                  pomSez=[]
            if ID==10:
                  for i in self.attacks:
                        if i!="Crossbow shoot -35lives -0mana":
                              pomSez.append(i)
                  self.attacks=pomSez
                  pomSez=[]
            if ID==11:
                  for i in self.attacks:
                        if i!="Hammer slam -30lives -0mana":
                              pomSez.append(i)
                  self.attacks=pomSez
                  pomSez=[]
            if ID==12:
                  for i in self.attacks:
                        if i!="Axe slash -30lives -0mana":
                              pomSez.append(i)
                  self.attacks=pomSez
                  pomSez=[]
            if ID==13:
                  for i in self.attacks:
                        if i!="Destruction -10000lives -5000mana":
                              pomSez.append(i)
                  self.attacks=pomSez
                  pomSez=[]
            if ID==14:
                  for i in self.attacks:
                        if i!="Server Kick -100000000000lives -0mana":
                              pomSez.append(i)
                  self.attacks=pomSez
                  pomSez=[]


      def equip(self,ID):
            pomSez=[]
            pomProm=1
            if 3 in ItemsType[ID]:
                  if ID in self.inventar and ID not in self.equipped and self.equippedType[3][0]<self.equippedType[3][1] and self.equippedType[4][0]<=0:
                        for i in self.inventar:
                              if i==ID and pomProm==1:
                                    pomProm=0
                              else:
                                    pomSez.append(i)
                        self.inventar=pomSez
                        self.equipped.append(ID)
                        self.equippedType[ItemsType[ID][0]][0]+=1
                        self.addBonus(ID)
                        return True
            elif 4 in ItemsType[ID]:
                  if ID in self.inventar and ID not in self.equipped and self.equippedType[4][0]<self.equippedType[4][1] and self.equippedType[3][0]<=0:
                        for i in self.inventar:
                              if i==ID and pomProm==1:
                                    pomProm=0
                              else:
                                    pomSez.append(i)
                        self.inventar=pomSez
                        self.equipped.append(ID)
                        self.equippedType[ItemsType[ID][0]][0]+=1
                        self.addBonus(ID)
                        return True
            else:
                  if ID in self.inventar and ID not in self.equipped and self.equippedType[ItemsType[ID][0]][0]<self.equippedType[ItemsType[ID][0]][1]:
                        for i in self.inventar:      
                              if i==ID and pomProm==1:
                                    pomProm=0
                              else:
                                    pomSez.append(i)
                        self.inventar=pomSez
                        self.equipped.append(ID)
                        self.equippedType[ItemsType[ID][0]][0]+=1
                        self.addBonus(ID)
                        return True
                  return False

      def unequip(self,ID):
            pomSez=[]
            if ID in self.equipped:
                  for i in self.equipped:
                        if i!=ID:
                              pomSez.append(i)
                  self.equipped=pomSez
                  self.equippedType[ItemsType[ID][0]][0]-=1
                  self.inventar.append(ID)
                  self.remuveBounus(ID)
                  return True
            return False

      def save(self):
            if 2 in self.equipped:
                  self.zivoty[0]-=50
                  self.zivoty[1]-=50
            if 3 in self.equipped:
                  self.mana[0]-=50
                  self.mana[1]-=50
            bonus=[]
            for i in self.bonus:
                  bonus.append(i[0])
            ulozHrace(self.jmeno,self.rasa,self.typ,self.level,self.zivoty,self.mana,self.hlaska,self.inventar,self.penize,self.equipped,self.equippedType,self.attackBonus,bonus)
            if 2 in self.equipped:
                  self.zivoty[0]+=50
                  self.zivoty[1]+=50
            if 3 in self.equipped:
                  self.mana[0]+=50
                  self.mana[1]+=50

      def getZivoty(self):
            return self.zivoty
      
      def getMana(self):
            return self.mana

      def attack(self):
            list=[]
            a=""
            b=""
            c=""
            d=0
            for i in self.attacks:
                  for j in i:
                        if d==0 and j=="-":
                              d=1
                              b+=j
                        elif d==0:
                              a+=j
                        elif d==1 and j=="l":
                              d=2
                        elif d==1:
                              b+=j
                        elif d==2 and j=="-":
                              d=3
                              c+=j
                        elif d==3 and j=="m":
                              d=4 
                        elif d==3:
                              c+=j 
                  if c=="":
                        c=0       
                  list.append([a,int(b),int(c)]) 
                  a=""
                  b=""
                  c=""
                  d=0 
            return list

      def getToAttack(self):
            vypocet=1
            self.level=int(self.level)
            if self.level>=100000:
                  vypocet=20
            elif self.level>=50000:
                  vypocet=19
            elif self.level>=35000:
                  vypocet=18
            elif self.level>=30000:
                  vypocet=17
            elif self.level>=26000:
                  vypocet=16
            elif self.level>=22000:
                  vypocet=15
            elif self.level>=18000:
                  vypocet=14
            elif self.level>=15000:
                  vypocet=13
            elif self.level>=12000:
                  vypocet=12
            elif self.level>=10000:
                  vypocet=11
            elif self.level>=8000:
                  vypocet=10
            elif self.level>=6500:
                  vypocet=9
            elif self.level>=5000:
                  vypocet=8
            elif self.level>=3500:
                  vypocet=7
            elif self.level>=2500:
                  vypocet=6
            elif self.level>=1500:
                  vypocet=5
            elif self.level>=1000:
                  vypocet=4
            elif self.level>=500:
                  vypocet=3
            elif self.level>=200:
                  vypocet=2
            return ["Lives:"+str(self.zivoty[0])+"/"+str(self.zivoty[1]),"Mana:"+str(self.mana[0])+"/"+str(self.mana[1]),self.hlaska,"Level:"+str(vypocet),"XP:"+str(self.level)]
            

      def __str__(self):
            self.save()
            vypocet=1
            self.level=int(self.level)
            if self.level>=100000:
                  vypocet=20
            elif self.level>=50000:
                  vypocet=19
            elif self.level>=35000:
                  vypocet=18
            elif self.level>=30000:
                  vypocet=17
            elif self.level>=26000:
                  vypocet=16
            elif self.level>=22000:
                  vypocet=15
            elif self.level>=18000:
                  vypocet=14
            elif self.level>=15000:
                  vypocet=13
            elif self.level>=12000:
                  vypocet=12
            elif self.level>=10000:
                  vypocet=11
            elif self.level>=8000:
                  vypocet=10
            elif self.level>=6500:
                  vypocet=9
            elif self.level>=5000:
                  vypocet=8
            elif self.level>=3500:
                  vypocet=7
            elif self.level>=2500:
                  vypocet=6
            elif self.level>=1500:
                  vypocet=5
            elif self.level>=1000:
                  vypocet=4
            elif self.level>=500:
                  vypocet=3
            elif self.level>=200:
                  vypocet=2
            return self.jmeno + "\n" + self.rasa + "\n" + self.typ + "\n" + str(self.level) + "XP = level " + str(vypocet) + "\n" + self.hlaska 
      def getItems(self):
            return [self.inventar,self.equipped]
# ---------- proměné ----------
hracNaUtok=False
tah=1
attackTo=0
jmenaMest={1:"Town 1",2:"Town 2",3:"Town 3",4:"Town 4",5:"Town 5",6:"Town 6",7:"Town 7",8:"Town 8",9:"Town 9",10:"Town 10",11:"Town 11",12:"Town 12",13:"Town 13",14:"Town 14",15:"Town 15",16:"Town 16",17:"Town 17",18:"Town 18",19:"Town 19",20:"Town 20"}
FPS=100
rasa=""
typ=""
x=10
naTahu=1
y=10
item=0
pomProm=False
eItem=0
smer=False
hraZacala=False
muzesposunout=1
BLACK       = (  0,   0,   0)
BLUE        = (  0,   0, 255)
GREEN       = (  0, 200,   0)
WHITE       = (255, 255, 255)
DARKGREEN   = (  0, 120,   0)
seznamJmenHracu=nactiJmenaHrace()
seznamHracu=[]
for i in seznamJmenHracu:
      seznamHracu.append(Hrac(i,nactiHrace(i)[0],nactiHrace(i)[1],nactiHrace(i)[2],nactiHrace(i)[3],nactiHrace(i)[4],nactiHrace(i)[5],nactiHrace(i)[6],nactiHrace(i)[7],nactiHrace(i)[8],nactiHrace(i)[9],nactiHrace(i)[10],nactiHrace(i)[11],nactiHrace(i)[12],nactiHrace(i)[13]))
seznamMest=[]
zadavani=False
zad=""
var=""
nextChar="m"
cisloHrace=0 
seznamJmenNPC=nactiJmenaNPC()
seznamNPC=[]
for i in seznamJmenNPC:
      seznamNPC.append(NPC(nactiNPC(i)[0],nactiNPC(i)[1],nactiNPC(i)[2],nactiNPC(i)[3],nactiNPC(i)[4],nactiNPC(i)[5],nactiNPC(i)[6],nactiNPC(i)[7],nactiNPC(i)[8]))
min=0
max=6
add=0
min2=0
max2=6
add2=0
muzesDalsi=True
HracNaEditaci=True
# ---------- Funkce ----------  
def ulozVse():
      globals
      ulozJmenaHracu(seznamJmenHracu)
      for i in seznamHracu:
            i.save()


def addCharacter(jmeno,rasa,typ):
      seznamJmenHracu.append(jmeno)
      seznamHracu.append(Hrac(jmeno,rasa,typ,0,0,0,0,0,""))


def character():
      try:
            pygame.mixer.music.load('sounds/newcharactermusic.wav')
      except:
            pygame.mixer.music.load('generování map/sounds/newcharactermusic.wav')
      global hraZacala
      hraZacala="Character"
      pygame.mixer.music.play(-1)


def zacatekHry():
      try:
            pygame.mixer.music.load('sounds/gamemusic.wav')
      except:
            pygame.mixer.music.load('generování map/sounds/gamemusic.wav')
      global hraZacala
      hraZacala=True
      pygame.mixer.music.play(-1)


def konecHry():
      try:
            pygame.mixer.music.load('sounds/menumusic.wav')
      except:
            pygame.mixer.music.load('generování map/sounds/menumusic.wav')
      global hraZacala
      hraZacala=False
      pygame.mixer.music.play(-1)

def doMesta():
      try:
            pygame.mixer.music.load('sounds/townmusic.wav')
      except:
            pygame.mixer.music.load('generování map/sounds/townmusic.wav')
      global hraZacala
      hraZacala="mesto"
      pygame.mixer.music.play(-1)


def souboj(name):
      try:
            pygame.mixer.music.load('sounds/warmusic.wav')
      except:
            pygame.mixer.music.load('generování map/sounds/warmusic.wav')
      global hraZacala, hracNaUtok
      hraZacala="souboj"
      pygame.mixer.music.play(-1)
      hracNaUtok=name
      


def testVlastnosti(cisloHrace):
      global seznamHracu
      if 4 in seznamHracu[cisloHrace].equipped:
            if seznamHracu[cisloHrace].zivoty[0]+1<=seznamHracu[cisloHrace].zivoty[1]:
                  seznamHracu[cisloHrace].zivoty[0]+=1
      if 5 in seznamHracu[cisloHrace].equipped:
            if seznamHracu[cisloHrace].mana[0]+1<=seznamHracu[cisloHrace].mana[1]:
                  seznamHracu[cisloHrace].mana[0]+=1


def afterMove(num):
      global seznamHracu, cisloHrace, sound2, x, y
      pomProm=0
      seznamHracu[cisloHrace].pohyb-=num
      pygame.mixer.Sound.play(sound2)
      testVlastnosti(cisloHrace)
      seznamHracu[cisloHrace].x=x
      seznamHracu[cisloHrace].y=y
      

def mapa():
      global list, x, y, seznamHracu, seznamMest
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
      for i in seznamHracu:
            i.x=x
            i.y=y
      for i in range(len(list)):
            for j in range(len(list[i])):
                  if list[i][j]==5:
                        list[i][j]=6
      pomSez=[]
      for i in range(3):
            m=[randint(1,len(list)-2),randint(1,len(list)-2)]
            while True:
                  m=[randint(1,len(list)-2),randint(1,len(list)-2)]
                  if list[m[0]][m[1]] in [6,7,8,9,10,11,12,13,14,15] and m not in pomSez and (list[m[0]+1][m[1]]>5 or list[m[0]-1][m[1]]>5 or list[m[0]][m[1]+1]>5 or list[m[0]][m[1]-1]>5):
                        break
            list[m[0]][m[1]]=5
            seznamMest.append(Town(m[1],m[0]))
            pomSez.append(m)

def posledni(prom):
      a=len(prom)
      prom2=""
      for i in range(a-1):
            prom2+=prom[i]
      return prom2

def odeberItem(prom,odeber):
      prom2=[]
      for i in range(len(prom)):
            if prom[i]!=odeber:
                  prom2.append(prom[i])
      return prom2

def editPlayer():
      global hraZacala
      hraZacala="EditPlayer"


def hracVypis(cisloHrace):
      global seznamHracu, display
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
      ret.append("Number of move "+str(seznamHracu[cisloHrace].pohyb))
      return ret


def nextPlayer():
      global x, y, seznamHracu, cisloHrace, item, eItem, seznamMest, add, add2, tah, attackTo
      attackTo=0
      eItem=0
      item=0
      seznamHracu[cisloHrace].x=x
      seznamHracu[cisloHrace].y=y
      add=0
      add2=0
      while True:
            if cisloHrace+1!=len(seznamHracu):
                  cisloHrace+=1
            else: 
                  cisloHrace=0
            tah+=1
            if seznamHracu[cisloHrace].zivoty[0]>0:
                  break
            else:
                  seznamHracu[cisloHrace].x=0
                  seznamHracu[cisloHrace].y=0
      x=seznamHracu[cisloHrace].x
      y=seznamHracu[cisloHrace].y
      if seznamHracu[cisloHrace].jmeno in ["Albatros","TEST"]:
            seznamHracu[cisloHrace].pohyb=9999999999999999999999999999999999999999900
      else:
            seznamHracu[cisloHrace].pohyb=10
      if 1 in seznamHracu[cisloHrace].equipped:
            seznamHracu[cisloHrace].pohyb+=5
      if randint(1,100)>60:
            seznamMest[randint(0,len(seznamMest)-1)].additem()
      if randint(1,100)>80:
            seznamMest[randint(0,len(seznamMest)-1)].addMission()
# ---------- Zadání funkcí a vytvoření okny pygame ----------
mapa()

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode([0,0],pygame.FULLSCREEN)
pygame.display.set_caption('Tydral')

# ---------- načtení fontů, textůr a zvuků ----------
try:
      pygame.mixer.music.load('generování map/sounds/menumusic.wav')   # muzika menu
      sound1=pygame.mixer.Sound('generování map/sounds/sound01.wav')   # zvuk vstupu do města
      sound2=pygame.mixer.Sound('generování map/sounds/sound02.wav')   # zvuk pohybu
      sound3=pygame.mixer.Sound('generování map/sounds/sound03.wav')   # zvuk nákupu
      sound4=pygame.mixer.Sound('generování map/sounds/sound04.wav')   # zvuk útoku mečem, nožem, sekerou
      sound5=pygame.mixer.Sound('generování map/sounds/sound05.wav')   # zvuk ohnivého útoku
      sound7=pygame.mixer.Sound('generování map/sounds/sound07.wav')   # zvuk Chyby
      sound8=pygame.mixer.Sound('generování map/sounds/sound08.wav')   # zvuk Chyby
      sound9=pygame.mixer.Sound('generování map/sounds/sound09.wav')   # zvuk nedostatku peněz
      newMapSound=pygame.mixer.Sound('generování map/sounds/newmapsound.wav')   # zvuk vytoření nové mapy
except:
      pygame.mixer.music.load('sounds/menumusic.wav')
      sound1=pygame.mixer.Sound('sounds/sound01.wav')
      sound2=pygame.mixer.Sound('sounds/sound02.wav')
      sound3=pygame.mixer.Sound('sounds/sound03.wav')
      sound4=pygame.mixer.Sound('sounds/sound04.wav')
      sound5=pygame.mixer.Sound('sounds/sound05.wav')
      sound7=pygame.mixer.Sound('sounds/sound07.wav')
      sound8=pygame.mixer.Sound('sounds/sound08.wav')
      sound9=pygame.mixer.Sound('sounds/sound09.wav')
      newMapSound=pygame.mixer.Sound('sounds/newmapsound.wav') 
pygame.mixer.music.play(-1)


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
nazev = fontnazev.render("Tydral", True, WHITE)

try:
      grass=pygame.image.load('textury/travnik.png')
      water=pygame.image.load('textury/voda.png')
      mountine=pygame.image.load('textury/hora.png')
      tree=pygame.image.load('textury/les.png')
      town=pygame.image.load('textury/mesto.png')
      logo=pygame.image.load('data/logo.png')
except:
      grass=pygame.image.load('generování map/textury/travnik.png')
      water=pygame.image.load('generování map/textury/voda.png')
      mountine=pygame.image.load('generování map/textury/hora.png')
      tree=pygame.image.load('generování map/textury/les.png')
      town=pygame.image.load('generování map/textury/mesto.png')
      logo=pygame.image.load('generování map/data/logo.png')
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
                        if event.key == K_RETURN and hraZacala == True:
                              nextPlayer()
                        if event.key == K_n:
                              generateList(GrafickeRozhrani=0)
                              mapa()
                              pygame.mixer.Sound.play(newMapSound)
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
                        if event.key == K_e and hraZacala==False:
                              editPlayer()
                        if event.key == K_TAB and hraZacala!="mesto":
                              konecHry()
                        if event.key == K_TAB and hraZacala=="mesto":
                              nextPlayer()
                              zacatekHry()
                        if event.key == K_ESCAPE:
                              ulozVse()
                              pygame.quit()
                              sys.exit()
                  if event.type == MOUSEBUTTONDOWN:
                        if mouse[0] > 750 and mouse[0] < 900 and mouse[1] > 400 and mouse[1] < 450 and hraZacala==True and list[(y-10)//11][(x-10)//11]==5:
                              doMesta()
                              pygame.mixer.Sound.play(sound1)
                        if mouse[0] > 150 and mouse[0] < 250 and mouse[1] > 450 and mouse[1] < 500 and hraZacala==False:
                              zacatekHry()
                        if mouse[0] > 300 and mouse[0] < 400 and mouse[1] > 450 and mouse[1] < 500 and hraZacala==False:
                              generateList(GrafickeRozhrani=0)
                              mapa()
                              pygame.mixer.Sound.play(newMapSound)
                        if mouse[0] > 300 and mouse[0] < 400 and mouse[1] > 450 and mouse[1] < 500 and hraZacala=="Character":
                              konecHry()
                              pygame.mixer.music.unpause()
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
                                    pygame.mixer.Sound.play(sound7)
                              elif len(zad)<3:
                                    var="Zadané jméno je příliš krátké"
                                    pygame.mixer.Sound.play(sound7)
                              elif len(zad)>20:
                                    var="Zadané jméno je příliš dlouhé"
                                    pygame.mixer.Sound.play(sound8)
                              elif rasa not in ['Human','Elf','Dwarf']:
                                    var="Nezadal jsi rasu postavy"
                                    pygame.mixer.Sound.play(sound7)
                              elif typ not in ['Warrior','Ranger','Wizzard']:
                                    var="Nezadal jsi classu postavy"
                                    pygame.mixer.Sound.play(sound7)
                              else:
                                    addCharacter(zad,rasa,typ)
                                    konecHry()
                                    var=""
                                    rasa=""
                                    typ=""
                                    pygame.mixer.music.unpause()
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
                              pygame.mixer.music.pause()
                              character()
                        if mouse[0] > 400 and mouse[0] < 800 and mouse[1] > 110 and mouse[1] < 160 and hraZacala=="Character":
                              zadavani=True
                        if mouse[0] > 900 and mouse[0] < 1100 and mouse[1] > 10 and mouse[1] <  60 and hraZacala==True:
                              nextPlayer()
                        if mouse[0] >  60 and mouse[0] < 160 and mouse[1] >  10 and mouse[1] <  60 and hraZacala=="mesto":
                              nextPlayer()
                              zacatekHry()
      if hraZacala==True:
            pomProm=0
            for i in seznamMest:
                  if i.sourednice[1]==(seznamHracu[cisloHrace].x-10)//11 and i.sourednice[0]==(seznamHracu[cisloHrace].y-10)//11:
                        pomProm=1
            if pomProm!=1 and tah>len(seznamHracu)*2:
                  pomSez=[]
                  for i in seznamHracu:
                        if i.x==seznamHracu[cisloHrace].x and i.y==seznamHracu[cisloHrace].y and i.jmeno!=seznamHracu[cisloHrace].jmeno:
                              pomSez.append(i.jmeno)
                  if len(pomSez)>1:
                        if mouse[0]>750 and mouse[0]<1200 and mouse[1]>400 and mouse[1]<450:
                              pygame.draw.rect(display,(0,255,0),(750,400,450,50))
                              if event.type==MOUSEBUTTONDOWN:
                                    if int(i.level)>=int(seznamHracu[cisloHrace].level):
                                          naTahu=1
                                    else:
                                          naTahu=2
                                    souboj(pomSez[attackTo])
                        else:
                              pygame.draw.rect(display,(0,200,0),(750,400,450,50))
                        for i in range(len(pomSez)):
                              display.blit(font3.render("Attack to "+pomSez[attackTo],True,(255,255,255)),(755,400))
                              pygame.draw.rect(display,(0,0,0),(1200,400,150,50))           
                              if mouse[0] > 1250 and mouse[0] < 1290 and mouse[1] > 400 and mouse[1] < 440:
                                    pygame.draw.polygon(display, (0,255,0), [[40+1250,0+400],[40+1250,40+400],[0+1250,20+400]])
                                    if event.type==MOUSEBUTTONDOWN:
                                          if attackTo-1>=0:
                                                attackTo-=1
                                          
                              else:
                                    pygame.draw.polygon(display, (0,200,0), [[40+1250,0+400],[40+1250,40+400],[0+1250,20+400]])
                              if mouse[0] > 1300 and mouse[0] < 1340 and mouse[1] > 400 and mouse[1] < 440:
                                    pygame.draw.polygon(display, (0,255,0), [[0+1300,0+400],[0+1300,40+400],[40+1300,20+400]])
                                    if event.type==MOUSEBUTTONDOWN:
                                          if attackTo+1<len(pomSez):
                                                attackTo+=1
                              else:
                                    pygame.draw.polygon(display, (0,200,0), [[0+1300,0+400],[0+1300,40+400],[40+1300,20+400]])
                  elif len(pomSez)==1:
                        if mouse[0]>750 and mouse[0]<1200 and mouse[1]>400 and mouse[1]<450:
                              pygame.draw.rect(display,(0,255,0),(750,400,450,50))
                              if event.type==MOUSEBUTTONDOWN:
                                    if int(i.level)>=int(seznamHracu[cisloHrace].level):
                                          naTahu=1
                                    else:
                                          naTahu=2
                                    souboj(pomSez[attackTo])
                        else:
                              pygame.draw.rect(display,(0,200,0),(750,400,450,50))
                        display.blit(font3.render("Attack to "+pomSez[attackTo],True,(255,255,255)),(755,400))
            if seznamHracu[cisloHrace].pohyb<=0:
                  nextPlayer()
            if list[(y-10)//11][(x-10)//11]==5:
                  if mouse[0] > 750 and mouse[0] < 900 and mouse[1] > 400 and mouse[1] < 450:
                        pygame.draw.rect(display, (  0, 255,  0),(750,400,150,50))
                        pygame.draw.rect(display,(20,20,20),(750,640,600,120))
                        for i in seznamMest:
                              if i.sourednice==[seznamHracu[cisloHrace].y//11,seznamHracu[cisloHrace].x//11]:
                                    townName=i.jmeno
                                    townItems=len(i.itemsToSell)
                                    townMise=i.hospod
                        display.blit(font2.render(townName,True,WHITE),(755,640))
                        display.blit(font2.render("Items to sell:"+str(townItems),True,WHITE),(755,670))
                        display.blit(font2.render("Missions:"+str(townMise),True,WHITE),(755,700))
                  else:
                        pygame.draw.rect(display, (  0, 200,  0),(750,400,150,50))
                  display.blit(font3.render("To Town",True,(255,255,255)),(755,400))

            if seznamHracu[cisloHrace].pohyb>0:
                  if smer == 1:
                        if y+11>=len(list)*11+10:
                              if list[0][(x-10)//11]>3:
                                    if list[0][(x-10)//11]>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                y=10
                                                afterMove(2)
                                    else:
                                                y=10
                                                afterMove(1)
                              elif seznamHracu[cisloHrace].presVodu>0:
                                    if list[0][(x-10)//11]>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                y=10
                                                afterMove(2)
                                    else:
                                                y=10
                                                afterMove(1)
                        else:
                              if list[(y+1)//11][(x-10)//11]>3:
                                    if list[(y+1)//11][(x-10)//11]>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                y+=11
                                                afterMove(2)
                                    else:
                                                y+=11
                                                afterMove(1)
                              elif seznamHracu[cisloHrace].presVodu>0:
                                    if list[(y+1)//11][(x-10)//11]>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                y+=11
                                                afterMove(2)                                                
                                    else:
                                                y+=11
                                                afterMove(1)
                                                
                        smer=False
                  # Pohyb směrem Dolů


                  if smer == 2:
                        if y-11<=0:
                              if list[len(list)-1][(x-10)//11]>3:
                                    if list[len(list)-1][(x-10)//11]>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                y=len(list)*11-1
                                                afterMove(2)
                                    else:
                                                y=len(list)*11-1
                                                afterMove(1)
                              elif seznamHracu[cisloHrace].presVodu>0:
                                    if list[len(list)-1][(x-10)//11]>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                y=len(list)*11-1
                                                afterMove(2)
                                    else:
                                                y=len(list)*11-1
                                                afterMove(1)
                        else:
                              if list[(y-21)//11][(x-10)//11]>3:
                                    if list[(y-21)//11][(x-10)//11]>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                y-=11
                                                afterMove(2)
                                    else:
                                                y-=11
                                                afterMove(1)
                              elif seznamHracu[cisloHrace].presVodu>0:
                                    if list[(y-21)//11][(x-10)//11]>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                y-=11
                                                afterMove(2)
                                    else:
                                                y-=11
                                                afterMove(1)
                                                
                        smer=False
                  # Pohyb směrem Nahoru


                  if smer == 3:
                        if x-11<=0:
                              if list[(y-10)//11][len(list)-1]>3:
                                    if list[(y-10)//11][len(list)-1]>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                x=len(list)*11-1
                                                afterMove(2)
                                    else:
                                                x=len(list)*11-1
                                                afterMove(1)
                              elif seznamHracu[cisloHrace].presVodu>0:
                                    if list[(y-10)//11][len(list)-1]>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                x=len(list)*11-1
                                                afterMove(2)
                                    else:
                                                x=len(list)*11-1
                                                afterMove(1)
                        else:
                              if list[(y-10)//11][(x-21)//11]>3:
                                    if list[(y-10)//11][(x-21)//11]>15:
                                          if seznamHracu[cisloHrace].pohyb>=2:
                                                x-=11
                                                afterMove(2)
                                    else:
                                                x-=11
                                                afterMove(1)
                              elif seznamHracu[cisloHrace].presVodu>0:
                                    if list[(y-10)//11][(x-21)//11]>15:
                                          if seznamHracu[cisloHrace].pohyb>=2:
                                                x-=11
                                                afterMove(2)
                                    else:
                                                x-=11
                                                afterMove(1)
                        smer=False
                  # Pohyb směrem Vleva


                  if smer == 4:       
                        if x+11>=len(list)*11+10:
                              if list[(y-10)//11][0]>3:
                                    if list[(y-10)//11][0]>3>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                x=10
                                                afterMove(2)
                                    else:
                                                x=10
                                                afterMove(1)
                              elif seznamHracu[cisloHrace].presVodu>0:
                                    if list[(y-10)//11][0]>3>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                x=10
                                                afterMove(2)
                                    else:
                                                x=10
                                                afterMove(1)
                        else:
                              if list[(y-10)//11][(x+1)//11]>3:
                                    if list[(y-10)//11][(x+1)//11]>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                x+=11
                                                afterMove(2)
                                    else:
                                                x+=11
                                                afterMove(1)
                              elif seznamHracu[cisloHrace].presVodu>0:
                                    if list[(y-10)//11][(x+1)//11]>15:
                                          if seznamHracu[cisloHrace].pohyb>1:
                                                x+=11
                                                afterMove(2)
                                    else:
                                                x+=11
                                                afterMove(1)
                        smer=False
                  # Pohyb směrem Vpravo


            
            for i in range(len(list)):
                  for j in range(len(list[i])):
                        if list[i][j]==5:
                              display.blit(town,(j*11+10,i*11+10,10,10))
                        elif list[i][j]<4:
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
            seznam=hracVypis(cisloHrace)
            for i in seznam:
                  display.blit(font3.render(i,True,WHITE),(760,70+poz))
                  poz+=50
            zivoty=seznamHracu[cisloHrace].getZivoty()
            mana=seznamHracu[cisloHrace].getMana()
            penize=seznamHracu[cisloHrace].penize
            display.blit(font3.render("Lives: "+str(zivoty[0])+"/"+str(zivoty[1]),True,WHITE),(955,70+50))
            display.blit(font3.render("Mana: "+str(mana[0])+"/"+str(mana[1]),True,WHITE),(955,70+100))
            display.blit(font3.render("Penize: "+str(penize),True,WHITE),(955,70+0))
            itemy=seznamHracu[cisloHrace].getItems()
            if len(itemy[0])>0:
                  if mouse[0] > 1250 and mouse[0] < 1290 and mouse[1] > 480 and mouse[1] < 520:
                        pygame.draw.polygon(display, (0,255,0), [[40+1250,0+480],[40+1250,40+480],[0+1250,20+480]])
                  else:
                        pygame.draw.polygon(display, (0,200,0), [[40+1250,0+480],[40+1250,40+480],[0+1250,20+480]])
                  if mouse[0] > 1300 and mouse[0] < 1340 and mouse[1] > 480 and mouse[1] < 520:
                        pygame.draw.polygon(display, (0,255,0), [[0+1300,0+480],[0+1300,40+480],[40+1300,20+480]])
                  else:
                        pygame.draw.polygon(display, (0,200,0), [[0+1300,0+480],[0+1300,40+480],[40+1300,20+480]])
                  if mouse[0] > 950 and mouse[0] < 1240 and mouse[1] > 480 and mouse[1] < 520:
                        pygame.draw.rect(display,(0,255,0),(930,475,300,50))
                        pygame.draw.rect(display,(20,20,20),(750,640,600,120))
                        if ItemsInfo[itemy[0][item]][1]!="Stick of fire":
                              display.blit(font2.render(ItemsInfo[itemy[0][item]][1],True,WHITE),(755,640))
                              display.blit(font2.render(ItemsInfo[itemy[0][item]][2],True,WHITE),(755,670))
                        else:
                              display.blit(font2.render(ItemsInfo[itemy[0][item]][1],True,WHITE),(755,640))
                              display.blit(font2.render(ItemsInfo[itemy[0][item]][2],True,WHITE),(755,670))
                              display.blit(font2.render(ItemsInfo[itemy[0][item]][3],True,WHITE),(755,700))
                  else:
                        pygame.draw.rect(display,(0,200,0),(930,475,300,50))
                  display.blit(font3.render("Inventory: "+ItemsID[int(itemy[0][item])],True,WHITE),(755,475))
            if len(itemy[1])>0:
                  if mouse[0] > 1250 and mouse[0] < 1290 and mouse[1] > 535 and mouse[1] < 575:
                        pygame.draw.polygon(display, (0,255,0), [[40+1250,0+535],[40+1250,40+535],[0+1250,20+535]])
                  else:
                        pygame.draw.polygon(display, (0,200,0), [[40+1250,0+535],[40+1250,40+535],[0+1250,20+535]])
                  if mouse[0] > 1300 and mouse[0] < 1340 and mouse[1] > 535 and mouse[1] < 575:
                        pygame.draw.polygon(display, (0,255,0), [[0+1300,0+535],[0+1300,40+535],[40+1300,20+535]])
                  else:
                        pygame.draw.polygon(display, (0,200,0), [[0+1300,0+535],[0+1300,40+535],[40+1300,20+535]])
                  if mouse[0] > 910 and mouse[0] < 1240 and mouse[1] > 530 and mouse[1] < 580:
                        pygame.draw.rect(display,(0,255,0),(910,530,320,50))
                        pygame.draw.rect(display,(20,20,20),(750,640,600,120))
                        if ItemsInfo[itemy[1][eItem]][1]!="Stick of fire":
                              display.blit(font2.render(ItemsInfo[itemy[1][eItem]][1],True,WHITE),(755,640))
                              display.blit(font2.render(ItemsInfo[itemy[1][eItem]][2],True,WHITE),(755,670))
                        else:
                              display.blit(font2.render(ItemsInfo[itemy[1][eItem]][1],True,WHITE),(755,640))
                              display.blit(font2.render(ItemsInfo[itemy[1][eItem]][2],True,WHITE),(755,670))
                              display.blit(font2.render(ItemsInfo[itemy[1][eItem]][3],True,WHITE),(755,700))
                  else:
                        pygame.draw.rect(display,(0,200,0),(910,530,320,50))
                  display.blit(font3.render("Equipped: "+ItemsID[int(itemy[1][eItem])],True,WHITE),(755,530))
            if seznamHracu[cisloHrace].mise!=[]:
                  if mouse[0] > 890 and mouse[0] < 1340 and mouse[1] > 585 and mouse[1] < 635:
                        pygame.draw.rect(display,(0,255,0),(890,585,460,50))
                        pygame.draw.rect(display,(20,20,20),(750,640,600,120))
                        if seznamHracu[cisloHrace].mise[0] in [0,5]:
                              display.blit(font2.render(nazvyMisi[seznamHracu[cisloHrace].mise[0]]+seznamHracu[cisloHrace].mise[2],True,WHITE),(755,640))
                        else:
                              display.blit(font2.render(nazvyMisi[seznamHracu[cisloHrace].mise[0]],True,WHITE),(755,640))
                        display.blit(font2.render(missionInfo[seznamHracu[cisloHrace].mise[0]][missionInfo[seznamHracu[cisloHrace].mise[0]][0]-1],True,WHITE),(755,670))
                  else:
                        pygame.draw.rect(display,(0,200,0),(890,585,450,50))
                  if seznamHracu[cisloHrace].mise[0] in [0,5]:
                        display.blit(font3.render("Mission: "+nazvyMisi[seznamHracu[cisloHrace].mise[0]]+seznamHracu[cisloHrace].mise[2],True,WHITE),(755,585))
                  else:
                        display.blit(font3.render("Mission: "+nazvyMisi[seznamHracu[cisloHrace].mise[0]],True,WHITE),(755,585))
                  if event.type == MOUSEBUTTONDOWN and mouse[0] > 890 and mouse[0] < 1340 and mouse[1] > 585 and mouse[1] < 635:
                              seznamHracu[cisloHrace].testMise()
            if event.type == MOUSEBUTTONUP:
                  muzesposunout=1
            if event.type == MOUSEBUTTONDOWN and muzesposunout==1:
                  muzesposunout=0
                  if len(itemy[0])>0:
                        if mouse[0] > 1250 and mouse[0] < 1290 and mouse[1] > 480 and mouse[1] < 520:
                              if item>0:
                                    item-=1
                              else:
                                    item=0
                        if mouse[0] > 1300 and mouse[0] < 1340 and mouse[1] > 480 and mouse[1] < 520:
                              if item<len(itemy[0])-1:
                                    item+=1
                              else:
                                    item=len(itemy[0])-1
                        if mouse[0] > 950 and mouse[0] < 1240 and mouse[1] > 480 and mouse[1] < 520:
                              pomProm=seznamHracu[cisloHrace].equip(int(itemy[0][item]))
                              if item!=0 and pomProm==True:
                                    item-=1
                  if len(itemy[1])>0:
                        if mouse[0] > 1250 and mouse[0] < 1290 and mouse[1] > 535 and mouse[1] < 575:
                              if eItem>0:
                                    eItem-=1
                              else:
                                    eItem=0
                        if mouse[0] > 1300 and mouse[0] < 1340 and mouse[1] > 535 and mouse[1] < 575:
                              if eItem<len(itemy[1])-1:
                                    eItem+=1
                              else:
                                    eItem=len(itemy[1])-1
                        if mouse[0] > 910 and mouse[0] < 1240 and mouse[1] > 530 and mouse[1] < 580:
                              pomProm=seznamHracu[cisloHrace].unequip(int(itemy[1][eItem]))
                              if eItem!=0 and pomProm==True:
                                    eItem-=1
                        
      elif hraZacala==False:
            display.blit(logo,(760,200,512,512))
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
      elif hraZacala=="mesto":
            poz=0
            seznam=hracVypis(cisloHrace)
            zivoty=seznamHracu[cisloHrace].getZivoty()
            mana=seznamHracu[cisloHrace].getMana()
            penize=seznamHracu[cisloHrace].penize
            display.blit(font3.render("Lives: "+str(zivoty[0])+"/"+str(zivoty[1]),True,WHITE),(260,70+50))
            display.blit(font3.render("Mana: "+str(mana[0])+"/"+str(mana[1]),True,WHITE),(260,70+100))
            display.blit(font3.render("Penize: "+str(penize),True,WHITE),(260,70+0))
            for i in seznam:
                  if poz<250:
                        display.blit(font3.render(i,True,WHITE),(60,70+poz))
                        poz+=50
            mesto=""
            for i in seznamMest:
                  if i.sourednice==[(y-10)//11,(x-10)//11]:
                        mesto=i.__str__()
                        mesto2=i.getItems()
                        mesto3=i.hospod
                        mesto4=i.mise
            seznam=[]
            pomProm=""
            for i in mesto:
                  if i=="\n":
                        seznam.append(pomProm)
                        pomProm=""
                  else:
                        pomProm+=i
            
            for i in seznam:
                  display.blit(font3.render(i,True,WHITE),(60,70+poz))
                  poz+=50 

            if mouse[0] > 60 and mouse[0] < 160 and mouse[1] > 10 and mouse[1] < 60:
                  pygame.draw.rect(display, (  0,   0, 255),(60, 10, 100, 50))
            else:
                  pygame.draw.rect(display, (  0,   0, 150),(60, 10, 100, 50))
            display.blit(font3.render("BACK",True,WHITE),(65,10))
            poz2=poz
            display.blit(font3.render("Tavern mission: "+str(mesto3),True,WHITE),(405,20+poz))
            for i in range(mesto3):
                  if mouse[0] > 400 and mouse[0] < 705 and mouse[1] > 70+poz2 and mouse[1] < 70+poz2+50:
                        pygame.draw.rect(display, (  0,   0, 255),(400, 70+poz2, 305, 50))
                        pygame.draw.rect(display, ( 20,  20,  20),(725, 420, 630, 340))
                        poz3=0
                        for k in range(1,missionInfo[mesto4[i]][0]):
                              display.blit(font3.render(missionInfo[mesto4[i]][k],True,WHITE),(730,420+poz3))
                              poz3+=60
                  else:
                        pygame.draw.rect(display, (  0,   0, 150),(400, 70+poz2, 305, 50))
                  if mesto4[i]==0:
                        display.blit(font3.render("Bring boat Here",True,WHITE),(405,70+poz2))
                  elif mesto4[i]==5:
                        display.blit(font3.render("Bring sword Here",True,WHITE),(405,70+poz2))
                  else:
                        display.blit(font3.render(nazvyMisi[mesto4[i]],True,WHITE),(405,70+poz2))
                  if event.type == MOUSEBUTTONUP:
                        muzu=True
                  if event.type == MOUSEBUTTONDOWN:
                        if mouse[0] > 400 and mouse[0] < 700 and mouse[1] > 70+poz2 and mouse[1] < 70+poz2+50 and muzu==True:
                              muzu=False
                              for j in seznamMest:
                                    if j.sourednice==[(y-10)//11,(x-10)//11] and seznamHracu[cisloHrace].mise==[]:
                                          if mesto4[i] in [0,5]:
                                                seznamHracu[cisloHrace].mise=[mesto4[i],j.sourednice,j.jmeno]
                                          else:
                                                seznamHracu[cisloHrace].mise=[mesto4[i],j.sourednice]
                                          j.hospod-=1
                                          j.mise=odeberItem(j.mise,mesto4[i])
                  poz2+=60 
                              
            if event.type == MOUSEBUTTONUP:
                  muzu=True
            for i in mesto2:
                  if event.type == MOUSEBUTTONDOWN:
                        if mouse[0] > 60 and mouse[0] < 360 and mouse[1] > 70+poz and mouse[1] < 70+poz+50 and muzu==True:
                              muzu=False
                              if seznamHracu[cisloHrace].penize>=cenaItemu[i]:
                                    seznamHracu[cisloHrace].penize-=cenaItemu[i]
                                    seznamHracu[cisloHrace].inventar.append(i)
                                    pygame.mixer.Sound.play(sound3)
                                    for j in seznamMest:
                                          if j.sourednice==[(y-10)//11,(x-10)//11]:
                                                j.itemsToSell=odeberItem(j.itemsToSell,i)
                                    seznamHracu[cisloHrace].save()
                              else:
                                    pygame.mixer.Sound.play(sound9)
                  if mouse[0] > 60 and mouse[0] < 360 and mouse[1] > 70+poz and mouse[1] < 70+poz+50:
                        pygame.draw.rect(display, (  0,   0, 255),(60, 70+poz, 300, 50))
                        pygame.draw.rect(display, ( 20,  20,  20),(725, 420, 630, 340))
                        poz3=0
                        for k in range(1,ItemsInfo[i][0]):
                              display.blit(font3.render(ItemsInfo[i][k],True,WHITE),(730,420+poz3))
                              poz3+=60
                  else:
                        pygame.draw.rect(display, (  0,   0, 150),(60, 70+poz, 300, 50))
                  display.blit(font3.render(ItemsID[i],True,WHITE),(65,70+poz))
                  poz+=60
      elif hraZacala=="souboj":
            poz=0
            poz2=0
            pomSez=[]
            display.blit(font3.render(seznamHracu[cisloHrace].jmeno,True,WHITE),(10,10))
            for i in range(len(seznamHracu)):
                  if seznamHracu[i].jmeno==hracNaUtok:
                        pomSez.append(i)
            jmeno=seznamHracu[pomSez[0]].jmeno
            for i in seznamHracu[cisloHrace].getToAttack():
                  display.blit(font3.render(str(i),True,WHITE),(300,10+poz))
                  poz+=60
            poz=0
            if seznamHracu[pomSez[0]].zivoty[0]<=0 or seznamHracu[cisloHrace].zivoty[0]<=0:
                  if seznamHracu[cisloHrace].zivoty[0]<=0:
                        x=0
                        y=0
                  elif seznamHracu[pomSez[0]].zivoty[0]<=0:
                        seznamHracu[pomSez[0]].x=0
                        seznamHracu[pomSez[0]].y=0
                  naTahu=1
                  nextPlayer()
                  zacatekHry()
            if naTahu==1:
                  if mouse[0] > 10 and mouse[0] < 260 and mouse[1] > 480 and mouse[1] < 530:
                        pygame.draw.rect(display,(0,0,255),(10,480,250,50))
                        if event.type == MOUSEBUTTONDOWN:
                              if seznamHracu[cisloHrace].zivoty[0]+5<=seznamHracu[cisloHrace].zivoty[1]:
                                    seznamHracu[cisloHrace].zivoty[0]+=5
                              else:
                                    seznamHracu[cisloHrace].zivoty[0]=seznamHracu[cisloHrace].zivoty[1]
                              if seznamHracu[cisloHrace].mana[0]+10<=seznamHracu[cisloHrace].mana[1]:
                                    seznamHracu[cisloHrace].mana[0]+=10
                              else:
                                    seznamHracu[cisloHrace].mana[0]=seznamHracu[cisloHrace].mana[1]
                              testVlastnosti(cisloHrace)
                              naTahu=2
                  else:
                        pygame.draw.rect(display,(0,0,200),(10,480,250,50))
                  display.blit(font3.render("Pass",True,WHITE),(100,480))
                  if mouse[0] > 270 and mouse[0] < 520 and mouse[1] > 480 and mouse[1] < 530:
                        pygame.draw.rect(display,(0,0,255),(270,480,250,50))
                        if event.type == MOUSEBUTTONDOWN:
                              a=randint(0,len(seznamMest)-1)
                              seznamHracu[pomSez[0]].penize+=seznamHracu[cisloHrace].penize
                              seznamHracu[cisloHrace].penize=0
                              y=seznamMest[a].sourednice[0]*11+10
                              x=seznamMest[a].sourednice[1]*11+10
                              zacatekHry()  
                              nextPlayer()
                  else:
                        pygame.draw.rect(display,(0,0,200),(270,480,250,50))
                  display.blit(font3.render("Surrender",True,WHITE),(310,480))
                  if len(seznamHracu[cisloHrace].attack())<8:
                        for i in seznamHracu[cisloHrace].attack():
                              pomText=str(i[0])
                              if mouse[0] > 10 and mouse[0] < 260 and mouse[1] > 60+poz and mouse[1] < 110+poz:
                                    pygame.draw.rect(display,(0,0,255),(10,60+poz,250,50))
                                    pygame.draw.rect(display,(20,20,20),(10,550,650,200))
                                    display.blit(font3.render(pomText,True,WHITE),(10,550))
                                    display.blit(font3.render(popisky[pomText][0],True,WHITE),(10,600))
                                    display.blit(font3.render(popisky[pomText][1],True,WHITE),(10,650))
                                    if event.type == MOUSEBUTTONUP and muzesDalsi==False:
                                          muzesDalsi=True
                                    if event.type == MOUSEBUTTONDOWN and muzesDalsi==True:
                                          muzesDalsi=False
                                          if seznamHracu[cisloHrace].mana[0]+i[2]>=0:
                                                if randint(1,20)>10-seznamHracu[cisloHrace].attackBonus:
                                                      seznamHracu[pomSez[0]].zivoty[0]+=i[1]
                                                seznamHracu[cisloHrace].mana[0]+=i[2]
                                                naTahu=2
                              else:
                                    pygame.draw.rect(display,(0,0,200),(10,60+poz,250,50))
                              display.blit(font3.render(pomText,True,WHITE),(10,60+poz))
                              poz+=60

                  else:
                        for i in range(len(seznamHracu[cisloHrace].attack())):
                              if i>=min+add and i<max+add:
                                    pomText=str(seznamHracu[cisloHrace].attack()[i][0])
                                    if mouse[0] > 10 and mouse[0] < 260 and mouse[1] > 60+poz and mouse[1] < 110+poz:
                                          pygame.draw.rect(display,(0,0,255),(10,60+poz,250,50))
                                          pygame.draw.rect(display,(20,20,20),(10,550,650,200))
                                          display.blit(font3.render(pomText,True,WHITE),(10,550))
                                          display.blit(font3.render(popisky[pomText][0],True,WHITE),(10,600))
                                          display.blit(font3.render(popisky[pomText][1],True,WHITE),(10,650))
                                          if event.type == MOUSEBUTTONUP and muzesDalsi==False:
                                                muzesDalsi=True
                                          if event.type == MOUSEBUTTONDOWN and muzesDalsi==True:
                                                muzesDalsi=False
                                                if seznamHracu[cisloHrace].mana[0]+seznamHracu[cisloHrace].attack()[i][2]>=0:
                                                      if randint(1,20)>10-seznamHracu[cisloHrace].attackBonus:
                                                            seznamHracu[pomSez[0]].zivoty[0]+=seznamHracu[cisloHrace].attack()[i][1]
                                                      seznamHracu[cisloHrace].mana[0]+=seznamHracu[cisloHrace].attack()[i][2]
                                                      naTahu=2
                                    else:
                                          pygame.draw.rect(display,(0,0,200),(10,60+poz,250,50))
                                    display.blit(font3.render(pomText,True,WHITE),(10,60+poz))
                                    poz+=60
                        if mouse[0] > 65 and mouse[0] < 115 and mouse[1] > 420 and mouse[1] < 470:
                              pygame.draw.polygon(display, (0,255,0), [[ 65,420],[115,420],[ 90,470]])
                              if event.type == MOUSEBUTTONUP and muzesDalsi==False:
                                    muzesDalsi=True
                              if event.type == MOUSEBUTTONDOWN and muzesDalsi==True:
                                    if max+add<len(seznamHracu[cisloHrace].attack()):
                                          muzesDalsi=False
                                          add+=1
                        else:
                              pygame.draw.polygon(display, (0,200,0), [[ 65,420],[115,420],[ 90,470]])
                        if mouse[0] > 125 and mouse[0] < 175 and mouse[1] > 420 and mouse[1] < 470:
                              pygame.draw.polygon(display, (0,255,0), [[125,470],[175,470],[150,420]])
                              if event.type == MOUSEBUTTONUP and muzesDalsi==False:
                                    muzesDalsi=True
                              if event.type == MOUSEBUTTONDOWN and muzesDalsi==True:
                                    if min+add>0:
                                          muzesDalsi=False
                                          add-=1
                        else:
                              pygame.draw.polygon(display, (0,200,0), [[125,470],[175,470],[150,420]])
            # - První Bojovník (aktivní Hráč)


                  pygame.draw.rect(display,BLACK,(700,0,9999,9999))
                  display.blit(font3.render(jmeno,True,WHITE),(710,10))
            
                  for i in seznamHracu[pomSez[0]].getToAttack():
                        display.blit(font3.render(str(i),True,WHITE),(1010,10+poz2))
                        poz2+=60
            elif naTahu==2:
                  pygame.draw.rect(display,BLACK,(700,0,9999,9999))
                  if mouse[0] > 710 and mouse[0] < 960 and mouse[1] > 480 and mouse[1] < 530:
                        pygame.draw.rect(display,(0,0,255),(710,480,250,50))
                        if event.type == MOUSEBUTTONDOWN:
                              if seznamHracu[pomSez[0]].zivoty[0]+5<=seznamHracu[pomSez[0]].zivoty[1]:
                                    seznamHracu[pomSez[0]].zivoty[0]+=5
                              else:
                                    seznamHracu[pomSez[0]].zivoty[0]=seznamHracu[pomSez[0]].zivoty[1]
                              if seznamHracu[pomSez[0]].mana[0]+10<=seznamHracu[pomSez[0]].mana[1]:
                                    seznamHracu[pomSez[0]].mana[0]+=10
                              else:
                                    seznamHracu[pomSez[0]].mana[0]=seznamHracu[pomSez[0]].mana[1]
                              testVlastnosti(pomSez[0])
                              naTahu=1
                  else:
                        pygame.draw.rect(display,(0,0,200),(710,480,250,50))
                  display.blit(font3.render("Pass",True,WHITE),(800,480))
                  if mouse[0] > 970 and mouse[0] < 1220 and mouse[1] > 480 and mouse[1] < 530:
                        pygame.draw.rect(display,(0,0,255),(970,480,250,50))
                        if event.type == MOUSEBUTTONDOWN:
                              a=randint(0,len(seznamMest)-1)
                              seznamHracu[cisloHrace].penize+=seznamHracu[pomSez[0]].penize
                              seznamHracu[pomSez[0]].penize=0
                              seznamHracu[pomSez[0]].y=seznamMest[a].sourednice[0]*11+10
                              seznamHracu[pomSez[0]].x=seznamMest[a].sourednice[1]*11+10
                              zacatekHry()  
                              nextPlayer()
                  else:
                        pygame.draw.rect(display,(0,0,200),(970,480,250,50))
                  display.blit(font3.render("Surrender",True,WHITE),(1010,480))
                  display.blit(font3.render(jmeno,True,WHITE),(710,10))
            
                  for i in seznamHracu[pomSez[0]].getToAttack():
                        display.blit(font3.render(str(i),True,WHITE),(1010,10+poz2))
                        poz2+=60
                  poz2=0
                  if len(seznamHracu[pomSez[0]].attack())<8:
                        for i in range(len(seznamHracu[pomSez[0]].attack())):
                              pomText=str(seznamHracu[pomSez[0]].attack()[i][0])
                              if mouse[0] > 710 and mouse[0] < 960 and mouse[1] > 60+poz2 and mouse[1] < 110+poz2:
                                    pygame.draw.rect(display,(0,0,255),(710,60+poz2,250,50))
                                    pygame.draw.rect(display,(20,20,20),(710,550,650,200))
                                    display.blit(font3.render(pomText,True,WHITE),(710,550))
                                    display.blit(font3.render(popisky[pomText][0],True,WHITE),(710,600))
                                    display.blit(font3.render(popisky[pomText][1],True,WHITE),(710,650))
                                    if event.type == MOUSEBUTTONUP and muzesDalsi==False:
                                          muzesDalsi=True
                                    if event.type == MOUSEBUTTONDOWN and muzesDalsi==True:
                                          muzesDalsi=False
                                          if seznamHracu[pomSez[0]].mana[0]+seznamHracu[pomSez[0]].attack()[i][2]>=0:
                                                if randint(1,20)>10-seznamHracu[pomSez[0]].attackBonus:
                                                      seznamHracu[cisloHrace].zivoty[0]+=seznamHracu[pomSez[0]].attack()[i][1]
                                                seznamHracu[pomSez[0]].mana[0]+=seznamHracu[pomSez[0]].attack()[i][2]
                                                naTahu=1
                              else:
                                    pygame.draw.rect(display,(0,0,200),(710,60+poz2,250,50))
                              display.blit(font3.render(pomText,True,WHITE),(710,60+poz2))
                              poz2+=60
                  else:
                        for i in range(len(seznamHracu[pomSez[0]].attack())):
                              if i>=min+add2 and i<max+add2:
                                    pomText=str(seznamHracu[pomSez[0]].attack()[i][0])
                                    if mouse[0] > 710 and mouse[0] < 960 and mouse[1] > 60+poz2 and mouse[1] < 110+poz2:
                                          pygame.draw.rect(display,(0,0,255),(710,60+poz2,250,50))
                                          pygame.draw.rect(display,(20,20,20),(710,550,650,200))
                                          display.blit(font3.render(pomText,True,WHITE),(710,550))
                                          display.blit(font3.render(popisky[pomText][0],True,WHITE),(710,600))
                                          display.blit(font3.render(popisky[pomText][1],True,WHITE),(710,650))
                                          if event.type == MOUSEBUTTONUP and muzesDalsi==False:
                                                muzesDalsi=True
                                          if event.type == MOUSEBUTTONDOWN and muzesDalsi==True:
                                                muzesDalsi=False
                                                if seznamHracu[pomSez[0]].mana[0]+seznamHracu[pomSez[0]].attack()[i][2]>=0:
                                                      if randint(1,20)>10-seznamHracu[pomSez[0]].attackBonus:
                                                            seznamHracu[cisloHrace].zivoty[0]+=seznamHracu[pomSez[0]].attack()[i][1]
                                                      seznamHracu[pomSez[0]].mana[0]+=seznamHracu[pomSez[0]].attack()[i][2]
                                                      naTahu=1
                                    else:
                                          pygame.draw.rect(display,(0,0,200),(710,60+poz2,250,50))
                                    display.blit(font3.render(pomText,True,WHITE),(710,60+poz2))
                                    poz2+=60
                        if mouse[0] >775 and mouse[0] <825 and mouse[1] > 420 and mouse[1] < 470:
                              pygame.draw.polygon(display, (0,255,0), [[775,420],[825,420],[800,470]])
                              if event.type == MOUSEBUTTONUP and muzesDalsi==False:
                                    muzesDalsi=True
                              if event.type == MOUSEBUTTONDOWN and muzesDalsi==True:
                                    if max+add2<len(seznamHracu[pomSez[0]].attack()):
                                          muzesDalsi=False
                                          add2+=1
                        else:
                              pygame.draw.polygon(display, (0,200,0), [[775,420],[825,420],[800,470]])
                        if mouse[0] > 835 and mouse[0] < 885 and mouse[1] > 420 and mouse[1] < 470:
                              pygame.draw.polygon(display, (0,255,0), [[835,470],[885,470],[860,420]])
                              if event.type == MOUSEBUTTONUP and muzesDalsi==False:
                                    muzesDalsi=True
                              if event.type == MOUSEBUTTONDOWN and muzesDalsi==True:
                                    if min+add2>0:
                                          muzesDalsi=False
                                          add2-=1
                        else:
                              pygame.draw.polygon(display, (0,200,0), [[835,470],[885,470],[860,420]])      
            # - Druhý bojovník (Hráč, kterého si aktivní hráč vybral)
      elif hraZacala=="EditPlayer":
            if HracNaEditaci==True:
                  poz=0
                  for i in seznamHracu:
                        if mouse[0] > 100 and mouse[0] < 400 and mouse[1] > 10+poz and mouse[1] < 70+poz:
                              pygame.draw.rect(display, (0,255,0), (100,10+poz,300,50))
                              if event.type == MOUSEBUTTONUP and muzesDalsi==False:
                                    muzesDalsi=True
                              if event.type == MOUSEBUTTONDOWN and muzesDalsi==True:
                                    muzesDalsi=False
                                    HracNaEditaci=i
                        else:
                              pygame.draw.rect(display, (0,200,0), (100,10+poz,300,50))
                        display.blit(font3.render(i.jmeno,True,WHITE),(105,10+poz))
                        poz+=60
            else:
                  display.blit(font3.render(HracNaEditaci.jmeno,True,WHITE),(105,10))
                  display.blit(font3.render(str(HracNaEditaci.zivoty[0])+"/"+str(HracNaEditaci.zivoty[1]),True,WHITE),(105,70))
                  display.blit(font3.render(str(HracNaEditaci.mana[0])+"/"+str(HracNaEditaci.mana[1]),True,WHITE),(105,120))
                  display.blit(font3.render(HracNaEditaci.jmeno,True,WHITE),(105,10))
      else:
            # Souboj S Boty
            pomProm=""
            poz=0
            poz2=0
            display.blit(font3.render(seznamHracu[cisloHrace].jmeno,True,WHITE),(10,10))
            for i in hraZacala:
                  if i!="B":
                        pomProm+=i
            NPC=int(pomProm)
            jmeno=seznamNPC[NPC].jmeno
            for i in seznamHracu[cisloHrace].getToAttack():
                  display.blit(font3.render(str(i),True,WHITE),(300,10+poz))
                  poz+=60
            poz=0
            if seznamNPC[NPC].zivoty[0]<=0 or seznamHracu[cisloHrace].zivoty[0]<=0:
                  if seznamHracu[cisloHrace].zivoty[0]<=0:
                        x=0
                        y=0
                  else:
                        seznamNPC[NPC].zivoty[0]=seznamNPC[NPC].zivoty[1]
                        seznamNPC[NPC].mana[0]=seznamNPC[NPC].mana[1]
                        seznamHracu[cisloHrace].testMise(1)
                  naTahu=1
                  nextPlayer()
                  zacatekHry()
            if naTahu==1:
                  if mouse[0] > 10 and mouse[0] < 260 and mouse[1] > 480 and mouse[1] < 530:
                        pygame.draw.rect(display,(0,0,255),(10,480,250,50))
                        if event.type == MOUSEBUTTONDOWN:
                              if seznamHracu[cisloHrace].zivoty[0]+5<=seznamHracu[cisloHrace].zivoty[1]:
                                    seznamHracu[cisloHrace].zivoty[0]+=5
                              else:
                                    seznamHracu[cisloHrace].zivoty[0]=seznamHracu[cisloHrace].zivoty[1]
                              if seznamHracu[cisloHrace].mana[0]+10<=seznamHracu[cisloHrace].mana[1]:
                                    seznamHracu[cisloHrace].mana[0]+=10
                              else:
                                    seznamHracu[cisloHrace].mana[0]=seznamHracu[cisloHrace].mana[1]
                              testVlastnosti(cisloHrace)
                              naTahu=2
                  else:
                        pygame.draw.rect(display,(0,0,200),(10,480,250,50))
                  display.blit(font3.render("Pass",True,WHITE),(100,480))
                  if mouse[0] > 270 and mouse[0] < 520 and mouse[1] > 480 and mouse[1] < 530:
                        pygame.draw.rect(display,(0,0,255),(270,480,250,50))
                        if event.type == MOUSEBUTTONDOWN:
                              a=randint(0,len(seznamMest)-1)
                              seznamHracu[cisloHrace].penize=0
                              y=seznamMest[a].sourednice[0]*11+10
                              x=seznamMest[a].sourednice[1]*11+10
                              zacatekHry()  
                              nextPlayer()
                  else:
                        pygame.draw.rect(display,(0,0,200),(270,480,250,50))
                  display.blit(font3.render("Surrender",True,WHITE),(310,480))
                  if len(seznamHracu[cisloHrace].attack())<8:
                        for i in seznamHracu[cisloHrace].attack():
                              pomText=str(i[0])
                              if mouse[0] > 10 and mouse[0] < 260 and mouse[1] > 60+poz and mouse[1] < 110+poz:
                                    pygame.draw.rect(display,(0,0,255),(10,60+poz,250,50))
                                    pygame.draw.rect(display,(20,20,20),(10,550,650,200))
                                    display.blit(font3.render(pomText,True,WHITE),(10,550))
                                    display.blit(font3.render(popisky[pomText][0],True,WHITE),(10,600))
                                    display.blit(font3.render(popisky[pomText][1],True,WHITE),(10,650))
                                    if event.type == MOUSEBUTTONUP and muzesDalsi==False:
                                          muzesDalsi=True
                                    if event.type == MOUSEBUTTONDOWN and muzesDalsi==True:
                                          muzesDalsi=False
                                          if seznamHracu[cisloHrace].mana[0]+i[2]>=0:
                                                if randint(1,20)>10-seznamHracu[cisloHrace].attackBonus:
                                                      seznamNPC[NPC].zivoty[0]+=i[1]
                                                seznamHracu[cisloHrace].mana[0]+=i[2]
                                                naTahu=2
                              else:
                                    pygame.draw.rect(display,(0,0,200),(10,60+poz,250,50))
                              display.blit(font3.render(pomText,True,WHITE),(10,60+poz))
                              poz+=60

                  else:
                        for i in range(len(seznamHracu[cisloHrace].attack())):
                              if i>=min+add and i<max+add:
                                    pomText=str(seznamHracu[cisloHrace].attack()[i][0])
                                    if mouse[0] > 10 and mouse[0] < 260 and mouse[1] > 60+poz and mouse[1] < 110+poz:
                                          pygame.draw.rect(display,(0,0,255),(10,60+poz,250,50))
                                          pygame.draw.rect(display,(20,20,20),(10,550,650,200))
                                          display.blit(font3.render(pomText,True,WHITE),(10,550))
                                          display.blit(font3.render(popisky[pomText][0],True,WHITE),(10,600))
                                          display.blit(font3.render(popisky[pomText][1],True,WHITE),(10,650))
                                          if event.type == MOUSEBUTTONUP and muzesDalsi==False:
                                                muzesDalsi=True
                                          if event.type == MOUSEBUTTONDOWN and muzesDalsi==True:
                                                muzesDalsi=False
                                                if seznamHracu[cisloHrace].mana[0]+seznamHracu[cisloHrace].attack()[i][2]>=0:
                                                      if randint(1,20)>10-seznamHracu[cisloHrace].attackBonus:
                                                            seznamNPC[NPC].zivoty[0]+=seznamHracu[cisloHrace].attack()[i][1]
                                                      seznamHracu[cisloHrace].mana[0]+=seznamHracu[cisloHrace].attack()[i][2]
                                                      naTahu=2
                                    else:
                                          pygame.draw.rect(display,(0,0,200),(10,60+poz,250,50))
                                    display.blit(font3.render(pomText,True,WHITE),(10,60+poz))
                                    poz+=60
                        if mouse[0] > 65 and mouse[0] < 115 and mouse[1] > 420 and mouse[1] < 470:
                              pygame.draw.polygon(display, (0,255,0), [[ 65,420],[115,420],[ 90,470]])
                              if event.type == MOUSEBUTTONUP and muzesDalsi==False:
                                    muzesDalsi=True
                              if event.type == MOUSEBUTTONDOWN and muzesDalsi==True:
                                    if max+add<len(seznamHracu[cisloHrace].attack()):
                                          muzesDalsi=False
                                          add+=1
                        else:
                              pygame.draw.polygon(display, (0,200,0), [[ 65,420],[115,420],[ 90,470]])
                        if mouse[0] > 125 and mouse[0] < 175 and mouse[1] > 420 and mouse[1] < 470:
                              pygame.draw.polygon(display, (0,255,0), [[125,470],[175,470],[150,420]])
                              if event.type == MOUSEBUTTONUP and muzesDalsi==False:
                                    muzesDalsi=True
                              if event.type == MOUSEBUTTONDOWN and muzesDalsi==True:
                                    if min+add>0:
                                          muzesDalsi=False
                                          add-=1
                        else:
                              pygame.draw.polygon(display, (0,200,0), [[125,470],[175,470],[150,420]])
                  
                  pygame.draw.rect(display,BLACK,(700,0,9999,9999))
                  display.blit(font3.render(jmeno,True,WHITE),(710,10))
            
                  for i in seznamNPC[NPC].getToAttack():
                        display.blit(font3.render(str(i),True,WHITE),(1010,10+poz2))
                        poz2+=60
            # - První Bojovník (aktivní Hráč)
            else:
                  if seznamNPC[NPC].zivoty[0]+500<=seznamNPC[NPC].zivoty[1] and seznamNPC[NPC].mana[0]>=200 and NPC in [3]:
                        seznamNPC[NPC].zivoty[0]+=500
                        seznamNPC[NPC].mana[0]-=200
                  elif seznamNPC[NPC].mana[0]>=20 and NPC in [3]:
                        seznamNPC[NPC].mana[0]-=20
                        if randint(1,20)>5: 
                              seznamHracu[cisloHrace].zivoty[0]-=30
                  elif seznamNPC[NPC].mana[0]>=10 and NPC in [1,2,3]:
                        seznamNPC[NPC].mana[0]-=10
                        if randint(1,20)>5:
                              seznamHracu[cisloHrace].zivoty[0]-=20
                  elif seznamNPC[NPC].zivoty[0]<999999 and NPC==4:
                        seznamHracu[cisloHrace].zivoty[0]-=100000
                  else:
                        if randint(1,20)>5: 
                              seznamHracu[cisloHrace].zivoty[0]-=10
                  naTahu=1
      pygame.display.update()
      clock.tick(FPS)
      ulozVse()