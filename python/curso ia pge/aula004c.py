import pandas as pd
import numpy as np, sys
from sklearn.linear_model import LogisticRegression
 
# Carregar os dados do CSV usando Pandas
dados = pd.read_csv('C:/Users/E223947318/Downloads/emprestimos.csv')
# Codificar variáveis categóricas usando one-hot encoding
dados = pd.get_dummies(dados, columns=['genero', 'estado_civil'], drop_first=True)
# Dividir os dados em recursos (X) e rótulo alvo (y)
X_treinamento = dados.drop('emprestimo_aprovado', axis=1) #uma copia do dados, lá não remove essa coluna
y_treinamento = dados['emprestimo_aprovado']
 
# Treinar o modelo de regressão logística
model = LogisticRegression()
model.fit(X_treinamento, y_treinamento)
 
# Certifique-se de que o dado de predição tenha as mesmas colunas que os dados de treinamento
colunas_treinamento = X_treinamento.columns
df_predicao = pd.DataFrame({
    'idade': np.array([30]),
    'dependentes': 0,
    'salario_anual': 60000,
    'genero_M': 0,
    'estado_civil_Solteiro': 1
})
# Fazer a previsão
y_pred = model.predict(df_predicao)
 
if y_pred[0] == 1:
    print("A previsão é que o empréstimo foi aprovado.")
else:
    print("A previsão é que o empréstimo foi rejeitado.")