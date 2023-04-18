from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    doc
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lece z szybkoscią", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Orzel(Ptak):
    """
    doc orzel
    """

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")

    def wydaj_odglos(self):
        print("piiiiiiii")


class Kura(Ptak):

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def dziobanie(self):
        print("Tu", self.gatunek, "Ide sobie podziobac")

    def wydaj_odglos(self):
        print("kokokokokoko")


# orzel = Ptak("orzel", 10)
# kura = Ptak("kura", 0)
# orzel.latam()
# orzel.wydaj_odglos()
# kura.latam()
# print(orzel.gatunek)
or_2 = Orzel('orzel', 10)
or_2.latam()
or_2.poluj()
kur_2 = Kura("kura")
kur_2.latam()
kur_2.dziobanie()
kur_2.wydaj_odglos()
