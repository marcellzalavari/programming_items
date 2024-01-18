# A feltételnek megfelelő elemeket átpakolja egy másik listába.
# 3-mal osztahtó számok

from random import randint
szamok=[]
for i in range(100):
    szamok.append(randint(-100,100))
print(szamok)

# kiválogatás
harommal_osztato_szamok=[]
for szam in szamok:
    if szam%3==0:
        harommal_osztato_szamok.append(szam)
        
print(f'Hárommal osztható számok:\n{harommal_osztato_szamok}')