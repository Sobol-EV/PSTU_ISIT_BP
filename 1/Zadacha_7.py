# Задание 7. Вариант 10.
# Ввод данных
x = float(input("Введите X:"))
# Проверка валидности введённых данных
if (x < -10) or (x > 10):
    print("Допустимые значения X [-10;10]")
    exit()
# Вычисление и вывод ответа
print("y=", 3*pow(x, 6)-6*pow(x, 2)-7)