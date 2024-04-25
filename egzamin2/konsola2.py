from random import randint

def losuj(n):
    tab = [randint(1,100) for i in range(n)]
    return tab

def wprowadzanie():
    try:
        x = int(input("Podaj liczbe: "))
        return x
    except ValueError:
        print("Błąd wprowadzonych danych")
        return wprowadzanie()


'''
******************************************************
 nazwa funkcji: wartownik
 argumenty: tab - typ lista - przechowuje wygenerowane pseudolosowo liczby
            x - typ int - szukana liczba
 typ zwracany: String, gdy nie znaleziono liczby
               Int, zwraca indeks położenia liczby gdy zostaje znaleziona  
 informacje: Przeszukuje listę liczb wygenerowanych funkcją losuj a następnie szuka czy wytępuje "x" podany przez użytkownika
 autor: Krystian Mankiewicz
*****************************************************
'''
def wartownik(tab, x):
    tab.append(x)

    for i in range(len(tab)):
        if tab[i] == x:
            if i == len(tab) - 1:
                return "Nie znaleziono elementu"
            else:
                return i

def main():
    tab = losuj(50)
    x = wprowadzanie()
    wynik = wartownik(tab,x)

    ll = ''
    for i in range(len(tab)-1):
        ll += str(tab[i]) + ", "
    print(ll)

    if type(wartownik(tab, x)) == type(""):
        print(wynik)
    else:
        print(f"Element {x} został znaleziony pod indeksem {wynik}") 
    


if __name__=="__main__":
    main()