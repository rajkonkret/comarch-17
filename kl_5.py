from typing import Optional

class Sample:
    def __init__(self, a, b, c, d, e: Optional[str] = None):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def __repr__(self):
        if self.d is None:
            self.d = 'nieznany'
        if self.e is None:
            self.e = 'nieznany'
        return(f"""
        a = {self.a}
        b = {self.b}
        c = {self.c}
        d = {self.d}
        e = {self.e}
    """)


wyn = Sample(1, 2, 3, 4)
print(wyn)
wyn = Sample(1, 2, 3, None)
print(wyn)