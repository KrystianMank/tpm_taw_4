'''
Rozszerzony cyfr cezara
ASCII 32 - 126
'''
ile = 94

def szyfruj():
    print("Szyfrowanie...")
    tekst = input("Podaj tekst do szyfrowania: ")
    klucz = int(input("Podaj klucz: "))
    szyfr = ''
    for litera in tekst:
        szyfr += chr(32 + ((int(ord(litera) + klucz - 32)) % ile)) 
    print(f"Szyrf: {szyfr}")


def odzyfruj():
    print("Deszyfracja...")
    tekst = input("Podaj tekst do odszyfrowania: ")
    klucz = int(input("Podaj klucz: "))
    szyfr = ''
    for litera in tekst:
        szyfr += chr(32 + ((int(ord(litera) - klucz - 32)) % ile)) 
    print(f"Szyrf: {szyfr}")

def menu():
    print("="*50)
    print("Menu: s-szyfrowanie, d-deszyfrowanie")
    print("="*50)
    odp = input("Wybierz opcje: ")
    return odp

odp = menu()
if odp in ['s', 'd']:
    if odp == 's':
        szyfruj()
    else:
        odzyfruj()
else:
    print("Zły wybor...")