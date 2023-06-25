# Повторите все фуекции и графы , рассмотренные на уроке
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):  # проходим по всему массиву
    ind_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] < array[ind_min]:
            ind_min = j
    if i != ind_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[ind_min] = array[ind_min], array[i]

print(array)
