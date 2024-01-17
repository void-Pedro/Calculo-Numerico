def f(x):
    return 1.006*x**5 + 3.006*x**2 - 1.006*x + 1.09

def f_deriv(x):
    return 1.006*5*x**4 + 3.006*2*x - 1.006

def phi(x):
    return x - f(x)/f_deriv(x)

max_iterations = 1000
xk=0
n=0
for k in range(max_iterations):
    xk_plus_1 = phi(xk)
    # Verifica o critério de parada
    if round(xk, 8) == round(xk_plus_1, 8):
         print ("K=",n,"Xk=",round(xk,8))
         break
    else:
         xk = xk_plus_1
         n = n + 1