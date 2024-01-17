import math

def f(x):
    # Defina a função que deseja integrar aqui
    return math.exp(-x**2)

def truncate(x):
    return int(x * 10**8) / 10**8

def simpson_integral(a, b, n):
    h = (b - a) / (2*n)
    integral_sum = f(a)  # First term: f(a)
    k = 4
    for i in range(1, 2*n):
        xi = a + (i * h)
        integral_sum += (k * f(xi))  # Middle terms: f(x_i)
        k = (k+2)%4
        if k==0: k = 4
    integral_sum += f(b)  # Last term: f(b)/2
    integral_result = h * integral_sum / 3
    return integral_result

def simpsoncprecisão(a, b):
    n = 2
    while True:
        integral_n_minus_1 = simpson_integral(a, b, n - 1)
        integral_n = simpson_integral(a, b, n)
        if truncate(integral_n_minus_1) == truncate(integral_n):
            return integral_n, n
        n += 1
        if n >= 100:
            return integral_n, n

# Intervalo de integração
a = -1.2
b = 2.2

integral_value, n = simpsoncprecisão(a, b)
print(f"O valor numérico da integral é: {integral_value}")
print(n)