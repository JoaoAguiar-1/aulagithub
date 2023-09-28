#criar uma lista de processos(mín 5) com seus respectivos autores e valores das causas e se houver exito na ação(isso é, o estado ganhou). OK!
#para os casos de exito, calcular o valor de honorário de ação com exito
#exibir a lista de autores e cada honorário calculado
#no final a soma de todos os honorários

processos = [
    {'nome':'José', 'valor_causa': 20000.00, 'exito': True},
    {'nome':'Maria', 'valor_causa': 11000.00, 'exito': True},
    {'nome':'Carla', 'valor_causa': 7000.00, 'exito': False},
    {'nome':'Ana', 'valor_causa': 9000.00, 'exito': True},
    {'nome':'Marcelo', 'valor_causa': 2000.00, 'exito': True},
]

honorarios = 0.00

for acao in processos:
    if acao['exito']:
        honorario = acao['valor_causa'] * 0.08
        honorarios += honorario
        print(f'Na ação do(a) Autor(a) {acao["nome"]}, o valor dos honorários calculados são de R${honorario:.2f}')
    else:
        print(f'Sem êxito na ação do(a) autor(a) {acao["nome"]}')

print(f"Total de honorários: R$ {honorarios: .2f}")
