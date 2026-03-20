import numpy as np

def lagrange_interpolation(x_nodes, y_nodes, x_target):
    """
    Универсальная функция интерполяции Лагранжа.
    x_nodes: список или массив координат X
    y_nodes: список или массив координат Y
    x_target: точка, в которой ищем значение
    """
    n = len(x_nodes)
    result = 0.0
    
    for k in range(n):
        # Вычисляем базисный полином l_k(x)
        basis = 1.0
        for i in range(n):
            if i != k:
                basis *= (x_target - x_nodes[i]) / (x_nodes[k] - x_nodes[i])
        
        # Добавляем слагаемое y_k * l_k(x) в общую сумму
        result += y_nodes[k] * basis
        
    return result

# --- Основной блок программы ---
if __name__ == "__main__":
    print("--- Интерполяция многочленом Лагранжа ---")
    
    # Ввод данных (можно ввести через запятую или пробел)
    try:
        x_input = input("Введите узлы X через пробел: ").split()
        x_points = [float(x) for x in x_input]
        
        y_input = input("Введите значения Y через пробел: ").split()
        y_points = [float(y) for y in y_input]
        
        if len(x_points) != len(y_points):
            print("Ошибка: количество X и Y должно совпадать!")
        else:
            target = float(input("Введите точку x для расчета: "))
            
            res = lagrange_interpolation(x_points, y_points, target)
            
            print("-" * 30)
            print(f"Результат в точке {target}: {res:.6f}")
            
    except ValueError:
        print("Ошибка: вводите только числа.")
