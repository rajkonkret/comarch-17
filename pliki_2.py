fh = open('dane.txt', 'w')
fh.write("Test nr 1\n")
fh.write("Test nr 2\n")
fh.write("Test nr 3\n")
fh.close()

with open('dane.txt', 'r') as fh:
    for line in fh:
        print(line.strip())  # strip() - usuniecie białych znaków

lista = [1, 2, 3, 4]

with open('dane.txt', 'w') as fh:
    fh.write(str(lista))

lista_2 =[]

with open('dane.txt', 'r') as fh:
    for line in fh:
        lista_2.append(line.strip())

print(lista_2)
