# class MyException(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#         self.message = message
#
#
# raise MyException("Wystąpił błąd!")

class MyException(ValueError):
    pass


try:
    x = int(input("Podaj liczbe całkowitą dodatnią"))
    if x < 0:
        raise MyException("Liczba musi byc dodatnia")
except MyException as e:
    print("Wystapił moj wyjątek", e)
except ValueError as e:
    print("Wystąpił bład wartości", e)





