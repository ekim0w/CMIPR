import math

def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("❌ Размер должен быть > 0")
                continue
            return value
        except:
            print("❌ Введите целое число")


def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("❌ Введите число")


def input_row(n, i):
    while True:
        try:
            row = list(map(float, input(f"Строка {i+1}: ").split()))
            if len(row) != n:
                print(f"❌ Нужно ввести ровно {n} чисел")
                continue
            return row
        except:
            print("❌ Ошибка ввода, попробуйте снова")

n = input_int("Введите размер матрицы n: ")

print("Введите матрицу A:")
A = [input_row(n, i) for i in range(n)]

print("Введите вектор B:")
while True:
    try:
        B = list(map(float, input().split()))
        if len(B) != n:
            print(f"❌ Нужно ввести {n} чисел")
            continue
        break
    except:
        print("❌ Ошибка ввода")

eps = input_float("Введите точность epsilon: ")

def check_diagonal(A):
    for i in range(len(A)):
        if A[i][i] == 0:
            print(f"❌ Ошибка: A[{i+1}][{i+1}] = 0 (деление невозможно)")
            return False
    return True


def is_diagonally_dominant(A):
    ok = True
    for i in range(len(A)):
        diag = abs(A[i][i])
        s = sum(abs(A[i][j]) for j in range(len(A)) if j != i)
        if diag < s:
            ok = False
    return ok


def norm(x, y):
    return max(abs(x[i] - y[i]) for i in range(len(x)))

def step(A, B, x):
    n = len(A)
    new_x = [0] * n

    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += A[i][j] * x[j]

        new_x[i] = (B[i] - s) / A[i][i]

    return new_x

def solve(A, B, eps):
    n = len(A)
    x_old = [0] * n
    iteration = 0
    max_iter = 1000

    print("\nТаблица итераций:")
    print("k\t" + "\t".join([f"x{i+1}" for i in range(n)]))

    while True:
        x_new = step(A, B, x_old)

        print(f"{iteration}\t" + "\t".join(f"{v:.6f}" for v in x_new))

        if norm(x_old, x_new) <= eps:
            return x_new, iteration

        if iteration > max_iter:
            print("❌ Метод не сошелся (слишком много итераций)")
            return None, iteration

        x_old = x_new
        iteration += 1


if not check_diagonal(A):
    exit()

if not is_diagonally_dominant(A):
    print("⚠️ Нет диагонального преобладания — метод может не сойтись\n")

solution, iters = solve(A, B, eps)

if solution:
    print("\nРешение:")
    for i, val in enumerate(solution):
        print(f"x{i+1} = {val:.6f}")

    print(f"\nИтераций: {iters}")

    print("\nПроверка (Ax ≈ B):")
    for i in range(n):
        s = sum(A[i][j] * solution[j] for j in range(n))
        print(f"{s:.6f} ≈ {B[i]:.6f}")
