def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False


array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
element = int(input("Введите любое число: "))