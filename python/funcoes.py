def ola(nome):
    return f"Olá {nome}!"

print(ola("joão"), 10, sep=";")

def soma(n1,n2):
    return n1+n2

x = soma(10,50)
print(f'a soma será {x}')

def dados(nome='desconhecido',sobrenome = 'desconhecido',idade ='desconhecido', genero= 'desconhecido' ):
    return f'nome: {nome} \nsobrenome {sobrenome} \nidade: {idade} \ngênero:{genero}'
print(dados('joão'))