# warunki - instrukcja przepływu

# if
# if True:
#     pass

# is_python = input("Podaj czy znasz pythona(t/n)")
#
# if is_python == 't':
#     print("Brawo")
# else:
#     print("Musisz się jeszcze pouczyc")
#
# print("Jestem poza warunkiem")
#
# podatek = 0.0
# zarobki = int(input("Podaj swoj dochód:"))
#
# if zarobki < 10000:  # if warunek, obowiazkowo :
#     podatek = 0.0   # obowiazkowo wciecie
# elif zarobki < 30000:   # kolejne warunki
#     podatek = 0.2
#     print(podatek)
# elif zarobki < 100000:
#     podatek = 0.35
# else:
#     podatek = 0.7
#
# print(f"Zaplacisz {zarobki * podatek} zł")
"""

"""
suma_zam = 247
rabat = 25 if suma_zam > 100 else 0
print(rabat)

if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print(rabat)

temp = 0
alert = True

if temp < 0:
    print("Mróz")
    if temp < -100:
        pass
    if temp < -10:
        if alert:
            print("Alert pogodowy")
elif temp == 0: # przyrównanie
    print("Przymrozek")
elif 10 < temp < 20:
    print("Dodatnia")
elif temp >= 20:
    print("Upał")

lista = []
alert_system = 'email'
error = 'nieznany'
error_message = "Stało się coś strasznego"

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error == 'critical':
        lista.append("Krytyczny")
    elif error == 'midium':
        lista.append("Medium")
    else:
        lista.append("Nieznany")

print(lista)

lista_odp = []

lang = input("Wpisz znany Ci język programowania")

match lang:
    case "python":
        lista_odp.append(lang)
    case "java":
        lista_odp.append(lang)
    case _:
        print("Nie ma takiego języka")

print(lista_odp)