import numpy as np
import matplotlib.pyplot as plt

##Regressão logistica gradiente descendente

#Dados de treinamento
idade_treinamento = np.array([30,25,35,40,40,50])                       #idade da pessoa
renda_treinamento = np.array([100000,80000,120000,90000,80000,110000])  #renda anual?
comprou_produto_treinamento = np.array([1,0,1,0,0,1])                   #comprou ou não

#função de ativação
def sigmoide(z):
    return 1 / ( 1 + np.exp(-z))

#função de normalização
def normalize(data, mean, std):
    return (data - mean) / std

#normalizar dados de treinamento
idade_mean = idade_treinamento.mean() # media
idade_std = idade_treinamento.std()
renda_mean = renda_treinamento.mean()
renda_std = renda_treinamento.std()

idade_norm = normalize(idade_treinamento, idade_mean, idade_std)
renda_norm = normalize(renda_treinamento, renda_mean, renda_std)

#parâmetros iniciais
theta = np.zeros(3) #coeficientes
alpha = 0.01        #taxa de aprendizado
num_iteracoes = 1000 #em ingles epox

#preparando dados de treinamento
X_treinamento = np.column_stack((np.ones(len(idade_norm)),idade_norm, renda_norm))
y_treinamento = comprou_produto_treinamento

#print(X_treinamento)
#print(X_treinamento.T) #transposta
#sys.exit()

custos = []

for _ in range(num_iteracoes):
    z = np.dot(X_treinamento,theta)
    h = sigmoide(z)
    custo = -np.mean(y_treinamento * np.log(h) + (1 - y_treinamento) * np.log(1 - h))
    custos.append(custo)
    gradiente = np.dot(X_treinamento.T, h - y_treinamento) / len(y_treinamento)
    theta -= alpha * gradiente
    #print(gradiente)
    #print(custo)
print(theta)

#plotando o gráfico

plt.plot(range(num_iteracoes), custos)
plt.xlabel("Iterações")
plt.ylabel("Custo")
plt.title("Convergência do Grandiente Descendente")
#plt.show()

#predição
idade_predicao = np.array([50, 40, 30])
renda_predicao = np.array([1110000, 3000, 110000])

#normalização
idade_pred_norm = normalize(idade_predicao, idade_mean, idade_std)
renda_pred_norm = normalize(renda_predicao, renda_mean, renda_std)

#preparação dos dados normalizados
X_predicao = np.column_stack((np.ones(len(idade_pred_norm)),idade_pred_norm, renda_pred_norm))

previsoes = sigmoide(np.dot(X_predicao, theta))
previsoes_classes = np.round(previsoes)
# print(previsoes)

print(f"Previsões : {previsoes_classes}")
