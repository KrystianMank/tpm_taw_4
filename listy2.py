# list=[2,4,5,7,8,5,4]
# print(list[1:5:1])

# for i in list:
#     print(i)
    
# for i in range(len(list)):
#     print(f"Element o indeksie {i} to {list[i]}")
    
# for i in range(1,5,1):
#     print(f"Element o indeksie {i} to {list[i]}")
    
# ile=int(input("Ile liczb? "))
# lista1=[]
# for i in range(ile):
#     lista1.append(int(input("Podaj liczbe: ")))

# print(lista1)
# lista1.reverse()

# for i in lista1:
#     print(lista1[i])
    
#zad1: wygeneruj 1000 liczb rzeczywistych z zakresu 0 do 1

import random as rd
from random import uniform as rdu

# lista=[]

# for i in range(1000):
#     lista.append(rdu(0,1))
    
# print(lista)

# #list comprehension
# lista1 = [rdu(0,1) for i in range(1000)]
# print(lista1)

#zad2: wygeneruj 1000 liczb nieparzystych z akresu 1 do 100

# lista_np=[]

# for i in range(1000):
#     li=rd.randint(1,99)
#     if li % 2 == 0:
#         li+=1
#     lista_np.append(li)
        
# print(lista_np)

lista_liczb=[rd.randint(1,99) for i in range(1000)]
lista_nieparz=[i if i%2 != 0 else i+1 for i in lista_liczb]
print(len(lista_nieparz))