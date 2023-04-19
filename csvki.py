import csv

fields = ['name', 'branch', 'year', 'cgpa']
# pliki csv to pliki gdzie wartosci oddzielone sa znakiem rozdziału(,;tab)
row = ['radek', 'COE', '1', '9.1']
my_dict = [
    {'branch': 'COK', 'cgpa': '9.1', 'name': "Radek", 'year': '2'},
    {'branch': 'POK', 'cgpa': '9', 'name': "Radek", 'year': '3'},
    {'branch': 'ZOE', 'cgpa': '6', 'name': "Radek", 'year': '1'},
    {'branch': 'CoS', 'cgpa': '6.1', 'name': "Radek", 'year': '1'},
]

file = 'records.csv'

with open(file, 'w', newline='') as csv_f:
    cswriter = csv.DictWriter(csv_f, fieldnames=fields)
    cswriter.writeheader()
    cswriter.writerows(my_dict)

