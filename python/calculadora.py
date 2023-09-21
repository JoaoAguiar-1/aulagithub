x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(
    input(
        """

Digite o número da operação:
        1 - Soma
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        5 - Exponenciação
        6 - Resto da Divisão        

"""
    )
)
""" 
Estrutura com Ifs
if z == 1:
    print(f"Soma: {x} + {y} = {x+y}")
elif z == 2:
    print(f"Subtração: {x} - {y} = {x-y}")
elif z == 3:
    print(f"Multiplicação: {x} x {y} = {x*y}")
elif z == 4:
    print(f"Divisão: {x} / {y} = {x/y}")
elif z == 5:
    print(f"Exponenciação: {x} ^ {y} = {x**y}")
elif z == 6:
    print(f"Resto: {x} resto {y} = {x%y}")
else:
    print("Operação não registrada")
"""

match z:
    case 1:
        print(f"Soma: {x} + {y} = {x+y}")
    case 2:
        print(f"Subtração: {x} - {y} = {x-y}")
    case 3:
        print(f"Multiplicação: {x} x {y} = {x*y}")
    case 4:
        print(f"Divisão: {x} / {y} = {x/y}")
    case 5:
        print(f"Exponenciação: {x} ^ {y} = {x**y}")
    case 6:
        print(f"Resto: {x} resto {y} = {x%y}")
    case other:
        print("Operação não registrada")
