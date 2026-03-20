import matplotlib.pyplot as plt
import numpy as np

def linear_ls_method(x_nodes, y_nodes):
    n = len(x_nodes)
    cx = sum(x_nodes)
    cy = sum(y_nodes)
    cxx = sum(x**2 for x in x_nodes)
    cxy = sum(x*y for x, y in zip(x_nodes, y_nodes))
    
    # Расчет по формулам из вашего учебника
    d = n * cxx - cx**2
    a = (n * cxy - cx * cy) / d
    b = (cxx * cy - cx * cxy) / d
    return a, b

# 1. Исходные данные из таблицы
x_data = np.array([1.32, 1.02, 2.36, 2.14, 2.82, 4.46, 4.80, 5.18, 6.62])
y_data = np.array([1.30, 2.81, 4.30, 2.58, 3.31, 7.43, 7.16, 8.16, 10.80])

# 2. Вычисляем коэффициенты
a, b = linear_ls_method(x_data, y_data)
print(f"Уравнение прямой: y = {a:.4f}x + ({b:.4f})")

# 3. Подготовка данных для графика
# Создаем массив точек для плавной линии прямой
x_line = np.linspace(min(x_data) - 1, max(x_data) + 1, 100)
y_line = a * x_line + b

# 4. Визуализация
plt.figure(figsize=(10, 6))

# Рисуем исходные точки
plt.scatter(x_data, y_data, color='blue', label='Исходные данные (узлы)', zorder=5)

# Рисуем аппроксимирующую прямую
plt.plot(x_line, y_line, color='red', linewidth=2, label=f'МНК: y = {a:.2f}x + ({b:.2f})')

# Отметим искомую точку x = 0.438
target_x = 0.438
target_y = a * target_x + b
plt.scatter(target_x, target_y, color='green', marker='X', s=100, label=f'Точка x={target_x}')

# Оформление
plt.title('Метод наименьших квадратов (линейная аппроксимация)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Показать график
plt.show()
