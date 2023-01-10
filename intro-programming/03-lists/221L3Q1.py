lista_suspeitos = str(input()).split(',')

# Iterando até sobrar apenas um suspeito
while len(lista_suspeitos) != 1:
    operacao = str(input())

    # Caso o primeiro seja removido
    if operacao == 'Não encontrei nada no primeiro suspeito':
        lista_suspeitos.pop(0)

    # Caso o último seja removido
    elif operacao == 'O último da lista está limpo':
        lista_suspeitos.pop(-1)

    # Caso o do meio seja removido
    elif operacao == 'Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita':
        # Se a lista tiver len par
        if len(lista_suspeitos) % 2 == 0:
            lista_suspeitos.pop(len(lista_suspeitos) // 2)
        # Se a lista tiver len ímpar
        elif len(lista_suspeitos) % 2 == 1:
            lista_suspeitos.pop((len(lista_suspeitos) - 1) // 2)

    # Caso seja escolhido uma posição
    elif operacao == 'Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:':
        posicao_suspeito = int(input())
        lista_suspeitos.pop(posicao_suspeito)

    # Caso um suspeito seja inserido
    elif operacao == 'Acho que temos mais uma opção a ser analisada…':
        novo_suspeito = str(input())
        lista_suspeitos.append(novo_suspeito)

    else:
        print('Isso não estava no combinado, a lista vai permanecer do mesmo jeito')

# Output após sobrar apenas um suspeito
else:
    print(f'Acho que encontramos o suspeito. O seu nome é {lista_suspeitos[0]}, vamos salvar o Sam!')