'''
Sprawdzian 01 Liczby, listy, krotki
Krystian Mankiewicz
Klasa 4TPM
28.09.2023
'''
#1
lista1=[2,6,4,'Zenon','Alicja']
#2
print(lista1)
#3
lista1.remove(4)
#4
lista1.append(99)
#5
lista2=[100,200,300]
#6
lista1.extend(lista2)
#7
for i in lista1,lista2:
    print(i)
#8
lista2.reverse()
#9
print(lista2)
#10

#11
print(lista1)
#12
moja_tupla=('A','B','C')
#13
moja_tupla=list(moja_tupla)
moja_tupla.append('D')
moja_tupla=tuple(moja_tupla)
#14
print(moja_tupla)
#BONUS
x=int(input("Podaj początek zakresu: "))
y=int(input("Pdoaj koniec zakresu: "))
listax=[i+1 for i in range(x,y) if(i%2==0)]
print(listax)