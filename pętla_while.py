#Pętla while - przykłądy

'''liczba = 120
licznik  = 0

#W pętli while podajemy warunek TRWANIA pętli
while liczba > 0: #tak długo jak liczba jest datnia(większa od zera), pętla sie wykonuje
 liczba = liczba // 2
    licznik = licznik + 1

print(licznik)'''
'''from wejscie import liczba'''

#Zadanie 1.
'''x = input('Podaj liczbę lub q aby zakończyć: ')
licznik = 0
while x != 'q':
    liczba = int(x)
    if liczba < 2:
        licznik = licznik + 1
    x = input('Podaj liczbę lub q aby zakończyć: ')
print(licznik)'''

#Zadanie 2.

'''popr_haslo = 'informatyka'
haslo = input('Podaj hasło')
proba = 1

while haslo != popr_haslo and proba < 5:
    print('Błędne hasło, podaj raz jeszcze!')
    haslo = input('Podaj hasło')
    proba = proba + 1
if haslo == popr_haslo:
    print('Witaj w systemie :)')
else:
    print('Nie ma hasła - nie ma dostępu')'''

#Zadanie 3.

'''pętla ta będzie wykonywała się cały 
czas dopóki n jest większe lub
większe lub równe 0 sie spełni to
od n program odejmie 1 więc nowe n 
będzie o jeden mniejsze i jeśli nowe n przy 
 dzieleniu przez 2 da reszte 1 to program nie 
wypisze tej liczby w wyniku a wynik 
to będą suma wszystkich liczb które są tym 
zakresie i przy dzieleniu przez 2 nie dają reszty 2 
'''
#Zadanie 4.

'''i = 10

for x in range(i):
    if i >= 1:
        print(i)
        i -= 1'''

#Zadnaie 6.
'''from time import sleep
from random import randint

wynik1 = 0
wynik2 = 0
akcja = 0

while not ((wynik1 >= 21 or wynik2 >= 21)and abs(wynik1 - wynik2 >= 2)):
    akcja += 1
    print(f'Akcja {akcja}')
    #druzyna = int(input('Podaj nr drużyny, która wygrałą akcje'))
    druzyna = randint(1, 2)
    if druzyna ==1:
        wynik1 += 1
    else:
        wynik2 += 1
    print(f'Wynik {wynik1} : {wynik2}')
    sleep(1)

if wynik1 > wynik2:
    print('Wygrała drużyna 1')
else:
    print('Wygrałą drużyna 2')'''

#Zadanie 7.
'''liczba = int(input('Podaj liczbe'))

while liczba > 0:
    cyfra = liczba % 10
    liczba = liczba // 10
    print(cyfra, end = '')'''

#Zadanie 8.
liczba = int(input('Podaj liczbe.'))

d = 2
ile_czyn = 0

while liczba > 1:
    while liczba % d == 0:
        liczba = liczba // 
        ile_czyn += 1
    d += 1
print(ile_czyn)

#Zadnie 5.
x = 0
y = 0
r = ''

while r != 'q':
    r = input("Ruch")

    if r == 'g' and y < 9: y += 1
    elif r == 'd' and x > 0: y -= 1
    elif r == 'l' and y > 0: x -= 1
    elif r == 'q': print("Koniec"); break
    else: print("Niemożliwe"); continue

    print((x, y))
