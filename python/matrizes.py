autores = [
    ['maria', 29],
    ['josé', 30],
    ['thiago', 22],
    ['lucas', 69],
]

#verificar se existe na lista

for autor in autores:
    if 'lucas' in autor:
        print(True)

#1 alterar valor na posição
autores[1][0] = 'joão'
print(autores)
print(autores[-1])

#2 inserir no final da lista
autores.append(['ana', 18])
print(autores)

#3 inserindo na posição especifica
autores.insert(1, ['marcos', 40])
print(autores)

#4 remover o ultimo da lista
autores.pop()
print(autores)

#5 removendo item em posição especifica
#del autores[1]
autores.pop(1)
print(autores)

#6 remove a primeira ocorrência com o valor
autores.remove(['joão', 30])
print(autores)

#7 adiciona no final da lista uma outra lista
autores.extend([['josé', 10], ['ramon', 32]])
print(autores)

#8 ordenar de forma crescente
autores.sort()
print(autores)

#9 ordenar de forma decrescente
autores.sort(reverse=True)
print(autores)

#10 lispar a lista (até o indice 0 deixa de existir)
autores.clear()
print(autores)