import numpy as np

dtype = [('anos_experiencia', 'float'), ('salario_anual', 'int')]
data = np.genfromtxt('C:/Users/E223947318/Downloads/salarios.csv', delimiter=',', skip_header=1)

#print(data)

'''
X = []
for i in data:
    #X.append(i[0])
    #print(i[0])
'''

anos_experiencia = data[:,0]
salario_anual = data[:,1]

m, b = np.polyfit(anos_experiencia, salario_anual, 1)

def predic_salario(anos):
    return m* anos + b

anos = float(input("Quantos anos?"))
predicao = predic_salario(anos)

print(f"Predição de salário para {anos} anos de experiência: {predicao:.2f}")