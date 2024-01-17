import numpy as np

# Definir a equação diferencial x' = f(t, x)
def f(t, x):
    return 0.1 * x**2 - 0.58 * np.sin(t)

# Condição inicial
x0 = 1.0

# Intervalo [a, b]
a = 0.0
b = 0.6

# Passo
h = 0.1

# Número de pontos
num_points = int((b - a) / h) + 2

# Inicializar arrays para armazenar os resultados
t_values = np.linspace(a, b, num_points)
x_values = np.zeros(num_points)
x_values[0] = x0

# Aplicar o método de Euler
for i in range(1, num_points):
    x_values[i] = x_values[i - 1] + h * f(t_values[i - 1], x_values[i - 1])
    print(f'{x_values[i]:,.12f}')
