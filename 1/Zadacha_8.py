# Задание 8. Вариант 10.
# Ввод данных
a1 = float(input("Введите A1:"))
b1 = float(input("Введите B1:"))
c1 = float(input("Введите C1:"))
a2 = float(input("Введите A2:"))
b2 = float(input("Введите B2:"))
c2 = float(input("Введите C2:"))
# Проверка валидности данных
if (a1 > 10) or (b1 > 10) or (c1 > 10) or \
        (a2 > 10) or (b2 > 10) or (c2 > 10) or \
        (a1 < -10) or (b1 < -10) or (c1 < -10) or\
        (a2 < -10) or (b2 < -10) or (c2 < -10):
    print("Введённые данные должны соответствовать условию -10 <= a1,b1,c1,a2,b2,c2 <=10 !")
    exit()
# Вычисление d
d = a1*b2 - a2*b1
# Если D =0
if d == 0:
    print("X и Y равны бесконечности. Т.K d=0")
    exit()
# Вычисление и форматированный вывод
print("----------------------------------")
print("X= {:0.4f}".format((c1*b2-c2*b1)/d))
print("Y= {:0.4f}".format((a1*c2-a2*c1)/d))