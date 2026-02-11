'''zbior = {5, 6, 6, 1, 1, 5, 9}
print(zbior)

zbior2 = {'kot', 'pies', 'gołąb', 'kot', 'pies'}
print(len(zbior2))'''

A = set(range(0,20, 2))
B = {1, 2, 3, 4, 6, 12}

#suma zbiorów
suma_A_B = A.union(B)
print(suma_A_B)

suma_A_B2 = set(list(A) + list(B))
print(suma_A_B2)

#Część wspólna
iloczyn_A_B = A.intersection(B)
print(iloczyn_A_B)

#Różnica
różnica_A_B = A.difference(B)
print(różnica_A_B)

#Dodawanie elementu do zbioru
C = {1, 7, 4, 5}
C.add(2)
print(C)