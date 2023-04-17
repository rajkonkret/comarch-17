krotka = ("Tomek", "Michał", "Asia", "Dariusz")
print(krotka)
print(krotka)
print(type(krotka))
krotka_2 = ("Radek",)
print(type(krotka_2))
krotka_3 = (43, 55, 22.46, 11, 200)
print(krotka_3)
print(krotka.count("Tomek"))
print(krotka.index("Asia"))
asia = krotka[2]
print(asia)

krotka = ("Tomek", "Michał", "Asia", "Dariusz")
*imie1, imie2, imie3 = krotka  # rozpakowanie krotki
print(imie1)
lista = list(krotka)
print(lista)