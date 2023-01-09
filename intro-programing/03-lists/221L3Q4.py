# Guardando as palavras em uma lista
palavras_escondidas = []
for i in range(10):
    palavras_escondidas.append(input())

# Passo 1: Strings que não se repetiram
palavras_nao_repetidas = []
for i in range(len(palavras_escondidas)):
    aux = palavras_escondidas[i]
    repeticoes = 0
    count = 0
    while count < len(palavras_escondidas):
        if aux == palavras_escondidas[count]:
            repeticoes += 1

        count += 1

    else:
        if repeticoes == 1:
            palavras_nao_repetidas.append(aux)

# 1º Output
print(f'As palavras sao:')
for i in range(len(palavras_nao_repetidas)):
    print(palavras_nao_repetidas[i])

# Passo 2: Soma do tamanho das palavras nao repetidas
soma_tamanho_palavra = 0
for palavra in palavras_nao_repetidas:
    for letra in palavra:
        soma_tamanho_palavra += 1

# 2º Output
print(f'A soma do tamanho das palavras é: {soma_tamanho_palavra}')

# Output final
print('Estou impressionado, você me venceu, pode ir embora...')
