# -*- coding: utf-8 -*-
from items import *
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
    for i in load.read():
        if i=="\n":
            if inventar != []:
                seznam.append(inventar)
            else:
                seznam.append(info)
            info=""
            inv=""
        elif i=="\"":
            pass
        elif i==",":
            inventar.append(inv)
            inv=""
        else:
            info+=i
            inv+=i
    return seznam

def ulozHrace(jmeno,rasa,typ,level,zivoty,mana,hlaska,inventar,penize):
    try:
        save=open('hraci/'+jmeno+".txt",'w')
    except:
        save=open('generování map/hraci/'+jmeno+".txt",'w')
    save.write(rasa+"\n"+typ+"\n"+str(level)+"\n"+str(zivoty[0])+"\n"+str(zivoty[1])+"\n"+str(mana[0])+"\n"+str(mana[1])+"\n\""+hlaska+"\"\n"+str(penize)+"\n")
    for i in inventar:
        save.write(str(i)+",")
    save.write("\n")
    