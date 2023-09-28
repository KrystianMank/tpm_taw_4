'''
Pobierz od uzytkownika dwa kody pocztowe
i wygeneruj pozostałe kody w tym zakresie
89-600  -  89-620
89-601  , ... , 89-619
'''
kod1=input("Podaj 1 kod pocztowy: ")
kod2=input("Podaj 2 kod pcoztowy: ")

kod1=kod1.split('-')
kod2=kod2.split('-')

n=int(kod2[1])-int(kod1[1])
nowy=''

# for i in range(n):
#     nowy=str(int(kod1[1])+i)
#     print(f"{kod1[0]}-{nowy}")
    
lista=[str(kod1[0]+"-"+str(int(kod1[1])+i)) for i in range(n) if i>0]
print(lista)

    
