# НЕОБЯЗАТЕЛЬНАЯ Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Задайте число: \n'))
new_list = [1, 1]
for i in range(2, n):   
    new_list.append(new_list[i - 1] + new_list[i - 2])
for i in range(n):
    if i % 2 != 0:
        new_list[i] = - new_list[i]
new_list.reverse()
new_list.insert(n, 0)
for i in range(n + 1, 2 * n + 1):   
    new_list.append(new_list[i - 1] + new_list[i - 2])
print(new_list)