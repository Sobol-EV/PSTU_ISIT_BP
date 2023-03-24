# Лабораторная работа № 3. Задание 1. Вариант 10.
niz = 0
ver = 0
st = input("Введите строку:")
for i in range(len(st)):
    # Если символ прописной, счётчик +1
    if st[i].islower():
        niz += 1
    # Если символ заглавный, счётчик +1
    if st[i].isupper():
        ver += 1
# Сравнение счётчиков, и преобразование строки
st = st.lower() if niz >= ver else st.upper()
print(st)
