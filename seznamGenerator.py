try:
    n=int(input("Doplň číslo 3-6\n   +1\r2^"))
    if n>6:
        n=6
    if n<3:
        n=3
except:
    n=3
a=2**n+1
d=[]
while len(d)!=4:
    d=[]
    b=input("zadej rohy oddělené mezerou (LevýHorní PravýHorní LevýDolní PravýDolní)")
    c=""
    for i in b:
        if i==" ":
            d.append(c)
            c=""
        else:
            c+=i
    d.append(c)
seznam=[]
seznam2=[]
for i in range(a):
    for j in range(a):
        seznam2.append(0)
    seznam.append(seznam2)
    seznam2=[]
seznam[0][0]=d[0]
seznam[0][-1]=d[1]
seznam[-1][0]=d[2]
seznam[-1][-1]=d[3]
try:
    load=open('seznam.txt','r',encoding='utf8')
    save=open('seznam.txt',mode='w',encoding='utf8')
    load.close()
except:
    save=open('generování map/seznam.txt',mode='w',encoding='utf8')
print("Načítaní souboru pokus 2")
print("Ukládání",end=" ")
x=0
for i in seznam:
    for j in i:
        save.write(str(j)+" ")
        x+=1
        print("\rUkládání "+str(x/((len(seznam)*len(seznam))/100))+" %     ",end=" ")
    save.write("\n")