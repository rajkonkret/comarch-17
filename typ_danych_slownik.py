# slownik - dict()
# klucz - wartosc
# {'name' : 'Radek'}
# klucze nie mogą sie powtarzac
# '' ""
# " '' "
slownik = {}  # deklaracja pustego słownika
print(type(slownik))
slownik['imie'] = "Radek"
slownik['wiek'] = 39

print(slownik)

print(slownik.items())
print(slownik.keys())
print(slownik.values())

lista = [44, 5, 66, 77, 88, 33, 22, 44]
slownik['liczby'] = lista
print(slownik)
print(slownik['liczby'][0])
lista_2 = [66,77,88,99]
nowa_lista = lista + lista_2
print(nowa_lista)

slownik_2 = {'imie': ["Radek", "Andrzej"], "wiek":39}
print(slownik_2)
# za pomoca koekcji dict() zaproponowac słownik pol - ang

# slownik_3 = {'name' : 'imie', 'cat' : 'kot'}
# print(slownik_3['name'])
# slownik_3.update({'dog':'pies'})
# # input() - wczytaj
# print('Mam w słowniku', slownik_3.keys())
# key = input("Podaj wyraz")  # zwraca dane typu str
# key.replace(" ", "")
#
# print(slownik_3[key.lower()])

a = int("34")
print(a)
b = str(17)
print(b)
print(str(a) + b)  # konkatenacja

# 13: 25