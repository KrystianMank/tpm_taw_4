'''
Aplikacja wydająca resztę...
Nominały do wydawania: 500, 200, 100, 50 ,20, 10, 5, 2, 1, 0.5, 0.2 , 0.1
np.
kw = 151.20
wp = 200
r = wp-kw = 48.80
'''
nominaly=[500, 200, 100, 50 ,20, 10, 5, 2, 1, 0.5, 0.2 , 0.1]
dowyplaty={}
      
#menu
def menu():
    print("="*50)
    print("Aplikacja do wydawania reszty")
    print("="*50)

#wyświetlanie wyników
def show(dowyplaty):
    print("Nomianały do wypłaty: ")
    for k, v in dowyplaty.items():
        if v!=0:
            print(f"{k} - {v}")

#wydawanie reszty
def wydaj(kw, wp):
    r = wp - kw
    i = 0
    while r!=0 and i < len(nominaly):
        ile = int(r / nominaly[i])
        r -= round(ile * nominaly[i], 1)
        dowyplaty[nominaly[i]] = ile
        i+=1
    return dowyplaty

#wprowadzanie wartosci kw i wp
def entry():
    try:
        kw = float(input("Podaj kwotę do zapłaty: "))
        wp = float(input("Podaj wartość wpłaty: "))
    except ValueError:
        print("Nie podałeś liczb!")
    else:
        '''
            czy czasem nie ujemne
            a co jeśli kw > wp
        '''
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