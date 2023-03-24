# Задание 4. Вариант 10.
import math
# Функция для вычисления сторон
def func(x, x1, y, y1):
    return math.sqrt(pow((x1-x), 2) + pow((y1-y), 2))
# Входные данные
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
x3 = float(input("Введите x3: "))
y3 = float(input("Введите y3: "))
# Проверка на существование треугольника
if (func(x1, x2, y1, y2) + func(x1, x3, y1, y3) > func(x2, x3, y2, y3)) and \
        (func(x1, x3, y1, y3) + func(x2, x3, y2, y3) > func(x1, x2, y1, y2)) and \
        (func(x1, x2, y1, y2) + func(x2, x3, y2, y3) > func(x1, x3, y1, y3)):
    # Вычисление площади,периметра и вывод результатов
    print("Площадь треугольника равна: ", (1/2)*(abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))))
    print("Периметр треугольника равен: ", func(x1, x2, y1, y2) + func(x1, x3, y1, y3) + func(x2, x3, y2, y3))
else:
     print("Треугольника не существует!")

