# Задание 1. Вариант 10.
import math
# Функция вычисления
def func(x, y, z):
    return abs(5-2*math.e)/(1 + pow(x, 2)*(y-math.tan(z))), abs(y-4)+(pow((y-x), 2)/6)+(pow((x-y), 2)/7)
# Ввод данныx
x = float(input("Введите X:"))
y = float(input("Введите Y:"))
z = float(input("Введите Z:"))
# Вычисление
a, b = func(x, y, z)
# Вывод данных
print("A={} , B={}".format(a, b))
