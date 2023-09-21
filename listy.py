'''
Typ LIST - sekwencyjny
'''
lista1=[1,3,5,2,7,1,9,0,5,3,6]
lista2=[3,4,"teskt"]
lista3=[3,5, [55,33,11] , ["co","tek",3] ]

# print(type(lista1))

# print(lista3)
# print(lista1[2])
# print(lista1[1:4])
# print(lista1[1:4:2]) #[początek, koniec, krok(domyślnie +1)] 
# print(lista1[::-1]) 

# print(lista1[-3:-8:-2])

# #co trzenie od prawej
# print(lista1[::-3])

# print(lista3[3][1])

# lista3[2][0]=666
# print(lista3[2][0])

lista4=[11,22,33,44,55,66,77,4,4]

#długość listy
n = len(lista4)
print(f"Długość listy {n}")

#dodawanie elementu do listy na końcu
lista4.append(4)
print(lista4)

#wstawienie elemntu w dowolny indeks
lista4.insert(2,99)
print(lista4)

#usuwa i pobiera ostatni elemnt listy
lista4.pop()
print(lista4)

#rozszezenie listy o inną listę
listax=[4,2,4]
lista4.extend(listax)
print(lista4)

#zliczenie wystąpień danej liczby
x=lista4.count(4)
print(f"Liczb 4 jest w liście: {x}")

#odwrócenie kolejności
lista4.reverse()
print(lista4)

#sortowanie
lista4.sort(reverse=True)
print(lista4)

#jak skleic lsite sama ze sobą tak aby na początku była lista poczatkowa i dalej lista w odwroonej kolejnosci
#345
#345 543
lista=[3,4,5]
lista.extend(lista[::-1])
print(lista)

