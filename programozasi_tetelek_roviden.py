#Összegzés
t = [ 3, 8, 2, 4, 5, 1, 6]
 
osszeg = 0
for num in t:
    osszeg = osszeg + num
 
print("Összeg: ", osszeg)

#Megszámolás
t = [ 3, 8, 2, 4, 5, 1, 6]
 
count = 0
for num in t:
    if num > 5:
        count = count + 1
 
print("5-nél nagyobb: ", count)

#Eldöntés
t = [ 3, 8, 2, 4, 5, 1, 6]
 
n = len(t)
ker = 5
 
i = 0
while i < n and t[i] != ker:
    i = i + 1
 
if i<n:
    print("Van ilyen: ", ker)
else:
    print("Nincs ilyen elem: ", ker)

#Keresés
t = [ 3, 8, 2, 4, 5, 1, 6]
 
n = len(t)
ker = 5
 
i = 0
while i < n and t[i] != ker:
    i = i + 1
 
if(i < n):
    print('Van ' + str(ker) + ' elem')
    print("Helye: ", i+1)
else:
    print('Nincs ' + str(ker) + ' elem!')

#Másolás
a = [ 3, 8, 2, 4, 5, 1, 6]
b = []
 
def dupla(num):
    return num * 2
 
for elem in a:
    b.append(dupla(elem))
 
print(b)

#Kiválogatás
a = [ 3, 8, 2, 4, 5, 1, 6]
b = []
 
for elem in a:
    if elem < 5:
        b.append(elem)
 
print(b)

#Szétválogatás
a = [ 3, 8, 2, 4, 5, 1, 6]
b = []
c = []
 
for elem in a:
    if elem < 5:
        b.append(elem)
    else:
        c.append(elem)
 
print(b)
print(c)

#Metszet
a = [ 5, 3, 6, 2, 1 ]
b = [ 6, 2, 7, 8, 9 ]
c = []
n = len(b)
for elem in a:
    i = 0
    while i < n and elem != b[i]:
        i+=1
    if i<n:
        c.append(elem)
 
print(c)

#Unió
a = [ 5, 3, 6, 2, 1 ]
b = [ 6, 2, 7, 8, 9 ]
 
n = len(a)
m = len(b)
 
c = a.copy()
 
for j in range(0, m):
    i=0
    while i < n and b[j] != a[i]:
        i+=1
    if i>=n:
        c.append(b[j])
 
print(c)

#Maximum kiválasztás
t = [ 5, 3, 6, 2, 1 ]
 
maxElem = t[0]
for elem in t:
    if elem > maxElem:
        maxElem = elem
print(maxElem)

#Minimum kiválasztás
t = [ 5, 3, 6, 2, 1 ]
 
minElem = t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
print(minElem)