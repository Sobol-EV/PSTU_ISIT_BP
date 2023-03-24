import numpy as np

# Вводим n
n = int(input("n: "))
# Создаём единичную матрицу размером N x N
m = np.eye(n)
# Строка
for i in range(n):
    # Столбец
    for j in range(i, n):
        m[i][j] = j+1
# Выводим матрицу
print(m)




