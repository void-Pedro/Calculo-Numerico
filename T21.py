import numpy as np

points = np.array([(-1.0, -0.122), (-0.8, 0.044), (-0.6, -0.107), (-0.4, 0.288),
                  (-0.2, -0.928), (0.0, -0.809), (0.2, 0.964), (0.4, 0.874),
                  (0.6, 0.415), (0.8, 0.941), (1.0, 0.711)])

x_values = points[:, 0]
y_values = points[:, 1]

A = np.column_stack([x_values**n for n in range(10)])

parameters, _, _, _ = np.linalg.lstsq(A, y_values, rcond=None)

for i, param in enumerate(parameters):
    print("Parâmetro {} : {:.8f}".format(i, param))