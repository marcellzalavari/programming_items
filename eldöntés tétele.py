# Döntsük el, hogy van-e valamilyen feltételnek megfelelő elem a listában.
# Válasz: Igen/nem
# A keresést ne folytassa, ha a választ meg tudja adni!

# Van-e 13-mal osztahtó elem a listában?

szamok=[11,26,33,12,3]
print(szamok)

# V1:
# Hivatalos algoritmus. (minden programozási nyelven megvalósítható)
index=0 # mivel while ciklus nincs ciklusváltozó, nekünk kell lépkedni az indexeken
while (index<len(szamok) and (szamok[index]%13!=0)):
 # while feltétele: index kisebb mint az elemszám és az aktuális elem NEM felel meg a feltételnek
    index+=1
if index==len(szamok):
    print('Nincs 13-mal osztható elem a listában!')
else:
     print('Van 13-mal osztható elem a listában!')

#V2:
# python specifikus megoldás.
for szam in szamok:
    if szam%13==0:
        print('Van 13-mal osztható elem a listában!')
        break # az első teljesüléskor kiugrik a ciklusból
else: # else ágba akkor megy bele, ha a for-ban nem volt break
    print('Nincs 13-mal osztható elem a listában!')

#V3:
# Később saját függvénnyel.