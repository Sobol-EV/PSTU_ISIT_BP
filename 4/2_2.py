import numpy as np
# Функция формирующая матрицу n x n
def pol_spiral_n(n):
    # Создаём единичную матрицу n на n
    m = np.eye(n)
    # Массив счётчиков
    z = np.array([1, 0, 0, 0, 1, 0, -1, -2, 2, 0])
    # Цикл заполнения матрицы
    while 1:
        #Условия остановки цикла
        if z[0] > ((1/2)*n + (1/2))*n: break
        #Заполнение в право по горизонтале
        for i in range(z[1], n + z[2]):
            m[z[3]][i] = z[0]
            z[0] += 1
        z[1] += 2
        z[3] += 1
        # Условия остановки цикла
        if z[0] > ((1/2)*n + (1/2))*n: break
        #Заполнение вниз по вертикали
        for i in range(z[4], n + z[5]):
            m[i][n+z[6]] = z[0]
            z[0] += 1
        z[4] += 1
        z[5] -= 2
        z[6] -= 1
        z[9] = n + z[7]
        # Условия остановки цикла
        if z[0] > ((1/2)*n + (1/2))*n: break
        #Заполнение по диагонали
        for i in range(z[8], n + z[2]):
            m[z[9]+z[2]][z[9]] = z[0]
            z[0] += 1
            z[9] -= 1
        z[7] -= 1
        z[8] += 2
        z[2] -= 1
    return m
# Функция формирующая матрицу 2n x 2n
def pol_spiral_2n(matr, n):
    # Создаём матрицу n x 2n
    matr2 = np.zeros((n, 2*n))
    # Заполняем матрицу n x 2n
    for i in range(len(matr2)):
        for j in range(n):
            matr2[i][j] = matr[i][j]
        for j in range(n):
            matr2[i][j+n] = matr[i][j]
    # Возвращаем стакнутую матрицу
    return np.vstack((matr2, matr2))
# Ввод значения n
n = int(input("Введите n: "))
# Вывод результата вызова функции
print(pol_spiral_n(n))
print("")
# Вывод результата вызова функции
print(pol_spiral_2n(pol_spiral_n(n), n))

