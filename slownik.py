oceny = {'matematyka': 3, 'fizyka': 2, 'język polski': 4}

#kluczami sąmatematyka , fizyka , j.polskie
# A wartościami są 3, 2 ,4

#1. Dostawanie się do wartości pod danym kluczem
print(oceny['fizyka']) # Pobieramy wartość przypisanądo klucza 'fizyka, czyli 2

#2. Modyfikacja wartości pod anym kluczem
oceny['język polski'] = 5
print(oceny['język polski'])

#3. Dodawanie klucza do słownika
oceny['geografia'] = 6
print(oceny)

#4. Sklejanie słownika z listy kluczy i listy warstości
klucze = ['Bitwa pod Grunwaldem', 'Chrzest Polski', 'III Rozbior Polski']
wartosci = [1410, 966, 1795]
slownik = {}
for i in range(len(klucze)):
    #print(klucze[i], wartosci[i])
    slownik[klucze[i]] = wartosci[i]
    print(slownik)

slownik2 = dict(zip(klucze, wartosci))
print(slownik2)

slownik3 = dict(janusz = 23, alojzy = 99, bronislawa = 67)
print(slownik3)

#5. Usuwanie klcza ze słownika
del oceny['fizyka']
print(oceny)

#6. Chodzenie w pętli po słowniku
for k in oceny:
    print(k, oceny[k])

for i in oceny.items():
    print(i)