# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint
arr = [randint(1, 10) for i in range(7)]
print(arr)
maximum = 3
minimum = 1
idx = []
for i in range(len(arr)):
	if minimum <= arr[i] <= maximum:
		idx.append(i)
		print(i)
