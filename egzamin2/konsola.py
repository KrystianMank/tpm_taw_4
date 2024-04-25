def sprawdzPeselPlec(pesel):
    if pesel[9] in ("0", "2", "4", "6", "8"):
        return "K"
    elif pesel[9] in("1", "3", "5", "7", "9"):
        return "M"

def podajPesel():
    try:
        pesel = int(input("Podaj numer pesel: "))
        while len(str(pesel)) != 11:
            pesel = int(input("Podaj numer pesel: "))
    except ValueError:
        print("Pesel niepoprawny ")
        pesel = int(input("Podaj numer pesel: "))

    return str(pesel)


'''
**********************************************
nazwa funkcji: cyfraKontrolna
opis funkcji: funkcja sprawdza sumę kontrolną na podstawie wag,
parametry: 
    wagi - typ lista, przechowuje listę wag dla peselu
    S - typ int, przechowujący sumę iloczyów wag i cyfr peselu
    M - typ int, wynik dzielenia modulo S%10
    R - suma kontrolna
zwracany typ i opis: Funkcja zwraca True, jeśli suma kontrolna R jest równa ostatniej cyfrze podanego peselu,
Funkcja zwraca False, jeśli nie jest równa
autor: Krystain Mankiewicz 
***********************************************
'''
def cyfraKontrolna(pesel):
    wagi = [1,3,7,9,1,3,7,9,1,3]
    S = 0
    for i in range(len(wagi)):
        S += int(pesel[i]) * wagi[i]

    M = S % 10

    if M == 0:
        R = 0
    else:
        R = 10 - M

    if str(R) == pesel[10]:
        return True
    else: 
        return False

def main():
    pesel = podajPesel()
    print("Kobieta" if sprawdzPeselPlec(pesel)=="K" else "Mężczyzna")
    
    print("Pesel poprawny" if cyfraKontrolna(pesel) else "Pesel niepoprawny" )

if __name__=="__main__":
    main()