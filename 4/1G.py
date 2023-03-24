import numpy as np
from numpy import linalg as LA
# B
# Вводим n
n = int(input("n: "))
# Вводим m
m = int(input("m: "))
# Создаём матрицу
a = np.array([[m-n, n], [2, 0], [m+n, -m]])
# Создаём матрицу
b = np.array([[2*m, 1], [n, -m], [2, n]])
# Создаём матрицу
c = np.array([[1, m, n+1], [0, 2*n, -2], [3, 1, m]])
# Создаём матрицу
d = np.array([[m, 2], [-1, n], [3, -2]])
print("-------------------------")
# Вычисляем и выводим первое вырожение
print(np.dot(np.array([[m-n, n], [2, 0], [m+n, -m]]), 2) - np.dot(np.array([[2*m, 1], [n, -m], [2, n]]), 3))
print("-------------------------")
# Вычисляем и выводим второе выражение
print(np.dot(np.array([[1, m, n+1], [0, 2*n, -2], [3, 1, m]]), np.array([[m, 2], [-1, n], [3, -2]])))

