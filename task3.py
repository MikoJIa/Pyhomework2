# Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.


n = int(input('Enter number - '))
def squerence(n):
    return [round((1 + 1/n)**n) for n in range(1, n + 1)]
res = squerence(n)
print(res)
print(sum(res))