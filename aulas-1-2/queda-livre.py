import numpy as np
import matplotlib.pyplot as plt

def f(t,a):
	return a[0] + a[1]*t + a[2]*(t**2)

file_t = open('t_data.txt','r')

file_h = open('h_data.txt','r')

t = file_t.readlines(); h = file_h.readlines()

m = len(t)

A = np.zeros((m,3)); b = np.zeros(m)

A[:,0] = 1.0

for i in range(m):
	A[i,1] = float(t[i])
	A[i,2] = float(t[i])**2
	b[i] = float(h[i])

AtA = np.matmul(np.transpose(A), A)

Atb = np.matmul(np.transpose(A), b)

a = np.linalg.solve(AtA, Atb)

x = np.linspace(0.0, 1.0, 1000)


plt.plot([float(t[i]) for i in range(m)],[float(h[i]) for i in range(m)],'o', label = 'Dados')
plt.plot(x, f(x,a), label = 'Solução')
plt.xlabel('Tempo')
plt.ylabel('Altura')
plt.legend()
plt.show()