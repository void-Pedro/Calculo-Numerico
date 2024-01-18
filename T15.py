# Determinar a quantidade de iterações necessárias para um sistema 9x9 (Jacobi e Gauss-Seidel) com critério de parada em 4 casas decimais exatas

import numpy as np

def truncate(number, n):
	return int(number * 10**n) / 10**n

def jacobi(A, B):
	x = np.zeros_like(B)  # Matriz das soluções (inicialmente com 0s)
	ant = x.copy()
	k = 0
	ok = 0

	# Limita em 100 iterações
	while k < 100:
		ant = x.copy()
		ok = 0
	 	
		for i in range(len(A)):
			x[i] = B[i]
			for j in range(len(A[0])):
				if i != j:
 					x[i] -= A[i][j] * ant[j]
			x[i] /= A[i][i]

		# Trunca na 4a casa decimal e compara todos os elementos (condição de parada)
		for i, j in zip(x, ant):
			if int(i*10000) == int(j*10000):
				ok += 1
		if ok == len(x): break # Se todos os elementos dos 2 arrays forem iguais, finaliza

		k += 1

	print(f'[Jacobi] {k+1} iterações')

	return x

def gauss_seidel(A, B):
	x = np.zeros_like(B)  # Matriz das soluções (inicialmente com 0s)
	ant = x.copy()
	k = 0
	ok = 0

	# Limita em 100 iterações
	while k < 100:
		ant = x.copy()
		ok = 0
	 	
		for i in range(len(A)):
			x[i] = B[i]
			for j in range(len(A[0])):
				if i != j:
 					x[i] -= A[i][j] * x[j]
			x[i] /= A[i][i]

		# Trunca na 4a casa decimal e compara todos os elementos (condição de parada)
		for i, j in zip(x, ant):
			if int(i*10000) == int(j*10000):
				ok += 1
		if ok == len(x): break # Se todos os elementos dos 2 arrays forem iguais, finaliza

		k += 1

	print(f'[Gauss-Seidel] {k+1} iterações')

	return x

def resolver(A, B):
	# Jacobi
	for k in jacobi(A, B):
		print(f'{round(k.item(), 4)}')
	
	print('\n')
	
	# Gauss-Seidel
	for k in gauss_seidel(A, B):
		print(f'{round(k.item(), 4)}')

# ----------------------------------------------------------------------------

# Matriz A
A = '''3.561	0.742	-0.219	0.349	-0.323	0.578	-0.486	0.57	-0.019
0.244	5.003	0.802	-0.503	0.604	-0.924	0.317	-0.365	0.341
-0.502	0.751	5.082	0.965	-0.52	0.647	-0.105	0.572	-0.152
0.314	-0.393	0.364	4.394	0.22	-0.96	0.419	-0.169	0.646
-0.867	0.57	-0.813	0.664	4.547	0.269	-0.226	0.63	-0.061
0.56	-0.68	0.56	-0.705	0.521	4.895	0.494	-0.04	0.973
-0.662	0.446	-0.937	0.057	-0.968	0.049	4.43	0.412	-0.523
0.468	-0.385	0.674	-0.221	0.49	-0.773	0.763	5.392	0.856
-0.981	0.209	-0.237	0.887	-0.805	0.82	-0.284	0.516	5.606'''

B = '''8.6 -5.5 5.9 1.4 -0.5 4 -8.9 3.4 -2.1'''

# Transforma os textos em matrizes
A = np.array([[float(num) for num in row.split()] for row in A.split('\n')])
B = np.array([[float(num) for num in row.split()] for row in B.split('\n')])

resolver(A, B)
