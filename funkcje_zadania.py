#Zadanie 0.3

#a)

'''def suma_v(u, v):
    w = []
    for i in range(len(u)):
        suma = u[i] + v[i]
        w.append(suma)
    return w

u = [2, 7, 3]
v = [-1, 0, 4]

wynik = suma_v(u, v)

print(wynik)'''

#b)

'''def iloczyn_s(u, v):
    wynik = 0
    for i in range(len(u)):
        wynik += u[i] * v[i]
    return wynik
u = [2, 7, 3]
v = [-1, 0, 4]
wynik = iloczyn_s(u, v)
print(wynik)'''

#Zadanie 2.1
def czy_anagramy(s1, s2):
    '''if sorted(s1) == sorted(s2):
        return True
    else:
        return False'''

    '''return sorted(s1) == sorted(2)'''#Krutsza opcja

#print(czy_anagramy('nosek', 'keson'))

'''s1 = 'nosek'
s2 - 'keson'
print(sorted(s1) == sorted(s2))'''

def jaki_trojkat(a, b, c):
    if a ** 2 + b ** 2 == c ** 2 == 2 * max([a, b, c]):
        print('prostokątny')
    elif a ** 2 + b ** 2 == c ** 2 > 2 * max([a, b, c]):
        print('ostrokątny')
    elif a ** 2 + b ** 2 == c ** 2 < 2 * max([a, b, c]):
        print('rozwartokątny')

jaki_trojkat(7, 10, 1)