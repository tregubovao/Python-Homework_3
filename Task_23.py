# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример: 
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = (input('Задайте список чисел (через пробел): \n').split())
new_list = []
if len(n) % 2 == 0:
    for i in range (int((len(n)) / 2)):    
        new_list.append(int(n[i]) * int(n[(len(n) - 1 - i)]))
else:
    for i in range (int((len(n)) / 2) + 1):        
        new_list.append(int(n[i]) * int(n[(len(n) - 1 - i)]))
print(new_list)