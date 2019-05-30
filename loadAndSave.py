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
    