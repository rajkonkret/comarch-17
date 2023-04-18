from pprint import pprint


class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f"{self.name!r}, {self.email!r}"
# Adam, adam@wp.pl
# 'Adam', 'adam@wp.pl'


class Suplier(Contact):

    def order(self, order):
        print(f"{order} zamowiono od {self.name}")


c_1 = Contact("Adam", "adam@wp.pl")
c_2 = Contact("Adam", "adam@wp.pl")
c_3 = Contact("Adam", "adam@wp.pl")
c_4 = Contact("Adam", "adam@wp.pl")
s = Suplier("Tomasz", "tomasz@wp.pl")
print(c_1.all_contacts)

print(c_1)
print(s)
s.order("kawa")
print(c_1.all_contacts)
pprint(c_1.all_contacts)
