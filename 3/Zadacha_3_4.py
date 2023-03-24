import random

def ra(a, b):
    return random.randint(a, b)

def krt10(a, b):
    return (ra(a, b), ra(a, b), ra(a, b), ra(a, b), ra(a, b), ra(a, b), ra(a, b), ra(a, b), ra(a, b), ra(a, b))

k = 0

a1 = krt10(0, 5)
a2 = krt10(-5, 0)
a3 = a1 + a2

for i in range(len(a3)):
    if str(a3[i]).count("0"):
        k += 1

print("Первый кортеж:", a1)
print("Второй кортеж:", a2)
print("Третий кортеж:", a3)
print("Количество нулей:", k)
