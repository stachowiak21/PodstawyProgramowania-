#Tabliczka mnożenia do 100
'''for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end = '\t')
    print()'''
from asyncio import get_child_watcher

#Trójkąt prostokątny

#sposób 1
'''n = int(input('Podaj wysokość'))

for x in range(n):
    for y in range(x + 1):
        print('*', end = ' ')
    print()'''

#sposób 2
'''n = int(input('Podaj wysokość'))
for x in range(n):
     print('*'*(x + 1))'''

#Trójkąt równoramienny dowolny
n = int(input("wysokość trójkąta = "))
spacje = n - 1
gwiazdki = 1

for i in range(n):
    print('' * spacje, end = '')
    print('*' * gwiazdki)
    spacje = spacje - 1
    gwiazdki = gwiazdki + 2

