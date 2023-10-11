"""
Wygeneruj 1000 słów z losowych liter o długościach od 3 do 10 znaków i zapisz
je do pliku w kolejnych liniach.
Sprawdź czy w pliku znajduj a się wyrazy, które mają długość większą niż4 znak i są jednocześnie palindromami 
wypisz liczbę slow spelniajacych ww. warunek.
"""
import random as rd
wyrazy=[]
for i in range(1000):
    dl=rd.randint(3,10)
    wyraz=''
    for j in range(dl):
        wyraz+=chr(rd.randint(97,122))
    wyrazy.append(wyraz)
print(wyrazy)
for wyraz in wyrazy:
    if len(wyraz) > 4 and wyraz==wyraz[::-1]:
        print(wyraz)
with open("plik.txt","w") as f:
    for i in range(1000):
        dl=rd.randint(3,10)
        wyraz=''
        for j in range(dl):
            wyraz+=chr(rd.randint(97,122))
        f.write(wyraz+"\n")
        
ile=0

with open("plik.txt","rt") as f:
    wyrazy=f.readlines()
    for w in range(len(wyrazy)):
        wyrazy[w]=wyrazy[w].replace("\n","")
        if len(wyrazy[w]) > 4 and wyrazy[w]==wyrazy[w][::-1]:
            ile+=1
    print(ile)