print('Usando while:\n')
i=0
while i <= 10:
    i += 1
    if i == 5:
        print('pulando ...')
        continue #pula pro próximo loop
    print(f'nº {i}')
    

    if i == 7:
        print('saindo ...')
        break #sai do loop


print('\nUsando for\n')
for i in range (2,11,2): #começa em 2 termina antes do 11 e pula de 2 em 2
    print(f'i nº {i}')