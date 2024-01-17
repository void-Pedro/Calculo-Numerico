from sympy import symbols, Rational

# Pontos de interpolação
points = [(-4, 6), (-3, 10), (2, 0), (4, -10)]

# Variável t
t = 0.72

# Coeficientes dos polinômios de Lagrange
a = []
b = []
c = []
d = []

# Cálculo dos coeficientes
for i in range(len(points)):
    L = 1
    for j in range(len(points)):
        if j != i:
            L *= (t - points[j][0]) / (points[i][0] - points[j][0])
    poly = L.expand()
    a.append(poly.coeff(t, 0))
    b.append(poly.coeff(t, 1))
    c.append(poly.coeff(t, 2))
    d.append(poly.coeff(t, 3))

# Resultados
print("L0(t) = a0 + b0*t + c0*t^2 + d0*t^3")
print("a0 =", Rational(a[0]).limit_denominator())
print("b0 =", Rational(b[0]).limit_denominator())
print("c0 =", Rational(c[0]).limit_denominator())
print("d0 =", Rational(d[0]).limit_denominator())

print("")

print("L1(t) = a1 + b1*t + c1*t^2 + d1*t^3")
print("a1 =", Rational(a[1]).limit_denominator())
print("b1 =", Rational(b[1]).limit_denominator())
print("c1 =", Rational(c[1]).limit_denominator())
print("d1 =", Rational(d[1]).limit_denominator())

print("")

print("L2(t) = a2 + b2*t + c2*t^2 + d2*t^3")
print("a2 =", Rational(a[2]).limit_denominator())
print("b2 =", Rational(b[2]).limit_denominator())
print("c2 =", Rational(c[2]).limit_denominator())
print("d2 =", Rational(d[2]).limit_denominator())

print("")

print("L3(t) = a3 + b3*t + c3*t^2 + d3*t^3")
print("a3 =", Rational(a[3]).limit_denominator())
print("b3 =", Rational(b[3]).limit_denominator())
print("c3 =", Rational(c[3]).limit_denominator())
print("d3 =", Rational(d[3]).limit_denominator())

print("")

# Valores da função nos pontos de interpolação
z = [point[1] for point in points]

# Cálculo do polinômio interpolador L(t)
L = sum(z[i] * (a[i] + b[i]*t + c[i]*t**2 + d[i]*t**3) for i in range(len(points)))

# Resultado
print("L(t) = a + b*t + c*t^2 + d*t^3")
print("a =", Rational(L.coeff(t, 0)).limit_denominator())
print("b =", Rational(L.coeff(t, 1)).limit_denominator())
print("c =", Rational(L.coeff(t, 2)).limit_denominator())
print("d =", Rational(L.coeff(t, 3)).limit_denominator())
print("L3 = ", L)

