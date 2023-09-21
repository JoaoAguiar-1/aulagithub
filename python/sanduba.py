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

opcao = int(input("""
Escolha o recheio:
    1 - Carne
    2 - Frango
    3 - Soja
"""))

match opcao:
    case 1:
        valor_total += 9
        recheio_escolhido = 'Carne'
    case 2:
        valor_total += 7
        recheio_escolhido = 'Frango'
    case 3:
        valor_total += 6
        recheio_escolhido = 'Soja'
    case other:
        valor_total += 7
        recheio_escolhido = 'Frango'

opcao = int(input("""
Escolha o molho:
    1 - Agridoce
    2 - Parmesao
    3 - Especial
"""))

match opcao:
    case 1:
        valor_total += 3
        molho_escolhido = 'Agridoce'
    case 2:
        valor_total += 2
        molho_escolhido = 'Parmesao'
    case 3:
        valor_total += 2
        molho_escolhido = 'Especial'
    case other:
        valor_total += 2
        molho_escolhido = 'Especial'

print(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    Caro cliente, conforme escolhido, seu sanduba terá:
      Pão:                      {pao_escolhido},
      Recheio:                  {recheio_escolhido},
      Molho:                    {molho_escolhido}.

    TOTAL DO PEDIDO:            R${valor_total:.2f}
    Obrigado pela preferência e volte sempre!
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")