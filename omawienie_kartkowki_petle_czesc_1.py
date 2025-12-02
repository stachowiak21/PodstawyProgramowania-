lista = [12, 45, 78, 101, 9, -5, 9, 7, 23]

#zadanie 2. gr.B
#sposób 1
'''for i in range(len(lista)):
    if i % 2 == 1:
        print(lista[i])'''

#sposób 2
'''for i  in range(1, len(lista), 2):
    print(lista[i])'''

#sposób 3
'''for i in lista[1:9:2]:
    print(i)'''

#sposób 4
'''i = 1
while i < len(lista):
    print(lista[i])
    i = i + 2'''

#Zadanie 4.
lista = [100]

for x in lista:
    liczba = float(input('Podaj liczbe'))
    print(liczba)
    if liczba != 0:
        lista.append(67)
