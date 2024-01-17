import math

def rangekutta(f, T, n, ordem, y0):

    h = T / n
    t = [j * h for j in range(n + 1)]

    y = [0] * (n + 1)
    y[0] = y0

    for k in range(n):
        if ordem == 2:
            e1 = f(t[k], y[k])
            e2 = f(t[k] + h, y[k] + h * e1)
            y[k+1] = y[k] + (h / 2) * (e1 + e2)

        elif ordem == 3:
            e1 = f(t[k], y[k])
            e2 = f(t[k] + h/2, y[k] + (h/2) * e1)
            e3 = f(t[k] + h*(3/4), y[k] + 3/4 * h * e2)
            y[k+1] = y[k] + (h / 9) * (2 * e1 + 3 * e2 + 4 * e3)

        elif ordem == 4:
            e1 = f(t[k], y[k])
            e2 = f(t[k] + h/2, y[k] + (h/2) * e1)
            e3 = f(t[k] + h/2, y[k] + (h/2) * e2)
            e4 = f(t[k] + h, y[k] + h * e3)
            y[k+1] = y[k] + (h / 6) * (e1 + 2 * e2 + 2 * e3 + e4)

    yn = y[n]
    aux= round(yn,8)
    #print(f"y(n = {n}) = {yn:.9f} arre = {aux}")
    return aux
# Função f(t, x) da equação diferencial
def f(t, x):
    return t * math.exp(x**2)

# Coloco o T

T = 0.3
n = 200
ordem = 2
y0 = 1.0

for i in range (1,n):
    x2 = rangekutta(f,T, i, 2, y0)
    x2a = rangekutta(f,T, i + 1, 2, y0)
    if(x2 == x2a):
      print(f"y(n = {i}) / termo = {x2}")
      break


for i in range (1,n):
    x3 = rangekutta(f,T, i, 3, y0)
    x3a = rangekutta(f,T, i + 1, 3, y0)
    if(x3 == x3a):
      print(f"y(n = {i}) / termo = {x3}")
      break

for i in range (1,n):
    x4 = rangekutta(f,T, i, 4, y0)
    x4a = rangekutta(f,T, i + 1, 4, y0)
    if(x4 == x4a):
      print(f"y(n = {i}) / termo = {x4}")
      break

for i in range (1,n):
    x4 = rangekutta(f,T, i, 4, y0)

print(f"X(T) = {x4}")