# suma= lambda x,y: x+y
# print(suma(3,4))

# liczby=[1,2,3,4,5]
# kwadraty=list(map(lambda x: x**2, liczby))
# print(kwadraty)

# liczby1=[1,2,3,4,5,6,7,8,9]
# parzyste=list(filter(lambda x: x%2==0,liczby1))
# print(parzyste)

# slowa=["owoc","ni","mam","kotek"]
# posortowane=sorted(slowa,key=lambda x:len(x),reverse=True)
# print(posortowane)

# dane=[(1,5),(3,2),(2,8),(4,1)]
# posortowane=sorted(dane,key=lambda x: x[1])
# print(posortowane)

# slowa=["owoc","ni","mam","kotki"]
# litera='i'
# slowa_filtr=list(filter(lambda x:x.endswith(litera),slowa))
# print(slowa_filtr)

# slownik={"Anna":18,"Szymon":22,"Joanna":47,"Krzysztof":54}
# #posortuj według imion
# slow_pos=sorted(slownik.items(),key=lambda x: x[0])
# print(slow_pos)
# #posrtuj według wieku
# slow_pos=sorted(slownik.items(),key=lambda x: x[1])
# print(slow_pos)

'''
Liczenie liter
Napisz funkjcę, któara przyjmuje ciąg znaków i zwraca liczbe
liter, cyfr, sapcji i wyrazow
'''

def staty(tekst):
    slownik={"litery":0,"cyfry":0,"spacje":0,"wyrazy":0}
    
    for litera in tekst:
        if litera.isalpha():
            slownik['litery'] += 1
        elif litera.isdigit():
            slownik["cyfry"] +=1
        elif litera.isspace():
            slownik["spacje"]+=1
    slownik['wyrazy']=len(tekst.split())
    
    return slownik

tekst=input("Podaj tekst: ")
print(staty(tekst))