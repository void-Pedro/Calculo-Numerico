# Ajustando f(x)=a+b⋅(x−1)² a y=x³−3x num intervalo [x0,x1] pelo método dos mínimos quadrados

import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize

def f(x, a, b):
    return a + b * ((x - 1) ** 2)

def g(x):
    return x ** 3 - 3 * x

def error_squared(a, b):
    integrand = lambda x: (f(x, a, b) - g(x)) ** 2
    error, _ = quad(integrand, -2.9, 0.4)
    return error

# Minimizar o erro quadrático
result = minimize(lambda params: error_squared(params[0], params[1]), x0=[0, 0])

# Resultado
a, b = result.x
print("Parâmetros a e b:")
print("a =", round(a, 6))
print("b =", round(b, 6))