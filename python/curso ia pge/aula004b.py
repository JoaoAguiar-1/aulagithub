import numpy as np, sys, os
from sklearn.linear_model import LogisticRegression

#Dados de treinamento
idade_treinamento = np.array([30,25,35,40,40,50])                       #idade da pessoa
renda_treinamento = np.array([100000,80000,120000,90000,80000,110000])  #renda anual?
comprou_produto_treinamento = np.array([1,0,1,0,0,1])                   #comprou ou não

#dividir em X e y
X_treinamento = np.column_stack((idade_treinamento, renda_treinamento))
y_treinamento = comprou_produto_treinamento

#treinar o modelo usando regressão logistica
model = LogisticRegression()
model.fit(X_treinamento,y_treinamento)

#predição
idade_predicao = np.array([50, 40, 20])
renda_predicao = np.array([1110000, 3000, 1000])

#predição
X_predicao = np.column_stack((idade_predicao,renda_predicao))
y_predicao = model.predict(X_predicao)

print("A previsão {}".format(y_predicao))