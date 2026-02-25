'''def hurra():
     print('Hurra!\n' * 50)'''


#Hurra2 - nazwa funkcji
#n - parametr funkcji
#6 - argument funkcji
#hurra2(6) - wywołanie funkcji dla argumentu n = 6

'''def hurra2(n):
    print('Hurra!\n' * n)

hurra2(6)
'''

# n = 10 znacz parametr z argumentem domyślnym
'''def hurra3(n = 10):
    print('Hurra!\n' * n)

hurra3()'''

#jeżeli funkcja poprostu wykonuje jakąś czynność i nie możemy wykorzystać dalej efektów jej pracy to jest to procedura

#Pole całkowite graniastołupa parwidłowego trójkąrne

def pole_trójkątna_równobocznego(a):
    return a ** 2 * (3**0.5) / 4

#Pp = pole_trójkątna_równobocznego(3 ** 0.25)

def pole_prostowkąta(a, b):
    return a * b

#Psb = pole_prostowkąta(5, 4)

def p_gransiatosłópa_prawidłowego_trójkątnego(a, b):
    return pole_trójkątna_równobocznego(a) * 2 + pole_prostowkąta(a, b) * 3

Pg = p_gransiatosłópa_prawidłowego_trójkątnego(7, 4)
print(Pg)