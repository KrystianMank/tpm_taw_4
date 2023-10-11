"""
exceptions
v.0.1    
"""
try:
    n=int(input("Podaj liczbę"))
    x=10 / n
    print(f"Wynik dzielenia 10 przez {n} wynosi {x}")
except ZeroDivisionError:
    print('Nie dzielimy przez 0')
except ValueError:
    print('wynikiem nie jest liczba CALKOWITA')
except Exception as e:
    print(f"wystapil wyjatek{e}")
finally:
    print("Zakończyłem pracę")