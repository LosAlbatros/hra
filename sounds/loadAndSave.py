# -*- coding: utf-8 -*-
from items import *
from mise import *
def nactiJmenaHrace():
    try:
        load=open('data/jmenaHracu.txt')
    except:
        load=open('generování map/data/jmenaHracu.txt')
    list=[]
    pomProm=""
    for i in load.read():
        if i=="\n":
            list.append(pomProm)
            pomProm=""
        else: 
            pomProm+=i
    return list


def ulozJmenaHracu(jmenaHracu):
    try:
        save=open('data/jmenaHracu.txt','w')
    except:
        save=open('generování map/data/jmenaHracu.txt','w')
    for i in jmenaHracu:
        save.write(i+"\n")

def nactiHrace(jmenoHrace):
    try:
        load=open('hraci/'+jmenoHrace+".txt",'r')
    except:
        load=open('generování map/hraci/'+jmenoHrace+".txt",'r')
    info=""
    seznam=[]
    inventar=[]
    inv=""
    equipped=[]
    equip=""
    equippedType=[]
    eType=""
    bonus=[]
    bon=""
    for i in load.read():
        if i=="\n":
            if inventar != []:
                seznam.append(inventar)
                inventar=[]
            elif equipped != []:
                seznam.append(equipped)
                equipped=[]
            elif equippedType != []:
                seznam.append(equippedType)
                equippedType=[]
            elif bonus != []:
                seznam.append(bonus)
                bonus=[]
            else:
                seznam.append(info)
            info=""
            inv=""
            equip=""
            eType=""
            bon=""
        elif i=="\"":
            pass
        elif i==",":
            inventar.append(inv)
            inv=""
        elif i=="*":
            equipped.append(equip)
            equip=""
        elif i==";":
            equippedType.append(eType)
            eType=""
        elif i=="%":
            bonus.append(bon)
            bon=""
        else:
            info+=i
            inv+=i
            equip+=i
            eType+=i
            bon+=i
    return seznam

def ulozHrace(jmeno,rasa,typ,level,zivoty,mana,hlaska,inventar,penize,equipped,equippedType,attackBonus,bonus):
    try:
        save=open('hraci/'+jmeno+".txt",'w')
    except:
        save=open('generování map/hraci/'+jmeno+".txt",'w')
    save.write(rasa+"\n"+typ+"\n"+str(level)+"\n"+str(zivoty[0])+"\n"+str(zivoty[1])+"\n"+str(mana[0])+"\n"+str(mana[1])+"\n\""+hlaska+"\"\n"+str(penize)+"\n"+str(attackBonus)+"\n")
    for i in inventar:
        save.write(str(i)+",")
    save.write("\n")
    for i in equipped:
        save.write(str(i)+"*")
    save.write("\n")
    for i in equippedType:
        save.write(str(i[0])+";")
    save.write("\n")
    for i in bonus:
        save.write(str(i)+"%")
    save.write("\n")
    

def nactiJmenaNPC():
    try:
        load=open('data/jmenaNPC.txt')
    except:
        load=open('generování map/data/jmenaNPC.txt')
    list=[]
    pomProm=""
    for i in load.read():
        if i=="\n":
            list.append(pomProm)
            pomProm=""
        else: 
            pomProm+=i
    return list

def nactiNPC(jmenoNPC):
    try:
        load=open('NPC/'+jmenoNPC+".txt",'r')
    except:
        load=open('generování map/NPC/'+jmenoNPC+".txt",'r')
    info=""
    seznam=[]
    for i in load.read():
        if i=="\n":
            seznam.append(info)
            info=""
        else:
            info+=i
    return seznam