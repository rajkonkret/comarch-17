class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = ""

    def powitanie(self):
        """
        Metoda w klasie Human
        :return: print z imieniem
        """
        print("Nazywam sie", self.imie)


czl_1 = Human()
print(czl_1.__doc__)
print(czl_1.plec)
print(czl_1.wiek)
print(czl_1.imie)
czl_1.imie = "Radek"
print(czl_1.imie)
czl_1.powitanie()