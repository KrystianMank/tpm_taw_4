'''
Krystian Mankiewicz
4TPM
26.10.2023
'''
import random
def losuj():
    try:
        with open("liczby.txt","w") as plik:
            tab=[random.randint(1,100) for i in range(10)]
            for i in range(len(tab)):
                plik.write(str(tab[i]))

    except FileNotFoundError:
        print("Nie znaleziono pliku")
        
def wczytaj():
    slownik={"male":0,"duze":0,"cyfry":0,"interpunkt":0}
    male=0
    duze=0
    cyfry=0
    inter=0
    try:
        with open("liczby.txt","r") as plik:
            asci = plik.readlines()
            for i in asci:
                if int(i)>=97 and int(i)<=122:
                    slownik["male"]+=1
                elif int(i)>=64 and int(i)<=90:
                    slownik["duze"]+=1
                elif int(i)>=48 and int(i)<=57:
                    slownik["cyfry"]+=1
                elif int(i)>=37 and int(i)<47:
                    slownik["interpunkt"]+=1
        with open("staty.py","w") as file:
            for k,a in slownik.items():
                file.write(f"{slownik.keys(k)} - {slownik.values(a)}")
                
    except Exception as e:
        print("Błąd: "+e)
           
def zad4():
    with open("liczby.txt","r") as plik:
        liczby = plik.readlines()
        for i in int(liczby):
            if i%7==0 or i%9==0:
                with open("podzielne.txt","w") as file:
                    file.write(str(i))
        

def main():
    losuj()
    wczytaj()
    zad4()
main()