class Human:
    """
    Dokumentacja
    """

    def __init__(self, imie, wiek=0, plec="k"):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        """
        metoda
        :return:
        """
        print("Nazywam sie", self.imie)

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w droge")
        else:
            print("Ruszyłem w droge")


czl_1 = Human("Radek", 39, "m")
czl_1.powitanie()
czl_2 = Human("Tomek")
czl_2.powitanie()
czl_2.ruszaj()
czl_1.ruszaj()
print(czl_1.__doc__)
print(czl_1.powitanie.__doc__)
#13:30