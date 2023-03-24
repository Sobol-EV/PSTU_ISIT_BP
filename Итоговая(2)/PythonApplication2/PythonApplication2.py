import tkinter as tk # использование функций библиотеки TKinter для пользовательского интерфейса
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # использование FigureCanvasTkAgg из библиотеки matplotlib для отрисовки графика на холсте
import matplotlib.pyplot as plt # использование plt из библиотеки matplotlib для формирования графика
import matplotlib # использований функций библиотеки matplotlib для взаимодействия с графиком
from math import * # использование всей библиотеки math для неявной работы с математическими выражениями
import numpy as np # использование библиотеки numpy для работы с вещественными диапазонами

# обновление графика
def update_graph(canvas, start, end, step, x_pad, y_pad, function_expression, is_polar):
    try: # попытка отрисовать график
        x_array = [x for x in np.arange(start, end, step)] # формируем массив значений x
        y_array = [eval(function_expression) for x in x_array] # формируем массив значений y
    
        if is_polar: # если нужен график в полярных координатах
            plt.polar(x_array, y_array) # отрисовываем в полярных координатах
        else: # если нужен график в декартовых координатах
            plt.plot(x_array, y_array) # отрисовываем в декартовых координатах

        plt.xticks(np.arange(start, end, x_pad)) # устанавливаем сетку по x
        plt.yticks(np.arange(min(y_array), max(y_array), y_pad)) # устанавливаем сетку по y
        canvas.draw() # рисуем график на холсте
    except Exception as e: # произошла ошибка
        tk.messagebox.showinfo("Ошибка вычисления", e) # выводим информацию о ошибке

# головная функция 
def main():
    def draw_graph(): # команда отрисовки графика
        update_graph(canvas, # холст
                     float(func_start.get()), # начало диапазона
                     float(func_end.get()), # конец диапазона 
                     float(func_step.get()), # шаг функции
                     float(func_x_pad.get()), # шаг сетки по x 
                     float(func_y_pad.get()), # шаг сетки по y 
                     func_expression.get(), # выражение функции 
                     func_is_polar.get()) # необходимость полярных координат

    def clear_graph(): # команда очистки графика
        plt.clf() # очистка графика
        plt.grid() # установка координатной сетки
        canvas.draw() # отрисовка холста

    root = tk.Tk() # создаем приложение с графическим интерфейсом
    
    plt.grid() # создаем график
    canvas = FigureCanvasTkAgg(plt.figure(1), master=root) # создаем холст
    plot_widget = canvas.get_tk_widget() # создает компонент, на котором будет установлен график и который будет встроен в холст
    
    # значения, которые привязаны к текстовым полям
    # расшифровка значений находится на строке №29
    func_expression = tk.StringVar()
    func_start = tk.StringVar()
    func_end = tk.StringVar()
    func_step = tk.StringVar()
    func_x_pad = tk.StringVar()
    func_y_pad = tk.StringVar()
    func_is_polar = tk.IntVar()
    
    # установка начальных значений для всех параметров графика
    func_start.set('-15')
    func_end.set('15')
    func_step.set('0.1')
    func_x_pad.set('3')
    func_y_pad.set('0.2')
    func_is_polar.set(0)
    func_expression.set('x*sin(x)/(1+x**2)')

    #region UI
    tk.Label(root, text="Выражение").grid(row=0, column=0)
    tk.Entry(root, width=40, textvariable=func_expression).grid(row=1, column=0)

    tk.Label(root, text="Начало интервала").grid(row=0, column=1)
    tk.Entry(root, width=15, textvariable=func_start).grid(row=1, column=1)

    tk.Label(root, text="Конец интервала").grid(row=0, column=2)
    tk.Entry(root, width=15, textvariable=func_end).grid(row=1, column=2)
    
    tk.Label(root, text="Шаг").grid(row=0, column=3)
    tk.Entry(root, width=15, textvariable=func_step).grid(row=1, column=3)
    
    tk.Label(root, text="Шаг сетки по x").grid(row=2, column=1)
    tk.Entry(root, width=15, textvariable=func_x_pad).grid(row=3, column=1)

    tk.Label(root, text="Шаг сетки по y").grid(row=2, column=2)
    tk.Entry(root, width=15, textvariable=func_y_pad).grid(row=3, column=2)
    
    tk.Button(root, text="+", command=lambda: func_expression.set(func_expression.get() + '+')).grid(row=4, column=0, pady=15)
    tk.Button(root, text="-", command=lambda: func_expression.set(func_expression.get() + '-')).grid(row=4, column=1)
    tk.Button(root, text="*", command=lambda: func_expression.set(func_expression.get() + '*')).grid(row=4, column=2)
    tk.Button(root, text="/", command=lambda: func_expression.set(func_expression.get() + '/')).grid(row=4, column=3)
    
    tk.Button(root, text="cos", command=lambda: func_expression.set(func_expression.get() + 'cos')).grid(row=5, column=0, pady=15)
    tk.Button(root, text="sin", command=lambda: func_expression.set(func_expression.get() + 'sin')).grid(row=5, column=1)
    
    tk.Checkbutton(text="Полярные координаты?", variable=func_is_polar).grid(row=5, column=2, pady=15)

    plot_widget.grid(row=6, column=0, columnspan=4, padx=15, pady=15)

    tk.Button(root, text="Построить", command=draw_graph).grid(row=7, column=0, columnspan=2)
    tk.Button(root, text="Очистка", command=clear_graph).grid(row=7, column=2, columnspan=2)
    #endregion
    
    draw_graph() # рисуем график
    root.title("Лабораторная №1 Соболь Е.В")
    root.mainloop() # запускаем приложение

main() # запускаем головную функцию