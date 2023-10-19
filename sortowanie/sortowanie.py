'''
Metody sortowania
v.0.1
'''
from random import randint as rdi
import time
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
def measure(func):
    def wrapper(*kwargs):
        start = time.perf_counter()
        liczby = func(*kwargs)
        stoptime=time.perf_counter()
        timer = stoptime - start
        
        return liczby, timer
    return wrapper

#generator liczb
def generuj():
    print("______Generowanie liczb_____")
    n=int(input("Podaj ilość liczb: "))
    while n<=0:
        print("Podałeś błędną liczbę!")
        n=int(input("Podaj ilość liczb:"))
        
    d=int(input("Podaj dolny zakres liczb: "))
    g=int(input("Podaj górny zakres liczb: "))
    
    if d>g:
        d,g=g,d
        
    liczby=[ rdi(d,g) for i in range(n) ]
    return liczby

@measure
#bubble sort
def bubblesort(liczby):
    
    for i in range(len(liczby)):
        for j in range(len(liczby)-1):
            if liczby[j] > liczby[j+1]:
                liczby[j], liczby[j+1] = liczby[j+1], liczby[j]
    
    return liczby

@measure
#insert sort
def insertsort(liczby):
    for i in range(1,len(liczby)):
        key=liczby[i]
        j = i - 1
        while j>=0 and liczby[j] > key:
            liczby[j+1] = liczby[j]
            j -= 1
        liczby[j+1] = key
    
    return liczby

@measure
#selection sort
def selectionsort(liczby):
    for  i in range(len(liczby)):
        index_smallest=i
        for j in range(i+1, len(liczby)):
            if liczby[j] < liczby[index_smallest]:
                index_smallest=j
        liczby[i], liczby[index_smallest] = liczby[index_smallest], liczby[i]
    
    return liczby

#quick sort
def quicksort(liczby):
    if len(liczby) <=1 :
        return liczby
    
    pivot = liczby[len(liczby) // 2]
    left = [ x for x in liczby if x < pivot ]
    middle = [ x for x in liczby if x==pivot ]
    right = [ x for x in liczby if x > pivot ]
  
    return quicksort(left) + middle + quicksort(right)


@measure
def quicksort_start(liczby):
    liczby=quicksort(liczby)
    return liczby
    
def witaj():
    
    print("\n")
    print("="*50)
    print("Sortowanie liczb")
    print("="*50)

def show(liczby,jaka=True, timer=0):
    if jaka==True:
        print("\nLiczby przed sortowaniem:")
        print(liczby)
    else:
        print("\nPosortowane liczby: ")    
        print(liczby)
        print(f"------------Czas wykonania sortowania {timer}s.----------")
    
#funkcja główna
def f_main():
    # menu()
    czygen=True
    
    witaj()
    
    while True:
        if czygen==True:
            liczby_g=generuj()
        
        menu()
        wybor=input("Wybierz metodę sortowania: ")
        while wybor not in ('b','i','s','q'):
            print("Zły wybór")
            wybor=input("Wybierz metodę sortowania: ")
        if wybor in ('b','i','s','q'):
            posort=[]
            liczby1=liczby_g.copy()
            if wybor == 'b':
                print("Bubblesort")
                
                show(liczby1)
                posort, timer=bubblesort(liczby1)
                show(posort,False,timer)
                
            elif wybor=='i':
                print("Insertsort")
                
                show(liczby1)
                posort, timer=insertsort(liczby1)
                show(posort,False,timer)
                
            elif wybor=='s':
                print("Selection sort")
                
                show(liczby1)
                posort, timer=selectionsort(liczby1)
                show(posort,False,timer)
                
            elif wybor=='q':
                print("Quicksort")
                
                show(liczby1)
                posort, timer=quicksort_start(liczby1)
                show(posort,False,timer)
        else:
            print("Zły wybór")
        
        koniec=input("Czy chcesz kontynuuować? (n-nie)")
        if koniec != 't' and koniec != 'T':
            print("-----------Dziękuje za współpracę---------------")
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