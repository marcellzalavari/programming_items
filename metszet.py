#Metszet: a két lista közös elemeit adjuk meg (beletesszük egy harmadik listába)
from random import randint

szamok1=[]
szamok2=[]

for i in range(20):
    szamok1.append(randint(-100,100))
    szamok2.append(randint(-100,100))
print('Szamok 1: ',szamok1 )
print('Szamok 2: ',szamok2)

# metszet
metszet=[]
for szam in szamok1: # végigmegyünk az első listán
    if szam in szamok2: #megvizsgáljuk, hogy az első lista aktuális eleme benne van-e a második listában
        metszet.append(szam)
print('Metszet: ',metszet)