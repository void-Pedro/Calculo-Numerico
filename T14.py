# Resolver um sistema 9x9 com 4 algarismos significativos e realizar três etapas de refinamento

from decimal import Decimal, getcontext
import numpy as np

# Escalonamento
def GaussJord(M):
    nLin = len(M)
    nCol = len(M[0])
    if nCol != nLin + 1:
        return 'erro - dimensao incompativel'
    else:
        MM = []
        xx = []
        for i in range(nLin):
            xx.append(0)
            linha = []
            for j in range(nCol):
                linha.append(M[i][j])
            MM.append(linha)
        for i in range(nLin):
            pivo = i
            for j in range(i+1, nLin):
                if abs(MM[pivo][i]) < abs(MM[j][i]):
                    pivo = j
            MM[i] , MM[pivo] = MM[pivo] , MM[i]
            for j in range(i+1,nLin):
                MM[j][i] = MM[j][i] / MM[i][i]
                for k in range(i+1, nCol):
                    MM[j][k] -= MM[j][i]*MM[i][k]

        for i in range(nLin-1,-1,-1):
            xx[i] = MM[i][nCol-1]
            for j in range(nLin-1,i,-1):
                xx[i] -= MM[i][j]*xx[j]
            xx[i] /= MM[i][i]
        return np.array(xx)

def arredondar(array):
    decimal_array = np.empty_like(array, dtype=object)
    iterator = np.nditer(array, flags=['multi_index', 'refs_ok'])
    
    for x in iterator:
        decimal_array[iterator.multi_index] = Decimal(str(x))
    
    return decimal_array

def resolver(A, B):
	# Elementos se tornam objetos Decimal()
	getcontext().prec = 4
	A = arredondar(A)
	B = arredondar(B)
	
	# Primeiro escalonamento
	x = np.concatenate((A, B), axis=1)
	x = GaussJord(x)
		
	print('Primeiro set de respostas:')
	for i in x: print(i)
		
	# Resposta
	for i in range(3):
		# Dobra a precisão
		getcontext().prec = 8
		
		# Calcula o resíduo
		r = B - (A.dot(x)).reshape((9, 1))
		
		# Retorna à precisão original
		getcontext().prec = 4
		
		# Reescalona
		y = np.concatenate((A, r), axis=1) # Une as matrizes
		y = GaussJord(y) # Escalona
		
		# Soma o resíduo com a resposta: refinamento
		x = x.reshape((9,1)) + y.reshape((9,1))
			
		print(f'\nRefinamento: {i+1}')
		for j in x: print(j[0])
# ----------------------------------------------------------------------------

# Matriz A
A = '''3.572	-14.65	4.087	1.122	11.47	-12.46	14.62	-11.44	7.883
2.678	-13.80	3.321	1.976	10.65	-11.76	13.84	-10.68	7.136
3.505	-14.64	4.072	1.152	11.32	-12.46	14.66	-11.41	7.922
2.793	-13.97	3.297	2.051	10.60	-11.78	13.83	-10.53	7.096
3.511	-14.76	4.035	1.260	11.36	-12.48	14.60	-11.32	8.000
2.686	-13.92	3.332	2.013	10.59	-11.70	13.94	-10.62	7.262
3.542	-14.71	4.201	1.203	11.34	-12.59	14.73	-11.39	7.948
2.671	-13.98	3.245	1.906	10.62	-11.76	13.97	-10.67	7.141
3.464	-14.72	4.040	1.075	11.45	-12.60	14.73	-11.46	8.031'''

B = '''0.8370
1.779
0.8220
1.772
0.9480
1.670
0.9100
1.749
0.7990'''
    
# Transforma os textos em matrizes
A = np.array([[float(num) for num in row.split()] for row in A.split('\n')])
B = np.array([[float(num) for num in row.split()] for row in B.split('\n')])

resolver(A, B)
