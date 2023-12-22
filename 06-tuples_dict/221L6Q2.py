# Função para transformar a lista em dicionário
def dicionario_str_to_int(lista):
    resposta = {}
    for i in range(len(lista)):
        # Usando keys como index
        auxiliar = {i: int(lista[i])}
        resposta.update(auxiliar)

    return resposta


# Função para encontrar as posições dos companheiros
def encontrar_posicao(dicionario, soma):
    lista_posicao = []

    for chave1, valor1 in dicionario.items():
        for chave2, valor2 in dicionario.items():
            if chave1 == chave2:
                continue
            else:
                if valor1 + valor2 == soma:
                    lista_posicao.append(chave1)
                    lista_posicao.append(chave2)

                    return lista_posicao


dicionario_companheiros = dicionario_str_to_int(input().replace('[', '').replace(']', '').split(','))
soma_companheiros = int(input())

posicao_companheiros = encontrar_posicao(dicionario_companheiros, soma_companheiros)

print(posicao_companheiros)
