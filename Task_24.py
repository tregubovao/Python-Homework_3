# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:  - [1.1, 1.2, 3.1, 5, 10.01] => 0.19      1.1 1.2 3.1 5 10.01

n = (input('Задайте список чисел (через пробел): \n').split())
n_float = [float(item) for item in n]                           #  Перевод списка строк в список вещ. чисел
new_list = []
for i in range (len(n)):
    if (n_float[i] - int(n_float[i])) != 0:
        new_list.append(round((n_float[i] - int(n_float[i])), 2))
# можно в одну строчку: print(max(new_list) - min(new_list)),   НО все-таки:
min_el = new_list[0]
max_el = new_list[0]        
for i in range (1, len(new_list)):
    if new_list[i] < min_el:
        min_el = new_list[i]
    if new_list[i] > max_el:
        max_el = new_list[i]    
print(f'Разность MIN и MAX значения дробной части: {max_el - min_el}')   
