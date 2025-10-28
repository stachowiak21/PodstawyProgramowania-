#Rozwiązywanie równania kwadratowego

'''a = float(input('Podaj liczbe a =/= 0'))
b = float(input('Podaj liczbe b'))
c = float(input('Podaj liczbe c'))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (-b - delta ** 0.5) / (2 * a)
    x2 = (-b + delta ** 0.5) / (2 * a)
    print(f'x1 = {x1} v x2 = {x2}')
elif delta == 0:
    x = (-b) / (2 * a)
    print('x1 = x2 = {}'.format(x))
else:
    print('brak rozwiązań')'''

'''#Zadanie 12.
pisemny_j_polski  = int(input('pisemny polski'))
pisemny_j_obcy = int(input('pisemny obcy'))
pisemny_dodatkowy = int(input('pisemny dpdatkowy'))
ustny_j_polski = int(input('ustny polski'))
ustny_j_obcy = int(input('ustny obcy'))

if pisemny_j_polski >= 30 and pisemny_j_obcy >= 30 and pisemny_dodatkowy >= 30 and ustny_j_polski >= 30 and ustny_j_obcy >= 30:
    print('zdałeś bez amnestii')
elif (pisemny_j_polski + pisemny_j_obcy + pisemny_dodatkowy + ustny_j_polski + ustny_j_obcy) / 5 >= 30:
    print('zdałeś z amnestią')
else:
    print('nie zdałeś!')'''
#Zadanie 13

'''ocena = int(input('Podaj ocenę z  języka obcego: '))
test = int(input('Podaj wynik z testu języka obcego: '))

if (ocena >= 5 and ocena <= 6) or (test >= 90 and test <=100):
    print('Jesteś w grupie zaawansowanej')
elif (ocena >= 1 and ocena <= 4) or (test >= 0 and test <= 89):
    print('Jesteś w grupie podstawowej')
else:
    print('Sprawdż czy wpisałeś dobre wyniki')
'''
'''#Zadanie 14

a = float(input('Podaj liczbę a =/= 0'))
b = float(input('Podaj liczbę b'))
c = float(input('Podaj liczbę c'))

if b == 0 and c == 0:
    print(f' wynik = 0')
if b == 0 and c != 0:
    if -c/a > 0:
        x1 = (-c/a) ** 0,5
        x2 = -(-c/a) ** 0,5
        print(f'x1 = {x1} v x2 = {x2}') 
    if -c/a < 0:
        print('Brak rozwiązań')
if c == 0 and b != 0:
    x1 = 0
    x2 = -(b)/(a)
    print(f'x1 = {x1} v x2 = {x2}')
if b != 0 and c != 0: # else
    delta = b ** 2 - 4 * a * b
    if delta > 0:
        pass
    if delta == 0:
        pass
    if delta < 0:
        if delta > 0:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            print(f'x1 = {x1} v x2 = {x2}')
        elif delta == 0:
            x = (-b) / (2 * a)
            print('x1 = x2 = {}'.format(x))
        else:
            print('brak rozwiązań')'''

