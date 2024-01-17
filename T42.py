def newton_interpolation(points):
    n = len(points)
    x_values, y_values = zip(*points)

    # Calcula as diferenças divididas
    def divided_differences(x, y, n):
        if n == 1:
            return y[0]
        else:
            return (divided_differences(x[1:], y[1:], n - 1) - divided_differences(x[:-1], y[:-1], n - 1)) / (x[n - 1] - x[0])

    # Calcula o termo do polinômio para um dado grau
    def newton_term(i, x_values):
        if i == 0:
            return "1"
        else:
            term = f"(x - {x_values[0]})"
            for j in range(1, i):
                term = term + f"(x - {x_values[j]})"
            return term

    polynomial = f"{divided_differences(x_values, y_values, n):.4f}"
    for i in range(1, n):
        polynomial_term = f" + {divided_differences(x_values[:i+1], y_values[:i+1], i + 1):.4f} * {newton_term(i, x_values)}"
        polynomial += polynomial_term

    return polynomial

# Exemplo de uso
points = [(-8, 5), (-6, 0), (-2, -1), (2, 0), (4, -3), (7, -5)]
result = newton_interpolation(points)
print(f"A equação interpoladora é: f(x) = {result}")
# Exemplo de uso
