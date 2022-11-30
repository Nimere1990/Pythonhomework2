# 3 - Дан массив размера N. 
# После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random

N = abs(int(input('Введите количество элементов массива:\n')))
new_list = []
for i in range(N):
    new_list.append(random.randint(-100, 100))
print(new_list)
for k, item in enumerate(new_list):
    if item < 0:
        new_list.insert(k+1, 0)
print("Массив с нулями:",new_list)