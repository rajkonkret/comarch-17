while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec""")

    wybor = input("Wprowadz numer(1,5)")
    a = int(input("Podaj liczbe a"))
    b = int(input("Podaj liczbe b"))
    if wybor == '1':
        print("Dodajemy", a + b)
    elif wybor == '2':
        print("Odejmujemy", a - b)
    elif wybor == '3':
        print("Mnozenie", a * b)
    elif wybor == '4':
            try:
             print("Dzielimy", a / b)
            except Exception as e:
                print("Nie dziel przez zero")
    else:
        print("Diekujemy. Do widzenia")
        break