# lista = []
# # iteracja porzez licznik
# for i in range(10):  # od 0..9
#     print(i)
#
# for i in range(1, 10): # od 1..9
#     if i % 2 == 0:
#         print(i)
#         lista.append(i)
#
# print(lista)
# # spam += 1	spam = spam + 1
# # spam -= 1	spam = spam - 1
# # spam *= 1	spam = spam * 1
# # spam /= 1	spam = spam / 1
# # spam %= 1	spam = spam %
#
# for cyfra in lista:
#     if cyfra == 2:
#         cyfra += 1  # cyfra = cyfra + 1
#     print(cyfra)
#
# lista = [j for j in range(10) if j % 2 ==0]
# print(lista)
#
# imiona = ["Radek", "Zenek", "Marta"]
# for p in range(len(imiona)):
#     print(p, imiona[p])
#
# for p in imiona:
#     print(p)
# # enumerate - zwraca index i element kolekcji
# for pozycja, osoba in enumerate(imiona):
#     print(pozycja, osoba)
#
# ludzie = ["Radek", "Janek", "Asia", "Michał"]
# wiek = [47, 67, 32, 34]
# jezyk = ['python', 'java']
#
# for p, o in enumerate(ludzie, start=1):
#     print(p, o, wiek[p-1])
#
# # łaczenie kolekcji
# for osoba, wiek, jezyk in zip(ludzie, wiek, jezyk):
#     print(osoba, wiek, jezyk)
#
# print(osoba)
# print(wiek)
# print(jezyk)
#
# for i in range(0, 10, 2):   # start, stop, step(krok)
#     print(i)

napis = "Radek"
for i in range(-1, -len(napis), -1):
    j = i + 1
    if j == 0:
        print(napis[i::])
    else:
        print(napis[i:j])

slownik = {'imie': 'Radek', 'nazwisko': 'Kowalski'}

for k in slownik:
    print(k)

for v in slownik.values():
    print(v)

for k, v in slownik.items():
    print(k, '=>', v)
