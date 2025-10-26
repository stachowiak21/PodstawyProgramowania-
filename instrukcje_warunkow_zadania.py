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

#Zadanie 12.
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
    print('nie zdałeś!')

#Zadanie 13
ocena = int(input('Podaj ocenę z  języka obcego: '))
test = int(input('Podaj wynik z testu języka obcego: '))

if (ocena >= 5 and ocena <= 6) or (test >= 90 and test <=100):
    print('Jesteś w grupie zaawansowanej')
elif (ocena >= 1 and ocena <= 4) or (test >= 0 and test <= 89):
    print('Jesteś w grupie podstawowej')
else:
    print('Sprawdż czy wpisałeś dobre wyniki')

#Zadanie 14
a = float(input('Podaj pierwszą liczbę różną od zera: '))
b = float(input('Podaj drugą liczbę: '))
c = float(input('Podaj trzecią liczbę: '))

print('ax² + bx + c =0')

if b + c == 0:
    print('ax² = 0')
    print('x₀ = 0')
elif b == 0:
    print('x² + c =0 ')
    if (-c / a) > 0:
        print('równanie ma dwa rozwiązania: 𝑥₁ = √(-c/a) lub x₂ = -√(-c/a)')
    else:
        print('równanie bez rozwiązania (jest sprzeczne)')
elif c == 0:
    print('równanie z dwoma rozwiązaniami : x₁ = 0 lub x₂ = (-b/a)')
