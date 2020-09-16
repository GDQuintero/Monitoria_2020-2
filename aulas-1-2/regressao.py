import numpy as np
import matplotlib.pyplot as plt

def f(x,a):
	return a[0] + a[1]*x

t = np.linspace(0.0, 1.0, 11)

v = np.array([-0.10290, 0.37364, 2.43748, 3.93836, 3.31230, 
	5.49472, 5.43325, 5.43325, 9.06048, 9.36416, 9.52066])

m = len(t)

A = np.zeros((m,2)); b = np.zeros(m)

A[:,0] = 1.0; A[:,1] = t[:]; b = v[:]

AtA = np.matmul(np.transpose(A), A)

Atb = np.matmul(np.transpose(A), b)

a = np.linalg.solve(AtA, Atb)

x = np.linspace(0.0, 1.0, 1000)

plt.plot([t[i] for i in range(m)],[v[i] for i in range(m)],'o', label = 'Dados')
plt.plot(x, f(x,a), label = 'Solução')
plt.xlabel('Tempo')
plt.ylabel('Velocidade')
plt.legend()
plt.show()