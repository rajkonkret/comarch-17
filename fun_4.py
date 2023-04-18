def liczby(c, *cyfry):
    suma = 0
    print(c)
    print(cyfry)
    count = len(cyfry)
    for i in cyfry:
        suma += i
    print(suma)
    try:
        print(suma / count)
    except:
        print("Nie dziel przez zero")


liczby(5)
liczby(5, 4, 7, 8, 9, 10, 11, 88, 99, 100, 4, 5, 7, 9)


def connect(**opcje):
    conn_param = {
        'host': '127.0.0.7',
        'port': '8080',
        'user': 'admin',
        'pass': '12345'
    }
    print(conn_param)
    conn_param['param'] = opcje
    print(opcje)
    print(conn_param)


connect()
connect(root="/")
connect(root="/", user="/usr", i="zenek", w="zenek")
