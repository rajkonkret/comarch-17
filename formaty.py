user = "Tomek"
wiek = 39
wersja = 3.9000001
liczba = 134632344532

print("Witaj %s masz teraz %d lat" % (user, wiek))  # lazy, zalecany przy logowaniu
print("Witaj %(user)s masz teraz %(wiek)d lat" % {'user': user, 'wiek' : wiek})
print("Witaj {} masz teraz {} lat".format(user, wiek))
print(f"Witaj {user} masz teraz {wiek} lat")

print("Używamy wersji Python %i" % 3)
print("Używamy wersji Python %f" % 3.9)
print("Używamy wersji Python %.1f" % 3.9)
print("Używamy wersji Python %.f" % 3.9)    # 0 miejsc po przecinku
print("Uzywamy wersji Python {}".format(wersja))
print(f"Uzywamy wersji Python {wersja}")
print(f"Uzywamy wersji Python {wersja:.1f}")
print(f"Uzywamy wersji Python {wersja:.2f}")
print(f"{user:>10}")
print(f"{user:>20}")
print(f"{user:<30}")

print(liczba)
print("Nasza duza liczba {:,}".format(liczba))
print("Nasza duza liczba {:,}".format(liczba).replace(",", "."))
print("Nasza duza liczba {:,}".format(liczba).replace(",", " "))


