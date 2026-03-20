import pandas as pd

def lagrange_with_steps(x_nodes, y_nodes, x_target):
    n = len(x_nodes)
    basis_polynomials = []
    terms = []
    
    final_result = 0.0
    
    for k in range(n):
        # Вычисляем l_k(x)
        l_k = 1.0
        for i in range(n):
            if i != k:
                l_k *= (x_target - x_nodes[i]) / (x_nodes[k] - x_nodes[i])
        
        term = y_nodes[k] * l_k
        final_result += term
        
        # Сохраняем для таблицы
        basis_polynomials.append(round(l_k, 6))
        terms.append(round(term, 6))
    
    # Создаем красивую таблицу через pandas
    df = pd.DataFrame({
        'i': range(n),
        'x_i': x_nodes,
        'y_i': y_nodes,
        'l_i(x)': basis_polynomials,
        'y_i * l_i(x)': terms
    })
    
    return final_result, df

# Данные из вашего задания
x_data = [0.08, 0.35, 0.58, 0.76, 0.98, 1.13, 1.30, 1.41, 1.67]
y_data = [-0.66, -1.76, 2.22, 1.44, -2.13, 1.71, 0.20, -1.85, 2.03]
target_x = 0.656

result, table = lagrange_with_steps(x_data, y_data, target_x)

print(f"Расчет интерполяции Лагранжа для x = {target_x}:")
print("-" * 60)
print(table.to_string(index=False))
print("-" * 60)
print(f"ИТОГО (сумма последнего столбца): {result:.6f}")
