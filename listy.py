#1)  listy a napisy

napis = 'informatyka'

#2) Zamiana napisu na listę

lista = list(napis)
print(lista)

#Zakres i lista

zakres = range(3, 10, 2)
lista2 = list(zakres)
print(lista2)

#3) Indeksowanie elementó listy

lista3 = ['osa', 99, 3.14, [5, 7, 8, 9]]
print(lista3[1:3]) #wycinanie fragmentu listy
print(lista3[3][2]) #obsługa listy zagnieżdżonej
print(lista3[3][::2]) #obsługa listy zagnieżdżonej

#4) Powielanie listy

#a) dodawanie list

lista4 = ['a' , 45, 78]
lista5 = [[4, 8], 56, 12]
lista6 = lista5 + lista4
print(lista6)

#b) dodawanie listy

lista7 = ['a' , 45, 78]
lista8 = [[4, 8], 56, 12]
lista8.extend(lista7)
print(lista8)

#"mnożenie" listy przezłiczby

lista9 =[0] * 1000
'''lista10 = [[0]* 10] * 10
print(lista10)'''

#5) Sortowanie i odwracanie listy

lista10 = [4, -1, 0, 5, 2, 9, 3]
#lista10.reverse()
#lista10.sort()
print(lista10)

#6)Wyrażenia listowe (listy składane)

lista11 = list(range(1,11))
lista11_kwadraty = [ x ** 2 for x in lista11 if x % 2 == 0 ]
print(lista11_kwadraty)

#7) Usówanie elementów listy

lista12 = [4, 7, 4, 8, 2, 1]
while 4 in lista12:
    lista12.remove(4)
print(lista12)

#8) Usuwanie elementu na bazie jego indeksu
lista13 = [5, 1, 8, 3, 9, 10]
del lista13[2]
print(lista13)