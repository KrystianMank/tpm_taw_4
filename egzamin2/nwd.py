def wprowadzanie():
    try:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        
        if a>0 and b>0:
            return a,b
        else:
            return wprowadzanie()
        
    except ValueError:
        print("Nie prawidłowe dane")
        return wprowadzanie()

'''
**********************************************
nazwa funkcji: nwd
opis funkcji: sprawdza nwd dla dwóch podanych liczb jako argumenty
parametry:  a - typ int, wartość pierwszej liczby
            b - typ int, wartośc drugiej liczby
zwracany typ i opis: a - typ int - zwraca wartość pierwszej liczby po wyknaniu działań jako nwd
autor: Krystian Mankiewicz 6
***********************************************
'''

def nwd(a, b):
    while a != b:
        if a>b:
            a -= b
        else:
            b -= a

    return a


def main():
    a, b = wprowadzanie()
    wynik = nwd(a,b)
    print(f"NWD dla: {a} i {b} wynosi {wynik}")

if __name__=="__main__":
    main()