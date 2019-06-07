missionInfo={0:[3,"Bring a Little Boat here","price:100 money, 10xp"],
             1:[5,"Pirate Level:1","Lives:100/100 Mana:0/0","Move: -10 hp","price:100 money, 20xp"],
             2:[5,"Knight Level:3","Lives:200/200 Mana:10/10","Move: -10 hp, -20 hp -10 mana","price:100 money, 150xp"],
             3:[5,"Shooter Level:5","Lives:240/240 Mana:40/40","Move: -10 hp, -20 hp -10 mana","price:500 money, 300xp"],
             4:[6,"Morgan Level:10","Lives:800/800 Mana:1000/1000","Move: -10 hp, -30 hp -20 mana,","+500 hp -200 mana","price:1000 money, 500xp"],
             5:[3,"Bring a Sword Here","price:200 money, 200xp"],
             6:[6,"Albatros Level:20","Lives:999999/999999","Mana:999999/999999","Move: -10 hp, -100 000 hp","price:1000000 money, 15000xp"]
             }
nazvyMisi=["Bring Little Boat to ",
           "Duel with Pirate",
           "Duel with Knight",
           "Duel with Shooter",
           "Duel with Morgan",
           "Take Sword to ",
           "Duel with Albatros"
           ]
def mise(cisloMise,Hrac,Mesto):
    if Mesto==[True]:
        if cisloMise==1:
            Hrac.penize+=100
            Hrac.level+=20
            Hrac.mise=[]
            return True
        elif cisloMise==2:
            Hrac.penize+=100
            Hrac.level+=150
            Hrac.mise=[]
            return True
        elif cisloMise==3:
            Hrac.penize+=500
            Hrac.level+=300
            Hrac.mise=[]
            return True
        elif cisloMise==4:
            Hrac.penize+=1000
            Hrac.level+=500
            Hrac.mise=[]
            return True
        elif cisloMise==6:
            Hrac.penize+=1000000
            Hrac.level+=15000
            Hrac.mise=[]
            return True
    elif cisloMise==0:
        if Mesto==[Hrac.y//11,Hrac.x//11] and 0 in Hrac.inventar:
            Hrac.penize+=100
            Hrac.level+=10
            Hrac.mise=[]
            pomProm=1
            pomSez=[]
            for i in Hrac.inventar:
                if pomProm==1 and i==0:
                    pomProm=0
                else:
                    pomSez.append(i)
            Hrac.inventar=pomSez
            return True
    elif cisloMise==5:
        if Mesto==[Hrac.y//11,Hrac.x//11] and 9 in Hrac.inventar:
            Hrac.penize+=200
            Hrac.level+=200
            Hrac.mise=[]
            pomProm=1
            pomSez=[]
            for i in Hrac.inventar:
                if pomProm==1 and i==9:
                    pomProm=0
                else:
                    pomSez.append(i)
            Hrac.inventar=pomSez
            return True
    elif cisloMise==1:
        return "B0"
    elif cisloMise==2:
        return "B1"
    elif cisloMise==3:
        return "B2"
    elif cisloMise==4:
        return "B3"
    elif cisloMise==6:
        return "B4"
    
