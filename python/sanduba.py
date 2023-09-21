valor_total = 0.00
pao_escolhido = ''
recheio_escolhido = ''
molho_escolhido = ''

opcao = int(input("""
Escolha o pão:
    1 - Integral
    2 - Italiano
    3 - Mel
"""))

match opcao:
    case 1:
        valor_total += 5
        pao_escolhido = 'Integral'
    case 2:
        valor_total += 4
        pao_escolhido = 'Italiano'
    case 3:
        valor_total += 3
        pao_escolhido = 'Mel'
    case other:
        valor_total += 4
        pao_escolhido = 'Italiano'

print(valor_total)
print(pao_escolhido)