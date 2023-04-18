class Dom:
    """
    To jest kalsa DOM
    """

    def __init__(self, metraz, kolor, ilosc_okien):
        self.__metraz = metraz
        self.kolor = kolor
        self.__ilosc_okien = ilosc_okien

    def podaj_metraz(self):
        print("Metraż wynosi", self.__metraz)

    def podaj_okna(self):
        print("Metraż wynosi", self.__ilosc_okien)

    def zmien_metraz(self):
        wybor = int(input("Podaj metraz"))
        self.__metraz = wybor
        print("Metraz wynosi", self.__metraz)

    def zmien_okna(self):
        wybor = int(input("Podaj okna"))
        self.__ilosc_okien = wybor

    def zmien_kolor(self):
        wybor = input("Podaj kolor")
        self.kolor = wybor
        print("Kolor wynosi", self.kolor)
        self.__farba()

    def __farba(self):
        print("Skonczyła sie farba")


dom_1 = Dom(54, "zielony", 5)
dom_1.zmien_metraz()
dom_1.podaj_metraz()
dom_1.zmien_kolor()