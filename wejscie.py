#1. wprowadzanie danych przez użytkownika do programu
from zmienne import liczba_z_przecinkiem

#1) utworzenie zmiennej
#2) na ekranie pojawia sie komunikat z inputa
#3) program sie zatrzymuje i czeka na podanie danych i zatwierdzenie tego ENTEREM
#4) po wpisanie i zatwierdzebiu ENTEREM to co wpiszemy trafia jako dtring do zmiennej
#5) i program wykonuje się dalej
imie = input('Podaj swoje imię')

liczba = int(input('Podaj liczbę'))
print (type(liczba))

liczba_z_przecinkiem = float(input('Podaj liczbę z przecinkiem'))
print(type(liczba_z_przecinkiem))

