import numpy as np
import matplotlib.pyplot as plt

dtype = [('X', 'float'), ('y', 'int')]
dados = np.genfromtxt('C:/Users/E223947318/Downloads/salarios.csv', delimiter=',', skip_header=1, missing_values='-999', dtype= dtype)
print(dados)

X = []
y = []

z = np.append([12], X)
print(z)

for i in dados:
    X.append(i[0])
    y.append(i[1])
    #print(i[0])


'''
array = np.array([1,2,3,4,5,6])
matriz =array.reshape(2,3)
print(matriz)
'''