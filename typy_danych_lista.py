# 11:25

lista = []  # definicja pustej listy
# dodawanie na koncu listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Asia")
lista.append("Renata")
print(lista)
# dodawanie elementu na indeksie nr.: 1
lista.insert(1, "Darek")
# indeksy w liscie numerowane od 0
print(lista)
# nadpisanie elementu o indeksie 1
lista[1] = "Magda"
print(lista)
# usuniecie z listy po elemencie
# usunie pierwsze wystąpienie
lista.remove("Asia")
print(lista)
lista_2 = lista.copy()  # kopia listy
lista_3 = lista  # kopia referencji do listy
# usuniecie wszystkiego z listy
lista.clear()
print("-------")
print(lista)
print(lista_2)
print(lista_3)

liczby = [54, 999, 34, 22, 12.54, 876]
print(liczby)
liczby.sort()
liczby.reverse()
print(liczby)
liczby[0] = 6666
print(liczby[0:3])  # 0..2
print(liczby[:3])
print(liczby)
print(liczby[2:])
print(liczby[:-1])
print(len(liczby))  # długosc kolekcji, liczba elementow
krotka = tuple(liczby)  # rzutowanie listy na tuple
print(krotka)
