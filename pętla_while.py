#Pętla while - przykłądy

'''liczba = 120
licznik  = 0

#W pętli while podajemy warunek TRWANIA pętli
while liczba > 0: #tak długo jak liczba jest datnia(większa od zera), pętla sie wykonuje
 liczba = liczba // 2
    licznik = licznik + 1

print(licznik)'''

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

popr_haslo = 'informatyka'
haslo = input('Podaj hasło')
proba = 1

while haslo != popr_haslo and proba < 5:
    print('Błędne hasło, podaj raz jeszcze!')
    haslo = input('Podaj hasło')
    proba = proba + 1
if haslo == popr_haslo:
    print('Witaj w systemie :)')
else:
    print('Nie ma hasła - nie ma dostępu')

#Zadanie 3.

#pętla ta będzie wykonywała się cały 
czas dopóki n jest większe lub
równe 0 i jeżeli warunek że n jest 
większe lub równe 0 sie spełni to
od n program odejmie 1 więc nowe n 
będzie o jeden mniejsze i jeśli nowe n przy 
 dzieleniu przez 2 da reszte 1 to program nie 
wypisze tej liczby w wyniku a wynik 
to będą suma wszystkich liczb które są tym 
zakresie i przy dzieleniu przez 2 nie dają reszty 2 

#Zadanie 4.

i = 10

for x in range(i):
    if i >= 1:
        print(i)
        i -= 1
