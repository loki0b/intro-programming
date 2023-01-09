# Função para conversão do texto em Miauês
def num_to_str(num):
    """ De acordo com tabela ASCII as letras do alfabeto sem acentos e cedilha usam outros decimais
    diferente do que foi passado (propositalmente) na questão. Então eu apenas fiz uma aritmetica básica para
    poder deixar os decimais iguais e facilitar na hora de converter com a função chr ao invés de usar vários elifs."""
    if num == 100:
        # Representa o Space em ASCII
        return chr(32)

    elif 0 <= num <= 49:
        # Representa as letras em caixa baixa
        if num <= 25:
            num += 97
            return chr(num)

        else:
            # Caso comece o alfabeto novamente
            num += 71
            return chr(num)

    elif num <= 99:
        # Representa as letras em caixa alta
        if num <= 75:
            num += 15
            return chr(num)

        else:
            # Caso comece o alfabeto novamente
            num -= 11
            return chr(num)


# Função para verificar se a tradução será totalmente completada
def verificar_traducao(lista):
    for nmr in lista:
        if int(nmr) < 0 or int(nmr) > 100:
            return False

    return True


# Separando os inteiros a ser convertido
miaues = input().split(' ')

# Verificando se a tradução será totalmente completa
traducao_completa = verificar_traducao(miaues)

# Convertendo a frase
if traducao_completa:
    frase_traduzida = ''
    for numero in miaues:
        frase_traduzida += num_to_str(int(numero))

    print(frase_traduzida)

else:
    print('Infelizmente os números nao dizem nada')
