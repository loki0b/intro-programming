# Contando quantas vezes o número apareceu no dicionário
def list_to_dict(lista):
    dicionario = dict()
    for numero in lista:
        if numero not in dicionario:
            dicionario[numero] = 1

        else:
            dicionario[numero] += 1

    return dicionario


# Comparando se os dicionários são iguais
def comparar_dicionario(dicionario1, dicionario2):
    resposta = False

    dicionario = dict()
    for chave1, valor1 in dicionario1.items():
        for chave2, valor2 in dicionario2.items():
            if chave1 in dicionario2:
                subtracao = dicionario1[chave1] - dicionario2[chave1]
                dicionario[chave1] = subtracao

            elif chave1 not in dicionario2:
                dicionario[chave1] = valor1

            elif chave2 not in dicionario1:
                dicionario[chave2] = valor2

    else:
        print(dicionario)
        resposta = iguais(dicionario)

        return resposta


# Funcao para verificar se existe o mesmos valores nos dicionarios
def iguais(dicionario):
    resposta = False
    for chave, valor in dicionario.items():
        if valor != 0:

            return resposta

    else:
        resposta = True

        return resposta


qtd_pedras = int(input())
pedras_gohan = list_to_dict(input().split())
pedras_piccolo = list_to_dict(input().split())

lista_iguais = comparar_dicionario(pedras_gohan, pedras_piccolo)

if lista_iguais:
    print('Dale Gohan!')

else:
    print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')
