def mnozenie(a, b):
    try:
        return int(a) * int(b)
    except ValueError:
        return "Bład wartosci"
    except TypeError:
        return "Błąd typu"


def mnozenie2(a, b):
    try:
        return int(a) * int(b)
    except (ValueError, TypeError) as e:
        return e


def dzielenie(a,b):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Bład wartosci"
    except TypeError:
        return "Błąd typu"
    except ZeroDivisionError:
        return "Dzielenie przez zero"


print(mnozenie(5, 6))
print(mnozenie("3", "4"))
print(mnozenie("A", "B"))
print("nadal działa")
print(mnozenie(2.8, 4.8))
print(mnozenie((2.8,), (4.8,)))
print(mnozenie2((2.8,), (4.8,)))
print(dzielenie(2, 0))


def mnozenie3(a, b):
    try:
        return (int(a) * int(b))
    except Exception as e:
        print("wystapił bląd", e)
    else:
        wynik = [a, b]
        print(wynik)
    finally:
        print("Wykonałem instrukcje z funkcji mnozenia")


mnozenie3((2.8,), (4.8,))
mnozenie3(2.8, 4.8)

