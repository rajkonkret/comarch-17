from abc import ABC, abstractmethod


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @staticmethod
    def format_string():
        return "%d"

    @abstractmethod
    def drukuj(self):
        pass

    @classmethod
    def from_other(cls, counter):
        return cls(counter.values)


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            raise ValueError("Wartość nie może przekroczyc MAX")
        super(BoundedCounter, self).__init__(values)

    def increment(self, by=1):
        super(BoundedCounter, self).increment()
        self.values = min(self.values, self.MAX)

    def drukuj(self):
        print("Drukuje....", self.values)


Counter.format_string()
b = BoundedCounter(34)
# b_2 = BoundedCounter(101)
b.increment()
b.drukuj()

c = BoundedCounter.from_other(b)
b.drukuj()
c.drukuj()
