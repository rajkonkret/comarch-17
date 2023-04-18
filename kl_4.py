import math


class MyClass:
    """
    Reprezentuje punkty x i y
    """

    def __init__(self, x=0, y=0):
        """
        Metoda inicjalizujaca
        :param x: x
        :param y: y
        """
        self.move(x, y)

    def reset(self):
        self.move(0, 0)

    def move(self, x, y):
        self.x = x
        self.y = y

    def calculate(self, other: "MyClass") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"x = {self.x}, y = {self.y}"


ob = MyClass()
print(ob)
print(ob.x)
ob.move(45, 67)
print(ob.y)
ob.reset()
print(ob.x)
a = MyClass(3, 5)
b = MyClass(0, 5)
print(a.x)
print(b.calculate(a))