'''3. Задайте последовательность чисел. Напишите
программу, которая выведет список неповторяющихся
элементов исходной последовательности.
'''

list_1 = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Список 1: {list_1}")
list_2 = []
[list_2.append(i) for i in list_1 if i not in list_2]
print(f"Список 2 без повторов: {list_2}")