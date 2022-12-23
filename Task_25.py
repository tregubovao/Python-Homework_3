# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Задайте десятичное число: \n'))
m = n
count = ""
while (int(n) > 0):
    count += str(n % 2)
    n //= 2
binary = ""
for i in range(len(count)):
    binary += str(count[len(count)-i - 1])
print(f'Число {m} в двоичном представлении: {binary}')
