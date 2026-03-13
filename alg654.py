import numpy as np

def get_determinant(A):
    # Используем встроенную функцию для точности
    return np.linalg.det(A)

def solve_gauss(A, B):
    n = len(B)
    matrix = np.hstack((A, B.reshape(-1, 1))).astype(float)
    for k in range(n):
        pivot_row = np.argmax(abs(matrix[k:, k])) + k
        matrix[k], matrix[pivot_row] = matrix[pivot_row].copy(), matrix[k].copy()
        pivot = matrix[k, k]
        if abs(pivot) < 1e-12: return None
        matrix[k] /= pivot
        for i in range(k + 1, n):
            matrix[i] -= matrix[i, k] * matrix[k]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i, n] - np.dot(matrix[i, i + 1:n], x[i + 1:n])
    return x

def solve_kramer(A, B, main_det):
    n = len(B)
    x = np.zeros(n)
    for i in range(n):
        A_temp = A.copy()
        A_temp[:, i] = B
        x[i] = get_determinant(A_temp) / main_det
    return x

def main():
    print("=== Универсальный решатель СЛАУ и Определителя ===")
    n = int(input("Введите порядок n: "))
    
    print(f"Введите элементы матрицы A (строки через пробел):")
    A = np.array([list(map(float, input(f"Строка {i+1}: ").split())) for i in range(n)])
    
    print(f"Введите вектор B ({n} чисел через пробел):")
    B = np.array(list(map(float, input().split())))

    # Считаем определитель сразу
    det = get_determinant(A)
    print(f"\n[ИНФО] Определитель матрицы (det A) = {det:.4f}")

    if abs(det) < 1e-12:
        print("Ошибка: Определитель равен 0, система не имеет единственного решения.")
        return

    print("\nВыберите метод решения:")
    print("1 - Метод Гаусса")
    print("2 - Метод Крамера")
    print("3 - Обратная матрица (X = A⁻¹ * B)")
    choice = input("Ваш выбор: ")

    res = None
    if choice == '1':
        res = solve_gauss(A, B)
    elif choice == '2':
        res = solve_kramer(A, B, det)
    elif choice == '3':
        try:
            res = np.dot(np.linalg.inv(A), B)
        except: res = None

    if res is not None:
        print("\n=== РЕЗУЛЬТАТ ===")
        for i, val in enumerate(res):
            print(f"x{i+1} = {val:.6f}")
    else:
        print("Не удалось вычислить решение выбранным методом.")

if __name__ == "__main__":
    main()

