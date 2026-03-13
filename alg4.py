import math

def solve_fixed_point(x0, eps):
    """
    x0 - начальное приближение
    eps - точность (например, 0.001)
    """
    # Определяем функцию f(x) из уравнения x = f(x)
    # Для 2 - x - ln(x) = 0 => x = 2 - ln(x)
    def f(x):
        return 2 - math.log(x)

    print(f"{'Итер.':<10} | {'x_i':<12} | {'Разность':<12}")
    print("-" * 40)

    x1 = x0
    x2 = f(x1)
    iteration = 1
    
    # Условие выхода: разница между соседними итерациями меньше точности
    while abs(x2 - x1) > eps:
        print(f"{iteration:<10} | {x2:<12.6f} | {abs(x2 - x1):<12.6f}")
        
        x1 = x2
        x2 = f(x1)
        iteration += 1
        
        # Защита от бесконечного цикла
        if iteration > 1000:
            print("Метод не сходится!")
            return None

    print("-" * 40)
    return x2

# Ввод данных
try:
    start_x = float(input("Введите начальное приближение (x0): "))
    precision = float(input("Введите точность (например, 0.001): "))

    root = solve_fixed_point(start_x, precision)
    
    if root:
        print(f"Корень уравнения: {root:.6f}")
except Exception as e:
    print(f"Ошибка: {e}")
