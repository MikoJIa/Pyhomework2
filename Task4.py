#Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода
#и зависит от количества элементов в списке) в одной строке одно число. 
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2
import random
from turtle import position

N = int(input('Enter number N - '))
with open('Newfile.txt', 'w') as data:
    random_position = random.randrange(1, N)
    for i in range(0,random_position):
        data.writelines(str(random.randrange(0, N + 1)))
position = 1
list = []
for i in range(-N, N):
    list.append(i)
print(list)

path = 'Newfile.txt'
data = open(path, 'r')
for line in data:
    position *= line
print(line)

   

