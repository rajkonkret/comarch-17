a = 10


def dodaj():
    global a    # a traktuj jako globalne
    a = 1
    b = 2
    print("Wynik", a + b)


def dodaj_2():
    b = 2
    return a + b


print("Wartosc a z góry", a)
dodaj()
print("Wartosc a z góry", a)
print(dodaj_2())