# Лабораторная работа № 3. Задание 2. Вариант 10.

while 1:
    n1 = input("Введите первое число:")
    n2 = input("Введите второе число:")
    # Проверяем что оба введённых значения являются числами
    if n1.isdigit() and n2.isdigit():
        # Выводим сумму
        print(int(n1) + int(n2))
        break
    print("Вы ввели не число! Повторите попытку!")