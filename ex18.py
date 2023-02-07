# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X

n = int(input("Введите кол-во элементов в массиве: "))
n_array = []

for i in range(n):
    print("Введите элемент массива ({}/{}):".format(i + 1, n), end=" ")
    n_array.append(int(input()))

x = int(input("Введите число X: "))

closest_range = abs(x - n_array[0])
closest_index = 0
for i in range(1, len(n_array)):
    if closest_range > abs(x - n_array[i]):
        closest_range = abs(x - n_array[i])
        closest_index = i

print("Ближайшее к {} значение: {}".format(x, n_array[closest_index]))
