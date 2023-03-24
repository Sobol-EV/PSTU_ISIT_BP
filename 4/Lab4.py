import numpy as np
from numpy import linalg as la


# Создаём класс
class Lab4:
    # Метод для решения задачи 1А
    @staticmethod
    def task_1a():
        return np.array([[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12]]).transpose(), \
               np.array([[1, 2, 8], [3, 4, 7], [5, 6, 9]]).transpose()

    # Метод для решения задачи 1В
    @staticmethod
    def task_1b(n, m):
        # Вычисляем и выводим определитель созданной матрицы
        return la.det(np.array([[m + n, n, m], [-n, m - n, -m], [1, -2, 3]]))

    # Метод для решения задачи 1С
    @staticmethod
    def task_1c(n, m):
        # Создаём матрицу
        a = np.array([[m, n, m + n], [n, m - n, m], [2, 1, 2]])
        # Создаём обратную матрицу
        b = la.inv(a)
        print(b)
        # Сравнение произведения матрицы A и B с единичной матрицей
        if np.array_equal(np.dot(a, b), np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])):
            return True
        return False

    # Метод для решения задачи 1G
    @staticmethod
    def task_1g(n, m):
        # Создаём матрицы и вычисляем 1 вырожение и вычисляем 2 выражение
        return np.dot(np.array([[m - n, n], [2, 0], [m + n, -m]]), 2) - np.dot(np.array([[2 * m, 1], [n, -m], [2, n]]),
                                                                               3), \
               np.dot(np.array([[1, m, n + 1], [0, 2 * n, -2], [3, 1, m]]), np.array([[m, 2], [-1, n], [3, -2]]))

    # Метод для решения задачи 2_1
    @staticmethod
    def task_2_1(n):
        # Создаём единичную матрицу размером N x N
        m = np.eye(n)
        # Строка
        for i in range(n):
            # Столбец
            for j in range(i, n):
                m[i][j] = j + 1
        return m

    # Метод формирующий матрицу n x 2 для задания 2_2
    @staticmethod
    def __pol_spiral_n(n):
        # Создаём единичную матрицу n на n
        m = np.eye(n)
        # Массив счётчиков
        z = np.array([1, 0, 0, 0, 1, 0, -1, -2, 2, 0])
        # Цикл заполнения матрицы
        while 1:
            # Условия остановки цикла
            if z[0] > ((1 / 2) * n + (1 / 2)) * n:
                break
            # Заполнение в право по горизонтале
            for i in range(z[1], n + z[2]):
                m[z[3]][i] = z[0]
                z[0] += 1
            z[1] += 2
            z[3] += 1
            # Условия остановки цикла
            if z[0] > ((1 / 2) * n + (1 / 2)) * n:
                break
            # Заполнение вниз по вертикали
            for i in range(z[4], n + z[5]):
                m[i][n + z[6]] = z[0]
                z[0] += 1
            z[4] += 1
            z[5] -= 2
            z[6] -= 1
            z[9] = n + z[7]
            # Условия остановки цикла
            if z[0] > ((1 / 2) * n + (1 / 2)) * n:
                break
            # Заполнение по диагонали
            for i in range(z[8], n + z[2]):
                m[z[9] + z[2]][z[9]] = z[0]
                z[0] += 1
                z[9] -= 1
            z[7] -= 1
            z[8] += 2
            z[2] -= 1
        return m

    # Метод формирующий матрицу 2n x 2n для задания 2_2
    @staticmethod
    def __pol_spiral_2n(matr, n):
        # Создаём матрицу n x 2n
        matr2 = np.zeros((n, 2 * n))
        # Заполняем матрицу n x 2n
        for i in range(len(matr2)):
            for j in range(n):
                matr2[i][j] = matr[i][j]
            for j in range(n):
                matr2[i][j + n] = matr[i][j]
        # Возвращаем стакнутую матрицу
        return np.vstack((matr2, matr2))

    # Метод для решения задачи 2_2
    @staticmethod
    def task_2_2(n):
        return Lab4.__pol_spiral_n(n), Lab4.__pol_spiral_2n(Lab4.__pol_spiral_n(n), n)


# Создаём экземпляр класса
L4 = Lab4()

print("Лабораторная 4, Задание 1 А. ")
print("------------------------------")
a, b = L4.task_1a()
print(a)
print(b, "\n")

print("Лабораторная 4, Задание 1 B. ")
print("------------------------------")
# Вводим n
n1 = int(input("n: "))
# Вводим m
m1 = int(input("m: "))
print(f"Определитель равен:{L4.task_1b(n1, m1)} . \n")

print("Лабораторная 4, Задание 1 C. ")
print("------------------------------")
# Вводим n
n1 = int(input("n: "))
# Вводим m
m1 = int(input("m: "))
if L4.task_1c(n1, m1):
    print("A*A^-1 = E \n")
else:
    print("A*A^-1 != E \n")

print("Лабораторная 4, Задание 1 G. ")
print("------------------------------")
# Вводим n
n1 = int(input("n: "))
# Вводим m
m1 = int(input("m: "))
a, b = L4.task_1g(n1, m1)
# Вывод результата 1 выражения
print(a)
# Вывод результата 2 выражения
print(b, "\n")

print("Лабораторная 4, Задание 2.1 ")
print("------------------------------")
# Вводим n
n1 = int(input("n: "))
# Выводим матрицу
print(L4.task_2_1(n1), "\n")

print("Лабораторная 4, Задание 2.2 ")
print("------------------------------")
# Вводим n
n1 = int(input("n: "))
a, b = L4.task_2_2(n1)
# Вывод матрицы NxN
print(a)
# Вывод матрицы 2Nx2N
print(b, "\n")
