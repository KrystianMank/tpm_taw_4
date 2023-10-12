'''
Metody sortowania
v.0.1
'''
from random import randint as rdi
#menu
def menu():
    print("="*35)
    print(
        f"""
        metoda: b-bubble sort, 
        i-insert sort, 
        s-selction sort
        q-quick sort
        """
    )
    print("="*35)

#dekorator pomiaru czasu
def measure():
    pass

#generator liczb
def generuj():
    n=int(input("Podaj ilość liczb: "))
    d=int(input("Podaj dolny zakres liczb: "))
    g=int(input("Podaj górny zakres liczb: "))
    
    if d>g:
        d,g=g,d
        
    liczby=[ rdi(d,g) for i in range(n) ]
    return liczby

#bubble sort
def bubblesort(liczby):
    pass

#insert sort
def insertsort(liczby):
    pass

#selection sort
def selectionsort(liczby):
    pass

#quick sort
def quicksort(liczby):
    pass

#funkcja główna
def f_main():
    # menu()
    czygen=True
    while True:
        if czygen==True:
            generuj()
        else:
            print("XXXXXX")
        
        koniec=input("Czy chcesz kontynuuować? (n-nie)")
        if koniec != 't' and koniec != 'T':
            break
        else:
            wyb=input("Czy chcesz wygenerować nowe liczby? (n-nie)")
            if wyb in ('t','n','T','N'):
                if wyb == 't' or wyb=='T':
                    czygen=True
                else:
                    czygen=False
            else:
                print("Wybierz poprawnie...")
#-----------------------------------------
f_main()