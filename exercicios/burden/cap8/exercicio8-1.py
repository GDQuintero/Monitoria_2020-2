import numpy as np
import matplotlib.pyplot as plt

def f(x,a):
	return a[0] + a[1]*x + a[2]*(x**2) + a[3]*(x**3)

n = int(input("Numero de dados: "))

x = np.zeros(n); y = np.zeros(n); a = np.zeros(4)

for i in range(n):
	x[i] = float(input("Escreva o valor de x(" + str(i) + "): "))

for i in range(n):
	y[i] = float(input("Escreva o valor de y(" + str(i) + "): "))

inf = np.amin(x); sup = np.amax(x)

deg = int(input("Grau do polinomio (1, 2 ou 3): "))

A = np.zeros((deg + 1, deg + 1)); b = np.zeros(deg + 1)

for i in range(deg + 1):
	b[i] = np.dot(x**i, y)
	for j in range(deg + 1):
		A[i,j] = np.dot(x**i, x**j)

a[:deg + 1] = np.linalg.solve(A, b); z = np.linspace(inf, sup, 1000)

print("Os coeficientes do polonomio de grau " + str(deg) +
 " sao: " + str(a[:deg + 1]))

erro = 0.0

for i in range(n):
	erro = erro + (y[i] - f(x[i],a))**2

print("Erro quadratico: " + str(erro))

plt.plot(x, y,'o', label = 'Dados')
plt.plot(z, f(z,a), label = 'Solução')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

