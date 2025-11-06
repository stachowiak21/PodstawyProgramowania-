from os.path import split

from zmienne import napis, slownik

#I. Fragment tekstu:
#1) wycinanie od ... do

'''print(napis[2:5]) #czyli tak naprawdę od 2 do 4

#2) wycinanie od ... do co ileś
print(napis[2:10:2])

#3) wycinanie od początku
print(napis[:3])

#4) wycinaie do końca
print(napis[7:])

#5) czytanie od końca
print(napis[::-1])

#II. Zawieranie sie znaku w słowie
if 'a' in napis:
    print('należy')
else:
    print('nie należy')

#III. Lączenie napisó (konkatencja)
napis2 = napis + 'jestnajlepsza'
print(napis2)'''

#IV. Fonkcje zmiennych typu streing

#1) poszukiwanie danego fragmentu w tekście
'''napis3 = 'matematyka'
index_gdzie_jest = napis3.find('tem')
print(index_gdzie_jest)

napis4 = 'alabalalalabala'
index_gdzie_jest2 = napis4.find('bala')
index_gdzie_jest3 = napis4.find('bala', index_gdzie_jest2 + 1 )
index_gdzie_jest4 = napis4.find('xyz', index_gdzie_jest2 + 1 )
print(index_gdzie_jest2)
print(index_gdzie_jest3)
print(index_gdzie_jest4)

if napis4.find('xyz') != -1:
    print('Jest w napisie')
else:
    print('Nie ma w napisie')'''

#2) Dzielenie napisu na fragmenty
'''piec_liczb = input('Podaj pięć liczb. Oddziel je przecinkiem.')
piec_liczb_po_podziale = piec_liczb.split(',')
print(piec_liczb_po_podziale)
trzecia_liczba = int(piec_liczb_po_podziale[2])
print(trzecia_liczba + 33)'''

#3) Lączenie napisów
'''lasta_napisow = ['Windows' , 'jest' , 'dla' , 'kasy']
cale_zdanie = '$'.join(lasta_napisow)
print(cale_zdanie)

lista_napisow2 = ['abc', 'xyz', 'bbc', 'tvn']
cale_zdanie2 = '\n'.join(lista_napisow2)
print(cale_zdanie2)
'''
#4) Zliczenie danego znaku w tekście
'''napis5 = 'prawdopodobieństwo'
ile_racy_o = napis5.count('o')
print(ile_racy_o)'''
# 5) "Mutowalność" stringow
napis6 = "fiwyka"
'''napis6[2] = 'z'
print(napis6)'''
# Wniosek: String są niemutowalne, czyli nie można podmieniać pojedyńczych liter
# Sposób na zmutowanie stringa
'''napis6_lista = list(napis6)
print(napis6_lista)
napis6_lista[2] = 'z'
print(napis6_lista)
napis6_gotowy = ''.join(napis6_lista)
print(napis6_gotowy)
#6) Długość napisu
napis7 = 'jezykpolski'
print(len(napis7))
#7) Powielanie stringa
napis8 = 'informatyka'
print(napis8 * 3)

#8) Funkcje testujące cyfry i litery
napis9 = 'qwerty'
if napis9.isalpha() == True:
    print('słowo składa sie z liter')
else:
    print('słowo nie składa sie z liter')

napis10= '1410w'
if napis10.isdigit() == True:
    print('słowo składa sie z liczb')
else:
    print('słowo nie składa sie z liczb')


napis11 = '140w\n'
if napis11.isalnum() == True:
    print('słowo składa tylko się z cyfr luv liter')
else:
    print('słowo nie składa się tylko z cyfr lib liter')
    '''

#9. KOdy ASCII
#9.1. ze znaku na kod ASCII
print(ord('A'))

#9.2 z kodu ASCII na znak
print(chr(66))

#Zagadka
print(chr(ord('Z')))

#10. Funkcja translate
slownik = str.maketrans('ąęćóżśźłń', 'aecozszln')
napis12 = 'ińfórmtyką'
napis12_poprawny = napis12.translate(slownik)
print(napis12_poprawny)

#11. Funkcja dużych i małych literek
napis13 = 'KoNgO'
napis13_tylo_duze = napis13.upper()
print(napis13_tylo_duze)

napis13_tylo_male = napis13.lower()
print(napis13_tylo_male)

#12. Podstawianie ciągu znaków
napis14 = 'Chlep kosztuje 15zł, a bułka 5 zł'
napis14_w_euro = napis14.replace('zł','€')
print(napis14_w_euro)

#13. sortowanie i obracanie napisów
#13.1. odwracanie napisu
napis15 = 'kemot'
napis15_odwrotnei = napis15[::-1]
print(napis15_odwrotnei)

#13.2. sortowanie napisu
napis16 = 'dbca'
napis16_posortowany = sorted(napis16)
napis16_posortowany = ''.join(napis16_posortowany)
print(napis16_posortowany)