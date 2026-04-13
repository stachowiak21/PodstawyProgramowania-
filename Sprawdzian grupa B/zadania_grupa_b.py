'''plik = open('przyklad.txt')
dane = plik.readlines()

for x in range(len(dane)):
    dane[x] = dane[x].strip()
# 2.1
# for x in dane:
#     if int(x[::-1]) % 17 == 0:
#         print(x[::-1])
# 2.2
# ile różnych liczb
print(len(set(dane)))

# Ile powtarza się dwa razy
# lista = []
# for x in dane:
#     ile = dane.count(x)
#     if ile == 2:
#     lista.append(x)
# print(len(set(lista)))
licznik2 = 0
licznik3 = 0

for i in set(dane):
    if dane.count(i) == 2:
        licznik2 += 1
    elif dane.count(i) == 3:
        licznik3 += 1
print(licznik2, licznik3)'''
from os.path import split

#Zadanie 3
def t(i):
    return (i - 1) / 100

def v_sr (rk, rp, dt):
    return [(rk[0] - rp[0]) / dt, (rk[1] - rp[1]) / dt]

def szyb_sr(v_sr):
    return (v_sr[0] ** 2 + v_sr[1] ** 2)** 5

for i in range(1, len(dane)):
    rp = dane[0]
    rk = dane[i]
    czas = t(i + 1)
    pr_sr = v_sr(rk, rp, czas)
    szybkosc_sr = szyb_sr(pr_sr)
    wynik.append((czas, szybkosc_sr))

print(wynik)

