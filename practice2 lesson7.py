# Повторите все фуекции и графы , рассмотренные на уроке
def binary_search(array, element, left, right):
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


element = int(input("Введите любое число от 1 до 100: "))
array = [i for i in range(1, 101)]

print(binary_search(array, element, 0, 100))
