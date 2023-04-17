import random

# random  - generator liczb pseudolosowych

print(random.randint(1, 6))  # 1..6
print(random.random() * 6)  # 0..5
print(random.randrange(6))  # 0..5
print(random.randrange(1, 6))   # 1..5

lista = [5, 7, 9, 34, 55, 0]
print(random.choice(lista))

lista_2 = list(range(1, 50))
print(lista_2)

wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)

wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)

wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)

wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)

wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)

wyn = random.choice(lista_2)
print(wyn)
lista_2.remove(wyn)
# 14:30