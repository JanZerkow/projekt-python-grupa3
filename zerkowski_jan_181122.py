def main():
    n = int(input("liczba do Zad 2 i 3: "))
    print(iloraz())
    print(cyfry(n))
    print(pierwsza(n))


def iloraz():
    n = 3
    wynik = 4
    while n <= 10:
        if n % 2 == 0:
            wynik /= n
        n += 1
    return wynik

def cyfry(n):
    if n >= 0:
        liczba = str(n)
        wynik = 0
        for i in liczba:
            wynik += int(i)
    else:
        return(print("Podano liczbe nienaturalną (Zad.2)"))
    return wynik


def pierwsza(n):
    if n <= 1:
        return ("Podano błędne dane (Zad.3)")

    if n > 1:
        for i in range(2, n//2):
            if n % i == 0:
                return False
        return True


main()