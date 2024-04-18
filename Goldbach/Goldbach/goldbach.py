'''
Mocna hipoteza Goldbacha
'''
def wczytaj(nazwa):
    try:
        with open(nazwa, "r+t") as file:
            lines = file.readlines()
            lines = [ int(l.split(" ")[0]) for l in lines ]
        
        return lines

    except FileNotFoundError as err:
        print(f"File {nazwa} not found. Error: {err}")

def czyPierwsza(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def goldbach(n):
    if n % 2 == 0:
        for i in range(3, n+1):
            if czyPierwsza(i):
                r = n - i
                if czyPierwsza(r):
                    return (i, r)
    else:
        return "brak"   

def main():
    #liczby = wczytaj("przyklad.txt")
    liczby = wczytaj("pary.txt")
    for liczba in liczby:
        print(goldbach(liczba))


if __name__=="__main__":
    main()