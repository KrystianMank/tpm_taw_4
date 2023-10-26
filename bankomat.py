'''
Aplikacja wydająca resztę...
Nominały do wydawania: 500, 200, 100, 50 ,20, 10, 5, 2, 1, 0.5, 0.2 , 0.1
np.
kw = 151.20
wp = 200
r = wp-kw = 48.80
'''
nominaly=[500, 200, 100, 50 ,20, 10, 5, 2, 1, 0.5, 0.2 , 0.1, 0.05, 0.02, 0.01]
dowyplaty={}
      
#menu
def menu():
    print("="*50)
    print("Aplikacja do wydawania reszty")
    print("="*50)

#wyświetlanie wyników
def show(dowyplaty):
    if isinstance(dowyplaty,dict): #if isinstance(dowyplaty,dict): if type(dowyplaty) is dict:
        print("Nomianały do wypłaty: ")
        for k, v in dowyplaty.items():
            if v!=0:
                print(f"{k} PLN - {v} sztuk")
    else:
        print(dowyplaty)

#wydawanie reszty
def wydaj(kw, wp):
    r = wp - kw
    if r!=0:
        i = 0
        while r!=0 and i < len(nominaly):
            ile = int(r / nominaly[i])
            r -= ile * nominaly[i]
            r=round(r,2)
            dowyplaty[nominaly[i]] = ile
            i+=1
        return dowyplaty
    else:
        print("Nic do wydania")

#wprowadzanie wartosci kw i wp
def entry():
    try:
        kw, wp = -1, -2
        while kw<=0 or wp<=0 or kw>wp:
            kw = float(input("Podaj kwotę do zapłaty: "))
            kw=str(kw)
            for i in range(len(kw)):
                if kw[i] == '.':
                    kw[i+3] = 0
                    
                        
            wp = float(input("Podaj wartość wpłaty: "))

            if kw<=0 or wp<=0:
                print("Podałeś ujemną liczbę. Wprowadź ponownie:")
            if kw>wp:
                print("Podałeś mniejszą kwotę wpłaty od należnej. Podaj ponownie:")
            
    except ValueError:
        print("Nie podałeś liczb!")
    else:
        dowyplaty = wydaj(kw,wp)
        show(dowyplaty)
   

#--------------------------------------------------------------------
def main():
    while True:
        menu()
        entry()
        koniec=input("Czy chcesz kontynuuować? (n-nie)")
        if koniec in ('t','T','n','N'):
            if koniec != 't' and koniec != 'T':
                print("-----------Dziękuje za współpracę---------------")
                break
                
        else:
            print("zły wybór")
           

if __name__=='__main__':
    main()