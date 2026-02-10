'''#Zadanie. 1
lista1 = [12, -9, 6, 2, 8, 1, 15, -7, 0, 1, 1, 2, 2, -7, 2, 1, -7, 2]
lista2 = [['pies', 'wilk'], ['kot domowy', 'tygrys', 'lew'], 'kapibara', 'mrówka', ['rekin', 'śledź', 'pstrąg']]

#a)
print(lista2[1][2])

#b)
mrowka = list(lista2[3])
print(mrowka[2])

#odwrotnie

slowo = ''.join(mrowka)
print(slowo)

#c)
lista3 = lista1[2::2]
print(lista3)'''

#d)
'''lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_a.append(lista_b)
print(lista_a)'''
'''lista2.append(lista2[1] * 3)
print(lista2)

#e)
lista1 = lista1 + [9, 6, 16, -8, 7]
print(lista1)
'''
#f)

#sposob 1.

#lista1.sort()
'''lista1_posortowana = sorted(lista1)
print(lista1_posortowana[0], lista1_posortowana[-1])

#sposob 2.

print(min(lista1))
print(max(lista1))'''

#g)
'''del  lista1[4]
print(lista1)'''

#h)
'''del lista1[4:9]
print(lista1)'''

#i)
'''while 2 in lista1:
    lista1.remove(2)

print(lista1)'''

#drugi sposób

'''lista1 = [x for x in lista1 if x != 2]

print(lista1)

#j)
lista3 = [x ** 2 for x in lista1 ]
lista3 = []
for x in lista1:
    lista3.append(x ** 2)
print(lista3)
'''
#Zadanie 2
'''lista4 = [178, 192, 184, 182, 180, 179, 186, 190, 191, 191]

x_max = max(lista4)
x_min = min(lista4)

lista_norm = [(x - x_min) / (x_max - x_min) for x in lista4]
print(lista_norm)'''

'''#Zadanie 3
lista5 = [123, 89, 5600, 432, 11, 45, 900, 12450, 1410, 390, 9999]
lista5 = [x for x in lista5 if x < 1000 or x > 9999]
lista5 = [x for x in lista5 if not (x > 1000 and x <= 9999)]
print(lista5)''' 

#Zadanie 8.
'''lista = [1, 5, 1, 2, 2, 1, 6, 7, 3, 2, 2, 1, 1, 4]

zbior = []
for liczba in lista:
    if liczba not in zbior:
        zbior.append(liczba)

print(zbior)

for unikalna in zbior:
    ile = 0
    for liczba in lista:
        if liczba == unikalna:
            ile = ile + 1
    print(unikalna, ":", ile)'''

#Zadanie 9.
'''plecak = [
    ("książka", 1.2),
    ("zeszyt", 0.5),
    ("laptop", 2.5),
    ("piórnik", 0.3),
    ("butelka z wodą", 1.0),
    ("strój sportowy", 1.8)
]

a = []
b = []
c = 0
d = []

for x in plecak:
    if x[1] < 1.0:
        a.append(x[0])

    b.append(x[1] * 1.1)

    if x[1] > 1.5:
        c =  + 1

    if x[1] <= 1.5 in len(x[0]) > 5:
        d.append(x[0])

print(a)
print(b)
print(c)
print(d)'''

#Zadanie 10.

#Program 1. Nie wiem

#Program 2. Program wyświetli słowo False, ponieważ funkcja all sprawdza, czy wszystkie liczby są parzyste, a na liście znajdują się też liczby nieparzyste.

#Program 3. Efektem będzie lista, która na samym końcu ma dodaną drugą listę jako jeden, wspólny element (czyli mamy listę wewnątrz listy).

#Program 4. Efektem będzie jedna, długa lista, do której po prostu dopisano (doklejono) liczby 9, 10 i 11 jako osobne elementy.
