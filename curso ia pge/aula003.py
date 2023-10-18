import numpy as np
'''
import matplotlib.pyplot as plt

X = np.array([1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2])
y = np.array([60,  62,  64,  66,  68,  70,  72,  74,])

m, b = np.polyfit(X, y, 1)

def predict_peso(altura):
    return m* altura + b

altura_prev = 1.75
peso_prev = predict_peso(altura_prev)
plt.plot(altura_prev, peso_prev, marker="o", markeredgecolor = "red", markerfacecolor = "green")
plt.scatter(X,y)
plt.plot(X,m*X+b, linestyle="--", color="k")
plt.xlim(np.min(X), np.max(X))
plt.ylim(np.min(y), np.max(y))
print(f"o peso predito é {peso_prev}")
plt.show()
'''
'''
intervalo = np.linspace(0, 1, 50)
print(intervalo)
'''
'''
array = np.array([1,2,3,4,5,6])
matriz =array.reshape(2,3)
print(matriz)
'''
'''
array = np.array([1,2],[3,4])
mt = np.transpose(array)
print(mt)
'''
'''
array = np.array([1,2])
array2 = np.array([3,4])

print(np.concatenate((array,array2)))
'''
'''
array = np.array([3,1,4,1,5,9,2,6])
resultado1 = np.argmax(array)
resultado2 = np.argmin(array)
print(resultado1, resultado2)
'''
'''
m1 = np.array([
    [1,2], [3,4]
])
m2 = np.array([
    [5,6], [7,8]
])
'''

'''
na = np.random.rand(3,3)
print(na)
'''
'''
a1 = np.array([1,2,3,4,5,6])
na = np.array_split(a1,3)
print(na)
'''
'''
a1 = np.arange(12)
print(a1)
'''
'''
#cria uma matriz 3d no reshape com 3 argumentos
a1 = np.arange(12).reshape(2,3,2)
print(a1[0][0][1])
'''

import os
os.getcwd()
#dados = np.loadtxt('C:/Users/E223947318/Downloads/dados.csv', delimiter=',', skip_header=1)
dtype = [('X', 'int'), ('y', 'int')]
dados = np.genfromtxt('C:/Users/E223947318/Downloads/dados.csv', delimiter=',', skip_header=1, missing_values='-999', dtype=dtype)
print(dados)