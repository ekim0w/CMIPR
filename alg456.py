import numpy as np

def get_determinant(A):
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

def solve_kramer(A, B):
    n = len(B)
    main_det = get_determinant(A)
    if abs(main_det) < 1e-12: return None
    
    x = np.zeros(n)
    for i in range(n):
        A_temp = A.copy()
        A_temp[:, i] = B  # Заменяем i-й столбец на вектор B
        x[i] = get_determinant(A_temp) / main_det
    return x

def solve_matrix_inv(A, B):
    try:
        A_inv = np.linalg.inv(A)
        return np.dot(A_inv, B)
    except np.linalg.LinAlgError:
        return None

def main():
    print("=== Универсальный решатель СЛАУ (n x n) ===")
    n = int(input("Введите порядок матрицы n: "))
    
    print(f"Введите строки матрицы A ({n} чисел через пробел):")
    A = np.array([list(map(float, input(f"Строка {i+1}: ").split())) for i in range(n)])
    
    print(f"Введите вектор B ({n} чисел через пробел):")
    B = np.array(list(map(float, input().split())))

    print("\nВыберите метод:")
    print("1 - Гаусс\n2 - Крамер\n3 - Обратная матрица")
    choice = input("Ваш выбор: ")

    res = None
    if choice == '1': res = solve_gauss(A, B)
    elif choice == '2': res = solve_kramer(A, B)
    elif choice == '3': res = solve_matrix_inv(A, B)

    if res is not None:
        print("\nРезультат:")
        for i, val in enumerate(res):
            print(f"x{i+1} = {val:.6f}")
    else:
        print("\nОшибка: определитель равен 0 или матрица вырождена.")

if __name__ == "__main__":
    main()
