wiek = 47
rok = 2023
temp = 36.6  # float
wiek_2 = 37.5

print(wiek)
print(wiek_2)
print(type(wiek_2))
print(5 * "Radek")
print(5 * "1")

print(wiek * rok)
print(wiek - rok)
print(wiek + rok)
print(wiek / rok)  # wynik dzielenia zawsze float
print(4 / 2)  # wynik dzielenia zawsze float
print(wiek // rok)  # czesc całkowita dzielenia
print(wiek ** rok)  # potęgowanie
print(54 - (5 * 43) + (4 / 2 + 4) / 2)
print("\tsprawdzam zmienna temp: {} {}\n".format(wiek, temp))
print(f"\tsprawdzam zmienna wiek: {wiek} {temp}")
print(f"""
    zmienna {wiek}
    zmienna {temp}
{54 - (5 * 43)}
""")

imie = "Radek Radek"
imie.lower()  # zamiana na małe litery
print(imie)  # str - niemutowalne
imie_2 = imie.lower()
print(imie_2)
print(imie.lower())
print(imie.upper())
print(imie.capitalize())
print(imie)
print(imie.count("Radek"))

print(4 // 2)
print(type(4 // 2))  # wynik int
print(type(4 / 2))  # wynik float

# bool
# True, False - obowiazkowo z duzej litery
is_true = False  # 0 - False, 1 - True
print(is_true)
print(type(is_true))
print(int(is_true))
print(bool(7))  # True
