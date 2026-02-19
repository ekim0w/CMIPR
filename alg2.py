import math


def f(x):
    return math.log(1 + x) - x ** 2


a_fixed = 0.5 
x_current = 1.0  
m_min = 0.33  
eps = 0.005  

print("Задание 2: Метод хорд")
print(f"{'Шаг (i)':<8} | {'Корень (xi)':<12} | {'В функции (f)':<15} | {'Погрешность'}")
print("-" * 60)

step = 0
# Старт
print(f"{step:<8} | {x_current:<12.6f} | {f(x_current):<15.6f} | {abs(f(x_current)) / m_min:.6f}")

# Цикл: пока погрешность больше заданной точности eps
while abs(f(x_current)) / m_min > eps:
    step += 1

    # Формула метода хорд
    x_current = x_current - (f(x_current) * (x_current - a_fixed)) / (f(x_current) - f(a_fixed))

    print(f"{step:<8} | {x_current:<12.6f} | {f(x_current):<15.6f} | {abs(f(x_current)) / m_min:.6f}")

print(f"\nИтоговый корень с точностью {eps}: {x_current:.6f}")
