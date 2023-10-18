import numpy as np
#Regressão linear multipla

quartos = np.array([2,3,2,4,3,4,3,2,3,4])
tamanho_m2 = np.array([80,120,90,150,100,130,110,85,95,140])
preco = np.array([200000,300000,220000,350000,240000,320000,280000,210000,250000,330000])

X_bias = np.column_stack(
    (
        np.ones(len(quartos)),
        quartos,
        tamanho_m2
    )
)
#print(X_bias)

coeficientes = np.linalg.lstsq(X_bias, preco, rcond=None)[0]
coeficientes_bias = coeficientes[0]
coeficientes_bias_quartos = coeficientes[1]
coeficientes_bias_m2 = coeficientes[2]


novo_quarto = 3
novo_m2 = 105
previsao = coeficientes_bias + coeficientes_bias_quartos * novo_quarto + coeficientes_bias_m2 * novo_m2
print(f"Preço estimado para o imóvel  com {novo_quarto} quarto(s) e {novo_m2} m²: R${previsao:.2f}")