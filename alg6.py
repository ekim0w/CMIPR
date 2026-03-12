import numpy as np


def calculate_determinant(A):
    n = len(A)

    matrix = A.astype(float)
    det = 1.0

    for k in range(n):

        pivot_row = k
        for i in range(k + 1, n):
            if abs(matrix[i, k]) > abs(matrix[pivot_row, k]):
                pivot_row = i


        if abs(matrix[pivot_row, k]) < 1e-12:
            return 0.0


        if pivot_row != k:
            matrix[k], matrix[pivot_row] = matrix[pivot_row].copy(), matrix[k].copy()
            det *= -1


        det *= matrix[k, k]

        pivot = matrix[k, k]
        for i in range(k + 1, n):
            factor = matrix[i, k] / pivot
            for j in range(k + 1, n):
                matrix[i, j] -= factor * matrix[k, j]

    return det


def main():
    try:
        print("=== Вычисление определителя матрицы методом Гаусса ===")
        n = int(input("Введите порядок матрицы (n): "))

        print(f"\nВведите элементы матрицы по строкам (через пробел):")
        matrix_data = []
        for i in range(n):
            row = list(map(float, input(f"Строка {i + 1}: ").split()))
            if len(row) != n:
                print(f"Ошибка: в строке должно быть {n} элементов!")
                return
            matrix_data.append(row)

        A = np.array(matrix_data)

        result = calculate_determinant(A)

        print("\n=== Результат ===")
        print(f"Определитель матрицы (det A) = {result:.4f}")

    except ValueError as e:
        print(f"\nОшибка ввода: {e}")


if __name__ == "__main__":
    main()
