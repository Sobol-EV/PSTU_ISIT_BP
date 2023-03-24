# Задание 2. Вариант 10.
# Начальные значения
a = 2
b = -1
h = 0.15
i = 4
m = 5.5
# функция вычисления f(x)
def func(x, a, b):
    return (a * (pow(round(x, 2), b) + round(x, 2))/3) - pow(round(x, 2), 3/4)
# Вычисляем F(x) для каждого x принадлежащего отрезку [i;m] c шагом h
while round(i, 2) <= m:
    print("X=", round(i, 2), " F(X)=", func(i, a, b))
    i += h
