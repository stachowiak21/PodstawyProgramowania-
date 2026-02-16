'''zbior = set() #Pusty zbior

lista2d = [
[5, 2, 8, 5, 1],
[3, 8, 2, 9, 5],
[1, 4, 4, 2, 7],
[6, 3, 9, 1, 4],
[8, 2, 5, 6, 3]
]

for x in range(len(lista2d)):
    for y in range(len(lista2d[0])):
        element = lista2d[x][y]
        zbior.add(element)

print(zbior)

zbior_cały = set()
for x in lista2d:
    zbior2 = set(x)
    zbior_cały = zbior_cały.union(zbior2)
print(zbior_cały)'''

slowa = [
"LETTER",
"BALLOON",
"SUCCESS",
"HAPPY",
"COFFEE",
"BOOKKEEPER",
"ASSESS",
"MISSISSIPPI",
"ADDRESS",
"TOOLBOX"
]

'''slowo = 'LETTER'
slowo_zbior = set(slowo)
print(len(slowo_zbior))'''

'''for x in slowa:
    x_zboir = set(x)
    print(f'{x} {len(x_zboir)}')'''

#Sposób 1
'''max_x = ''
max_l_r_l = 0

for x in slowa:
    x_zbior = set(x)
    l_r_l = len(x_zbior)
    if l_r_l > max_l_r_l:
        max_l_r_l = l_r_l
        max_x = x
print(max_x)'''

#Sposób 2
zbior = set()

'''max_slowo = max(slowa, key = lambda x: len(set(x)))
print(max_slowo)'''

#Zadanie 2.2
for x in slowa:
    for y in x:
        zbior.add(y)

for l in zbior:
    lista = []
    for s in sorted(slowa):
        if l in s:
            lista.append(s)
    print(f'{l}: {lista}')