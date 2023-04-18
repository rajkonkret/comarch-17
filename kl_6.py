class Car:
    """
    Klasa samochod
    """

    def __init__(self, model, year):
        self.model = model
        self. year = year
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def hamuj(self):
        self.__predkosc -= 10

    def licznik(self):
        print("Prędkość wynosi", self.__predkosc)

    def __zmien_bieg(self):
        print("zmiana biegu")


car_1 = Car('Opel', '2018')
car_1.gaz()
car_1.gaz()
car_1.gaz()
car_1.gaz()
car_1.gaz()
car_1.licznik()
car_1.hamuj()
car_1.hamuj()
car_1.hamuj()
car_1.hamuj()
car_1.hamuj()
car_1.licznik()

# 14:45