def fatorial(n):
    if n == 1:
        return n
    else:
        return n*fatorial(n-1)
i = int(input("Digite um número para calcular seu valor fatorial:"))

print(f"O fatorial de {i}, ou seja, {i}! será {fatorial(i)}.")