'''def ola(nome):
    return f"Olá {nome}!"

print(ola("joão"), 10, sep=";")

def soma(n1,n2):
    return n1+n2

x = soma(10,50)
print(f'a soma será {x}')

def dados(nome='desconhecido',sobrenome = 'desconhecido',idade ='desconhecido', genero= 'desconhecido' ):
    return f'nome: {nome} \nsobrenome {sobrenome} \nidade: {idade} \ngênero:{genero}'
print(dados('joão'))

def imc():
    global altura,peso #usado caso queira acessar elas fora do escopo local
    altura = float(input("Digite a altura:"))
    peso = float(input("Digite o peso:"))
    return peso/altura**2

print(f"Seu imc é {imc():.2f}")'''

#*args passamos varios valores de um mesmo tipo
def somador(*numeros):
    return sum(numeros)

print(somador(5,1,4,6,4))

def pagamentos(nome, *pagamentos):
    print('Nome:' , nome)
    for pagamento in pagamentos:
        print("Valor: R$",pagamento)
    print('Total: R$',sum(pagamentos))

pagamentos('Maria', 300.00, 440.50)

#**kwargs passamos valores que ocuparão a estrutura do dicionário
def calcular(**valores):
    return valores['valor'] + (valores['valor'] * valores['taxa'] / 100)
print(calcular(valor = 100.00, taxa = 10))

#equivalente a fazer isso:
meu_dict = {
    'valor' : 100.00,
    'taxa' :10
}
print(meu_dict['valor'] + (meu_dict['valor'] * meu_dict['taxa']/100))

