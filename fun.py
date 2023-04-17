a = 5
b = 6


def dodaj():
    print("Wynik = ", a + b)


def odejmij(a, b, c=0):
    print("Wynik = ", a - b - c)


def oblicz_vat(cena, vat):
    return cena * (100 + vat) / 100


def odejmij_2(a, b):
    return a - b


dodaj()
odejmij(3, 4)
odejmij(3, 4, 5)
print(odejmij(5, 6))  # None - funkcja nic nie zwraca
print(oblicz_vat(1000, 23))
print(oblicz_vat(odejmij_2(30000, 18000), 23))

oblicz_vat_3 = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat_3(1000))