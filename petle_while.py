licznik = 0

while True:
    licznik += 1
    print("Komunikat...")
    if licznik == 10:
        break

licznik = 0
while licznik < 10:
    print("Komunikat...")
    licznik += 1
# if a:=1
lista = []

while True:
    wejscie = input("Wprowadz liczbe")  # zwraca str
    if wejscie == 's':
        break
    lista.append(wejscie)

print(lista)

x = 10
if x > 5:
    print(x)

x = 0
if False or (x := 10) > 5:  # walrus operator
    print(x)

lista = [4, 6, 8, 10]
people = ["Radek", "Kuba", "Agata", "Krystyna"]
pos = 0

while pos < len(people):
    person = people[pos]
    liczba = lista[pos]
    pos += 1
    print(person, liczba)



