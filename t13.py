from decimal import Decimal, getcontext
import numpy as np
import math

def resolver(A, B):
    # Une as matrizes
    R = np.concatenate((A, B), axis=1)
    
    # Aplica o arredondamento (4 algarismos significativos) na nova matriz
    R = arredondar(R)
    
    # Resultado
    R = GaussJord(R)
    R = np.array(R)
    R = arredondar(R)
    
    # Printa o resultado
    for a in R: print(a)

def arredondar(array):
    decimal_array = np.empty_like(array, dtype=object)
    iterator = np.nditer(array, flags=['multi_index', 'refs_ok'])
    
    for x in iterator:
        decimal_array[iterator.multi_index] = Decimal(str(x))
    
    return decimal_array

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
        return xx

# --------------------------------------------------------------------------------------------------------

# Definir quantos algarismos significativos
getcontext().prec = 3
'''
# Matriz A
A = 2.442	-3.400	-1.530	4.926	-11.03	10.68	-13.98	-12.07	0.4789
1.624	-2.656	-2.256	5.591	-11.88	11.53	-14.67	-11.19	-0.1691
2.394	-3.365	-1.530	4.931	-11.08	10.70	-13.94	-12.06	0.4479
1.582	-2.582	-2.263	5.630	-11.77	11.46	-14.79	-11.27	-0.1641
2.470	-3.385	-1.368	4.790	-10.95	10.72	-13.85	-11.99	0.6069
1.646	-2.537	-2.158	5.675	-11.84	11.49	-14.78	-11.19	-0.2051
2.448	-3.412	-1.361	4.814	-11.02	10.66	-13.80	-11.89	0.5069
1.618	-2.538	-2.222	5.770	-11.84	11.60	-14.62	-11.15	-0.2271
2.479	-3.480	-1.513	4.907	-11.08	10.82	-13.89	-12.02	0.5869

B = -7.405
-6.584
-7.465
-6.696
-7.446
-6.633
-7.399
-6.590
-7.408
'''

A = '''1.4 -0.26
-0.9 0.07'''

B = '''-9.6
-7.1'''
    
# Transforma os textos em matrizes
A = np.array([[float(num) for num in row.split()] for row in A.split('\n')])
B = np.array([[float(num) for num in row.split()] for row in B.split('\n')])

# Resposta
resolver(A, B)
