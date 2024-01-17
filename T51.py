import math

def truncate(x):
    return int(x * 10**8) / 10**8

def f(x):
    return math.exp(x) / x

def trapezoidal_integral(a, b, n):
    h = (b - a) / n 
    integral_sum = f(a) / 2  # First term: f(a)/2
    for i in range(1, n):
        xi = a + i * h
        integral_sum += f(xi)  # Middle terms: f(x_i)
    integral_sum += f(b) / 2  # Last term: f(b)/2
    integral_result = h * integral_sum
    return integral_result

def calculate_integral_with_precision(a, b):
    n = 2
    while True:
        integral_n_minus_1 = trapezoidal_integral(a, b, n - 1)
        integral_n = trapezoidal_integral(a, b, n)
        if truncate(integral_n_minus_1) == truncate(integral_n):
            return integral_n, n
        n += 1

# Intervalo de integração
a = 1.2
b = 2.2

result, n = calculate_integral_with_precision(a, b)
print(f'n = {n}')
print("Valor numérico da integral:", truncate(result))