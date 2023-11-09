'''
OOP - object oriented programing 
'''
class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie=imie
        self.nazwisko = nazwisko
        self.wiek=wiek
    
    def przedstaw_sie(self):
        return f"Nazywam się {self.imie} {self.nazwisko} i mam {self.wiek}"
    

class Uczen(Osoba):
    def __init__(self,imie,nazwisko,wiek,klasa):
        super().__init__(imie, nazwisko, wiek)
        self.klasa=klasa
    
    def przedstaw_sie(self):
        return f"Jestem uczniem {self.imie} {self.nazwisko} i chodzę do {self.klasa}"        

    def zmien_klase(self,nowa):
        self.klasa=nowa
        return self.klasa

class Nauczyciel(Osoba):
    def __init__(self,imie,nazwisko,wiek,przedmiot):
        super().__init__(imie,nazwisko,wiek)
        self.przedmiot=przedmiot
        self.__staz=10
    
    def __del__(self):
        print(f"Usunięto obiekt {self.imie} {self.nazwisko}")
    
    def przedstaw_sie2(self):
        return f"Nazywam się {self.imie} {self.nazwisko} i uczę przedmiotu {self.przedmiot}"
    
    def zmien_wiek(self,ile):
        self.zwieksz_staz(ile)
        self.wiek+=ile
        return self.wiek
    
    def pokaz_staz(self):
        return f"Staż {self.__staz}"
    
    def zwieksz_staz(self,ile):
        self.__staz+=ile
        return self.__staz

def witaj(obiekt):
    return obiekt.przedstaw_sie()

def main():
    os1 = Osoba("Jan","Kowalski",17)
    # print(os1.przedstaw_sie())
    
    # u1=Uczen("Jan","Nowak",18,"4TPM")
    # print(u1.przedstaw_sie())
    # u1.zmien_klase("4TI")
    # print(u1.przedstaw_sie())
    
    n1=Nauczyciel("Marek","Lolek",45,"Fizyka")
    print(n1.przedstaw_sie2())
    n1.zmien_wiek(10)
    print(n1.przedstaw_sie())
    print(n1.pokaz_staz())
    n1.zwieksz_staz(5)
    print(n1.pokaz_staz())
    del n1
    try:
        if isinstance(n1, Nauczyciel):
            print(n1.przedstaw_sie())
        else:
            print("On nie żyje...")
    except NameError:
        print("Nie ma obiektu ")
    
    print(witaj(os1))
if __name__=="__main__":
    main()

    
        