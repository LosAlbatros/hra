from random import *
# ----------- Vypočet středů ----------    
def generate(list,topLeft=[0,0],bottomRight=[0,0]):
    if bottomRight==[0,0]:
        bottomRight=[len(list)-1,len(list[0])-1]
    
    list[topLeft[1]][(topLeft[0]+bottomRight[0])//2]=(list[topLeft[1]][topLeft[0]]+list[topLeft[1]][bottomRight[0]])//2
    # prostřední horní

    list[bottomRight[1]][(topLeft[0]+bottomRight[0])//2]=(list[bottomRight[1]][topLeft[0]]+list[bottomRight[1]][bottomRight[0]])//2 
    # prostřední spodní

    list[(topLeft[1]+bottomRight[1])//2][topLeft[0]]=(list[topLeft[1]][topLeft[0]]+list[bottomRight[1]][topLeft[0]])//2 
    # prostřední levý

    list[(topLeft[1]+bottomRight[1])//2][bottomRight[0]]=(list[topLeft[1]][bottomRight[0]]+list[bottomRight[1]][bottomRight[0]])//2
    # prostřední pravý

    return middles(list,bottomRight=bottomRight,topLeft=topLeft)
# ----------- Vypočet středu ----------    
def middles(list,topLeft,bottomRight):

    list[(topLeft[1]+bottomRight[1])//2][(topLeft[0]+bottomRight[0])//2]=(list[topLeft[1]][topLeft[0]]+list[topLeft[1]][bottomRight[0]]+list[bottomRight[1]][topLeft[0]]+list[bottomRight[1]][bottomRight[0]])//4 
    # střed

    if topLeft[0]+2>=bottomRight[0]:
        if topLeft[1]+2>=bottomRight[1]:
            return list

    list=generate(list,topLeft,[(topLeft[0]+bottomRight[0])//2,(topLeft[1]+bottomRight[1])//2]) 
    # levý horní čtverec

    list=generate(list,[(topLeft[0]+bottomRight[0])//2,(topLeft[1]+bottomRight[1])//2],bottomRight) 
    # pravý dolní čtverec

    list=generate(list,[(topLeft[0]+bottomRight[0])//2,topLeft[1]],[bottomRight[0],(topLeft[1]+bottomRight[1])//2]) 
    # pravý horní čtverec

    list=generate(list,[topLeft[0],(topLeft[1]+bottomRight[1])//2],[(topLeft[0]+bottomRight[0])//2,bottomRight[1]]) 
    # levý dolní čtverec

    return list