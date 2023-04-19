from decimal import Decimal,getcontext

# decimal - działą na stałej liczbie wartosci po przecinku
# błąd zaokrąglenia
a = 0.2
b = 0.7
print(a + b)
# 0.8999999999999999

# getcontext().prec = 4 # precyzja ale dla całego wyniku, nie tylko liczb po przecinku

kwota_1 = Decimal('2110.25')
kwota_2 = Decimal('744.50')

suma = kwota_1 + kwota_2
print("Suma:", suma)

roznica = kwota_1 - kwota_2
print("Róznica:", roznica)

podatek = Decimal('0.23')
kwota = kwota_1 * (1 + podatek)
print("Kwota z podatkiem", kwota)

ilosc_osob = 3
rachunek_na_osobe = kwota / ilosc_osob
print("Rachunek na osobe", rachunek_na_osobe)