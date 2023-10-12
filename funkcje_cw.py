# def srednia(lista):
#     ilosc=len(lista)
#     suma=sum(lista)
    
#     if ilosc!=0:
#         return suma/ilosc
#     else:
#         return 0

# lista=[2,5,4,7,6,8]
# print(srednia(lista))

# def srednia2(*args):
#     ilosc=len(args)
#     suma=0
#     for i in args:
#         suma+=i
#     return suma/ilosc

# print(srednia2(2,3,4,5,2,3,2,8,6,7,2))


# def kolo(r):
#     pi=3.14
#     pole = r*(pi**2)
#     obwod = 2*pi * r
    
#     return pole, obwod

# r=float(input("Podaj promień: "))

# pole, obwod= kolo(r)
# print(f"Koło o promieniu {r} ma pole {pole} i obwod: {obwod}")

# print(f"Koło o promieniu {r} ma pole {kolo(r)[0]} i obwod: {kolo(r)[1]}")