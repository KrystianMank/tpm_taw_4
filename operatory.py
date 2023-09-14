'''
Prosty kalkulator ver. 0.1
K>M> 2023
'''
#pobieranie danych

x=float(input("Podaj x="))
y=float(input("Podaj y="))

#obliczenia
suma=x + y
roznica = x- y
iloczyn = x * y
iloraz= x / y

potega = x ** y
pierwiastek = x ** 0.5

czesc_calkowita_dzielenia = x // y
reszta_z_dzielenia = x % y

print(f"Suma = {suma}\n rożnica = {roznica}\n \
    iloczyn = {iloczyn}\n iloraz = {iloraz}\n \
        potega = {potega} pierwaistek = {pierwiastek}\n \
            cześć całkowita z dzieleniia = {czesc_calkowita_dzielenia}\n \
                reszta z dzielenia = {reszta_z_dzielenia}")

print("Dodano koniec")
print("Zmiana w repozytorium")
