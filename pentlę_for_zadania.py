#Zadanie 15
'''X = list(range(3, 103, 3))'''
from statistics import median_grouped

'''print(f'x\ty')
for x in X:
    y= 0.5 * x + 3
    #print(x, y)
    print(f'{x}\t{y}')'''

#b)

'''print(f'x\ty')
for x in range(-30, 61):
    x = x / 10
    y= 0.5 * x + 3
    if x >= 0:
        print(f'{x}\t\t{y}')
else:
    print(f'{x}\t{y}')'''

#Zadanie 16

'''lista1 = list(range(3, 31, 3))
lista2 = list(range(11, 111, 11))
lista3 = list(range(13, 131, 13))'''

#Sposoby na chodzenie po listach

#sposób 1
'''for x, y, z in zip(lista3,lista2,lista1):
    print(f'{x}\t{y}\t{z}')'''

#sposób 2
'''for  i in range(10):
    print(f'{lista1[i]}\t{lista2[i]}\t{lista3[i]}')
'''
#Zadanie 17
n = int(input('Podaj ile będzie liczb'))
suma = 0

for x in range(n):
    liczba = int(input('Podaj liczbe'))
    suma = suma + liczba

print(suma)