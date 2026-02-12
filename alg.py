import math

print("ВВЕДИТЕ ФУНКЦИЮ ОТ x")
print("Например: x*log10(x+1)-1")
print("Доступно: sin, cos, tan, log, log10, exp, sqrt, abs, pi, e")
func_str = input("f(x) = ")

print("ВВЕДИТЕ КОНЦЫ ПРОМЕЖУТКА")
a = float(input())
b = float(input())

print("ВВЕДИТЕ ТОЧНОСТЬ")
e = float(input())

def f(x):
    return eval(func_str, {
        "x": x,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log,
        "log10": math.log10,
        "exp": math.exp,
        "sqrt": math.sqrt,
        "abs": abs,
        "pi": math.pi,
        "e": math.e
    })

while b - a > 2 * e:
    c = (a + b) / 2
    if f(a) * f(c) > 0:
        a = c
    else:
        b = c

print(f"ЗНАЧЕНИЕ КОРНЯ С ТОЧНОСТЬЮ {e} РАВНО {(a + b) / 2}")
