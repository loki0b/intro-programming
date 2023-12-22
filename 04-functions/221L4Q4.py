# Função para separar sílabas
def separar_silabas(palavra_a_ser_separada):
    lista_silabas = []
    silaba = ''
    for letra in palavra_a_ser_separada:
        if letra not in 'aeiou':
            silaba += letra

        else:
            silaba += letra
            lista_silabas.append(silaba)
            silaba = ''

    return lista_silabas


# Função que retorna apenas as sílabas necessárias
def palavra_encontrada(input_escolhido):
    silabas_separadas = separar_silabas(input_escolhido)

    lista_silabas_reais = ['shi', 'chi', 'ko', 'ku', 'ya', 'ma']

    silabas_encontradas = []
    for silaba in silabas_separadas:
        for silaba_real in lista_silabas_reais:
            if silaba_real == silaba:
                silabas_encontradas.append(silaba)

    return silabas_encontradas


# Função para verificar se a palavra está na ordem correta
def ordem_correta(palavra_sep):
    if palavra_sep in 'shichikokuyama':
        return True

    else:
        return False


palavra_bool = [False, False, False, False, False, False]
palavra_completa = ''

finished = False
while not finished:
    palavra_input = input()

    palavra_retornada = palavra_encontrada(palavra_input)

    remove = False
    # Removendo sílabas existentes e já verificadas
    for i in range(len(palavra_retornada)):
        for palavra in palavra_retornada:
            if palavra == 'shi' and palavra_bool[0]:
                palavra_retornada.pop(palavra_retornada.index(palavra))
                remove = True

            elif palavra == 'chi' and palavra_bool[1]:
                palavra_retornada.pop(palavra_retornada.index(palavra))
                remove = True

            elif palavra == 'ko' and palavra_bool[2]:
                palavra_retornada.pop(palavra_retornada.index(palavra))
                remove = True

            elif palavra == 'ku' and palavra_bool[3]:
                palavra_retornada.pop(palavra_retornada.index(palavra))
                remove = True

            elif palavra == 'ya' and palavra_bool[4]:
                palavra_retornada.pop(palavra_retornada.index(palavra))
                remove = True

            elif palavra == 'ma' and palavra_bool[5]:
                palavra_retornada.pop(palavra_retornada.index(palavra))
                remove = True

        else:
            for palavra_retirada in palavra_retornada:
                aux = palavra_retirada
                for palavra_re in palavra_retornada:
                    if aux == palavra_re and palavra_retornada.count(aux) > 1:
                        palavra_retornada.pop(palavra_retornada.index(palavra_re))

    if len(palavra_retornada) == 0:
        print(f'Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.')

    elif len(palavra_retornada) == 1:
        print(f'Lembrei! A sílaba {palavra_retornada[0]} está no nome do hospital. Obrigada, Totoro!')

    elif len(palavra_retornada) > 1:
        if ordem_correta(''.join(palavra_retornada)) and not remove:
            print(f'A palavra {"".join(palavra_retornada)} está toda no nome do hospital. Acertou em cheio, Totoro!')

        else:
            print(f'Lembrei! As sílabas:', end=' ')
            for i in range(len(palavra_retornada)):
                if palavra_retornada[i] == palavra_retornada[-1]:
                    print(f'{palavra_retornada[i]}', end=' ')

                else:
                    print(f'{palavra_retornada[i]}', end=', ')

            else:
                print(f'estão no nome do hospital. Obrigada, Totoro!')

    for palavra in palavra_retornada:
        if palavra == 'shi':
            palavra_bool[0] = True

        elif palavra == 'chi':
            palavra_bool[1] = True

        elif palavra == 'ko':
            palavra_bool[2] = True

        elif palavra == 'ku':
            palavra_bool[3] = True

        elif palavra == 'ya':
            palavra_bool[4] = True

        elif palavra == 'ma':
            palavra_bool[5] = True

    count = 0
    for boolean in palavra_bool:
        if boolean:
            count += 1

        if count == 6:
            finished = True

else:
    print(f'Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!')
