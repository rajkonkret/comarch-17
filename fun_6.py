def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2


xFun = fun1()
print(type(xFun))
xFun()


def kantor(waluta):
    print("To jest kantor")

    def dolary(kwota):
        print("Wymieniam dolary")

    def euro(kwota):
        print("wymieniam euro")

    if waluta == 'eur':
        return euro
    else:
        return dolary


kantor = kantor('eur')
kantor(100)
# 11:20


