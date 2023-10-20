import pandas as pd

data = {
    'nome': ['João', 'Maria', 'José'],
    'idade': [20,30,35],
    'cidade': ['Rio de Janeiro', 'Duque de Caxias', 'Niterói']
}

df = pd.DataFrame(data)
#print(df.columns)
#print(df['nome'])
#print(df['nome'].loc[1])

'''
filtro = df['idade'] >= 30
#resultado = df[df['idade'] >= 30]
'''
filtro = (df['idade'] >= 20) & (df['cidade'] == 'Rio de Janeiro')
resultado = df[filtro]
print(resultado)


