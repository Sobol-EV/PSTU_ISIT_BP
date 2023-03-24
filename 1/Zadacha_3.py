# Задание 3. Вариант 10.
import math
# Входные данные
i = 1
m = 3
h = 0.1
# Функция подсчёта F(X)
def func(x):
    # Если встречается корень из отрцательного числа, то берём число по модулю
    return math.sqrt(abs(math.log1p(math.cos(math.sqrt(round(x, 1)))))) \
        if (math.log1p(math.cos(math.sqrt(round(x, 1))))) < 0 \
        else math.sqrt(math.log1p(math.cos(math.sqrt(round(x, 1)))))
# Вычисляется F(X) для каждого X в интервале [i;m] c шагом h
while round(i, 1) <= m:
    print("X=", round(i, 1), " F(X)=", func(round(i, 1)))
    i += h
