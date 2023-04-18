# lambda - skrocona forma funkcji

odejmij = lambda a, b: a - b

print(odejmij(5, 3))
print(odejmij(9, 3))

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100

print(oblicz_vat(1000, 1))
print(oblicz_vat(1000, 7))
print(oblicz_vat(1000, 23))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))
print(wiek(11))
print(wiek(21))
x = 10


def wiek_2(x):
    if x < 10:
        return "dziecko"
    else:
        if x < 18:
            return "nastolatek"
        else:
            return "dorosły"


lista = [1, 2, 7, 8, 8, 10, 56]
# map() - mapowanie - zamiana na inne dane
print(f"Zastosowanie map: {list(map(lambda x: x * 2 , lista))}")
print(f"Zastosowanie map: {list(map(lambda x: x ** 2, lista))}")

# filter() - filtruje wg warunku
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 3, lista))}")
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 8, lista))}")

# x > 7, a mniejsze od 20
# 7 < x < 20
print(f"Zastosowanie filter(): {list(filter(lambda x: 7 < x < 20, lista))}")

words = ['apple', 'banana', 'cherry']
sorted_words = sorted(words, key=lambda  x: len(x))
print(sorted_words)

numbers = [1, 2, 3, 4, 5]
even_n = list(filter(lambda x: x % 2 == 0, numbers))
print(even_n)


def min_max(numbers):
    return min(numbers), max(numbers)


x = min_max(numbers)
print(x)    #  # ( 1, 5 )
print(type(x))
minimum, maximum = min_max(numbers)
print(minimum)  # 1
print(maximum)  # 5

a = 10
b = 15
a, b = b, a
print(a)
print(b)