import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1.0, 2.0, -1.0, 3.0],
	[2.0, 3.0, 9.0, 16.0],
	[-2.0, 0.0, 4.0, -1.0],
	[2.0, 11.0, 5.0, 3.0],
	[0.0, 2.0, -1.0, 4.0],
	[1.0, -3.0, 1.0, 7.0]])

b = np.array([1.0, 0.0, 1.0, 0.0, -1.0, 1.0])

AtA = np.matmul(np.transpose(A), A)

Atb = np.matmul(np.transpose(A), b)

x = np.linalg.solve(AtA, Atb)

print(x)

