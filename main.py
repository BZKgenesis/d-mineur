import datetime
import random
def check(x,y,jeu):
    nb=0
    if jeu[y-1][x] == "█":
        nb+=1
    if jeu[y-1][x-1] == "█":
        nb+=1
    if jeu[y][x-1] == "█":
        nb+=1
    if jeu[y+1][x-1] == "█":
        nb+=1
    if jeu[y+1][x] == "█":
        nb+=1
    if jeu[y+1][x+1] == "█":
        nb+=1
    if jeu[y][x+1] == "█":
        nb+=1
    if jeu[y-1][x+1] == "█":
        nb+=1
    if nb == 0:
        nb = ' '
    return nb

def créer_tableau(largeur,hauteur):
    tableau=[]
    tableau.append(["H" for i in range(largeur+2)])
    for j in range(hauteur):
        row=['H']
        for k in range(largeur):
            if random.randint(0,100)<15:
                row.append("█")
            else:
                row.append(" ")
        row.append('H')
        tableau.append(row)
    tableau.append(["H" for i in range(largeur+2)])
    return tableau
before = datetime.datetime.now()
tableau =créer_tableau(12,24)
for n in range(1,len(tableau)-1):
    for o in range(1,len(tableau[n])-1):
        if tableau[n][o] != "█":
            tableau[n][o]=str(check(o,n,tableau))
for l in range(len(tableau)):
    for m in range(len(tableau[l])):
        print(tableau[l][m],end=' ')
    print()
print(datetime.datetime.now()-before)
