import math

# =========================
# ФУНКЦИЯ 1
# =========================

def f1_func(x):
    return x**3 - 3*x**2 + 9*x + 2

def f1_der(x):
    return 3*x**2 - 6*x + 9


# =========================
# ФУНКЦИЯ 2
# =========================

def f2_func(x):
    return math.log10(x) - 7/(2*x + 6)

def f2_der(x):
    return 1/(x * math.log(10)) + 14/((2*x + 6)**2)


# =========================
# МЕТОД НЬЮТОНА
# =========================

def newton_method(f, df, x0, eps=1e-6, max_iter=100):
    x = x0
    step = 0
    
    print(f"{'Шаг':<5} | {'x_i':<12} | {'f(x_i)':<12}")
    print("-" * 40)
    
    while abs(f(x)) > eps and step < max_iter:
        print(f"{step:<5} | {x:<12.8f} | {f(x):<12.8f}")
        
        if df(x) == 0:
            print("Производная равна нулю. Метод остановлен.")
            return None
        
        x = x - f(x)/df(x)
        step += 1
    
    print(f"{step:<5} | {x:<12.8f} | {f(x):<12.8f}")
    print("Корень:", round(x, 8))
    print()
    
    return x


# =========================
# ЗАПУСК
# =========================

print("Решение первой функции:")
newton_method(f1_func, f1_der, x0=-1)

print("Решение второй функции:")
newton_method(f2_func, f2_der, x0=1.5)
