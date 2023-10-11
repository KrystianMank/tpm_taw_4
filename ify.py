"""
IF 05.10
v.0.1
"""
#podstawowy if
n=int(input("Podaj liczbę"))
# if n%2==0:
#     print(" Jest parzysta")
# else:
#     print(" Nieparzysta")

#warunek elif
# if n<0:
#     print(f"Liczba {n} jest ujemna")
# elif n==0:
#     print(f"Liczba {n} jest zerem")
# else:
#     print(f"Liczba {n} jest dodatnia")

#uzycie and
# if n%2==0 and n<0:
#     print(f"{n} jest parzyste i ujemne")
# elif n%2==0 and n>=0:
#     print(f"{n} jest parzyste i dodatnie")
# elif n%2!=0 and n<0:
#     print(f"{n} jest nieparzyste i ujemne")
# else:
#     print(f"{n} jest nieparzyste i dodatnie")

#krotsze
if n%2==0:
    k1="jest parzyste"
else:
    k1="jest nieparzyste"
    
if n<0:
    k2=" jest ujemna"
elif n==0:
    k2=" jest zerem"
else:
    k2=" jest dodatnia"
    print(f"liczba {n} {k1} i {k2}")