'''
Funkcje w Pythonie
'''
#Wyświetlanie menu
def menu():
    print(
    """
    Menu: d-dodawanie, o-odejmowanie,
    m-mnożenie, s-dzielenie
    """
    )

#obliczenia na działaniach podanych przez użytkownika
def kalk(dzialanie, x=1, y=1):
    if dzialanie=='d':
        return x+y
    elif dzialanie=='o':
        return x-y
    elif dzialanie=='m':
        return x*y
    elif dzialanie=='s':
        if y!=0:
            return x/y
        else:
            return "Dzielenie przez 0"
    else:
        print("Kys, zły wybór")
        return 0
        
#funkcja główna
def f_main():
    x=float(input("Podaj liczbe: "))
    y=float(input("Podaj drugą liczbę: "))
    menu()
    dzialanie=input("Wybierz działanie: ")
    wynik=kalk(dzialanie,x,y)
    print(f"Wynikiem tego działania jest: {wynik}")
        
#------------------------------------------------

f_main()