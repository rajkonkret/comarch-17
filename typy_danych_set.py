# set() - przechowuje tylko niepowtarzajace sie elementy
lista = [44, 55, 66, 77, 33, 22, 11, 55, 33, 11]
zbior = set(lista)  # rzutowanie na set
print(zbior)
zbior_1 = set()  # deklaracja pustego seta
print(type(zbior_1))
zbior.add(18)
zbior.add(18)
zbior.add(62)
print(zbior)
print(zbior.pop())  # pierwszy element z seta(równiez zostanie usniety)
print(zbior.pop())
print(zbior.pop())
print(zbior)

zbior_3 = {66, 11, 44, 55, 62, 999}
print(zbior_3)
print(zbior_3 | zbior)  # suma zbiorów
print(zbior_3 & zbior)  # część wspólna zbiorów
print(zbior_3 - zbior)  # różnica zbiorów
print(zbior_3.difference(zbior))