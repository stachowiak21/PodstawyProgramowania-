napis = 'informatyka'

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