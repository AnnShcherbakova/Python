# Написать функцию, которая будет перемножать любое количество переданных ей аргументов
def mult(*args):
    a = 1
    for i in args:
        a *= i
    return a
print(mult(2, 3, 4, 5, 6, 7))