def lagrange_interpolation_with_table(x_nodes, y_nodes, x_target):
    n = len(x_nodes)
    basis_polynomials = []
    terms = []
    final_result = 0.0

    # Заголовок таблицы
    print(f"\nРасчет интерполяции Лагранжа для x = {x_target}")
    print("-" * 85)
    print(f"{'i':<4} | {'x_i':<8} | {'y_i':<8} | {'l_i(x)':<12} | {'y_i * l_i(x)':<15}")
    print("-" * 85)

    for k in range(n):
        # Вычисляем базисный полином l_k(x)
        l_k = 1.0
        for i in range(n):
            if i != k:
                l_k *= (x_target - x_nodes[i]) / (x_nodes[k] - x_nodes[i])
        
        term = y_nodes[k] * l_k
        final_result += term
        
        # Печатаем строку таблицы сразу для экономии памяти
        print(f"{k:<4} | {x_nodes[k]:<8.4f} | {y_nodes[k]:<8.4f} | {l_k:<12.6f} | {term:<15.6f}")

    print("-" * 85)
    print(f"ИТОГОВОЕ ЗНАЧЕНИЕ L(x): {final_result:.6f}")

# --- Ввод данных ---
# Вы можете просто заменить эти списки на свои данные
x_data = [0.08, 0.35, 0.58, 0.76, 0.98, 1.13, 1.30, 1.41, 1.67]
y_data = [-0.66, -1.76, 2.22, 1.44, -2.13, 1.71, 0.20, -1.85, 2.03]

# Запрос точки у пользователя
try:
    target_x = float(input("Введите точку x для расчета (например, 0.656): "))
    lagrange_interpolation_with_table(x_data, y_data, target_x)
except ValueError:
    print("Ошибка: введите числовое значение.")
