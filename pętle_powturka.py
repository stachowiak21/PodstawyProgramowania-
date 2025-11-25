lista = [10, 56, 89, 59]

#1. chodzenie bezpośrednio po elementach listy
# Do zmiennej b trafiają bezpośrednio elementy listy< tznaczy 10 56 89 59
'''for b in lista:
    print(b)'''

#2. Chodzenie po liście z użyciem indeksów
#2.1 Co to jest indeks?
#lista[2]
# 2 - indeks
# lista[2] - element znajdujący siępod danym indeksem lista[2] = 89

#2.2.
for k in range(len(lista)): #znaczy to samo co range(0, 4)
    print(lista[k])