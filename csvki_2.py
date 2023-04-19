import csv

fields = []
rows = []
filename = 'records.csv'

with open(filename, 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

# yield - sekwencyjny dostep
print(fields)
print(rows)