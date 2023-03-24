import numpy as np
from numpy import linalg as LA
# B
# Вводим n
n = int(input("n: "))
# Вводим m
m = int(input("m: "))
# Создаём матрицу
a = np.array([[m, n, m+n], [n, m-n, m], [2, 1, 2]])
# Создаём обратную матрицу
b = LA.inv(a)
print(b)
# Сравнение произведения матрицы A и B с единичной матрицей
if np.array_equal(np.dot(a, b), np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])):
    print("A*A^-1 = E")
else:
    print("A*A^-1 != E, скорее всего из запогрешности")

