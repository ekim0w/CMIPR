import numpy as np


def solve_gauss(A, B):
    n = len(B)
    matrix = np.hstack((A, B.reshape(-1, 1))).astype(float)

    for k in range(n):

        pivot_row = np.argmax(abs(matrix[k:, k])) + k
        if abs(matrix[pivot_row, k]) < 1e-12:
            raise ValueError("Система не имеет однозначного решения.")

        matrix[k], matrix[pivot_row] = matrix[pivot_row].copy(), matrix[k].copy()

        pivot = matrix[k, k]
        matrix[k] /= pivot

        for i in range(k + 1, n):
            factor = matrix[i, k]
            matrix[i] -= factor * matrix[k]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i, n] - np.dot(matrix[i, i + 1:n], x[i + 1:n])
    return x


def main():
    try:
        print("Решение СЛАУ методом Гаусса")
        n = int(input("Введите порядок матрицы (n): "))

        print(f"\nВведите коэффициенты матрицы A (по строкам, через пробел):")
        A = []
        for i in range(n):
            row = list(map(float, input(f"Строка {i + 1}: ").split()))
            if len(row) != n:
                print(f"Ошибка: в строке должно быть {n} элементов!")
                return
            A.append(row)

        print(f"\nВведите свободные члены B (через пробел):")
        B = list(map(float, input("Вектор B: ").split()))
        if len(B) != n:
            print(f"Ошибка: вектор B должен содержать {n} элементов!")
            return

        A = np.array(A)
        B = np.array(B)

        res = solve_gauss(A, B)

        print("\n=== Результат ===")
        for i, val in enumerate(res):
            print(f"x{i + 1} = {val:.6f}")

    except ValueError as e:
        print(f"\nОшибка ввода или решения: {e}")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")


if __name__ == "__main__":
    main()
