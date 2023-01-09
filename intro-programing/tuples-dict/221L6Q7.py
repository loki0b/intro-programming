# Função para retornar uma nova receita
def new_recipe(nome_receita, lista_ingredientes):
    # Usei lista aqui apenas para fazer append e organizar melhor o dicionário, mas retorno a lista como tupla
    # no dicionário
    receita = list()
    ingredientes = list()
    for ingrediente in lista_ingredientes:
        ingredientes.append(ingrediente)

    else:
        # retornando como dicionário e tupla
        receita.append({nome_receita: tuple(ingredientes)})
        receita.append({nome_receita: price_new_recipe(lista_ingredientes)})

        return receita


# Função para determinar preço da nova receita
def price_new_recipe(lista_ingredientes):
    global preco_ingredientes

    preco_total = 5
    for ingrediente in lista_ingredientes:
        preco_total += preco_ingredientes[ingrediente]

    return preco_total


# Função para retornar o mais vendido
def mais_vendido(lista_informacoes):
    resposta = list()
    lista_auxiliar = lista_informacoes.copy()
    lista_auxiliar.pop('caixa total')

    nome = ''
    maior = 0
    for vendas in lista_auxiliar:
        if lista_auxiliar[vendas] > maior:
            maior = lista_auxiliar[vendas]
            nome = vendas
    else:
        resposta.append(nome)
        resposta.append(maior)

        return resposta


# Nos controles eu decidi usar variáveis globais só para não deixar o código main muito grande

# Controle de vendas
def controle_vendas(nome_pedido):
    global informacoes_vendas

    if nome_pedido not in informacoes_vendas:
        informacoes_vendas[nome_pedido] = 1

    else:
        informacoes_vendas[nome_pedido] += 1


# Controle de preparo
def controle_preparo(nome_pedido):
    global cardapio, estoque_ingredientes, informacoes_vendas, preco_ingredientes

    for ingrediente in cardapio[nome_pedido]:
        if estoque_ingredientes[ingrediente] == 0:
            informacoes_vendas['caixa total'] -= 4 * preco_ingredientes[ingrediente]
            estoque_ingredientes[ingrediente] += 4

    for ingrediente in cardapio[nome_pedido]:
        estoque_ingredientes[ingrediente] -= 1


# Controle do caixa
def controle_caixa(nome_pedido):
    global preco_cardapio

    return preco_cardapio[nome_pedido]


# Informações sobre o ERP do Siri Cascudo
cardapio = {'hamburguer de siri':  ('siri', 'pao', 'alface', 'tomate', 'queijo', 'picles'),
            'pizza de siri': ('siri', 'trigo', 'fermento', 'ovos', 'queijo'),
            'siri frito': ('siri', 'manteiga'),
            'siri a parmegiana': ('siri', 'trigo', 'ovos', 'queijo', 'tomate')}

preco_cardapio = {'hamburguer de siri': 24, 'pizza de siri': 42, 'siri frito': 15, 'siri a parmegiana': 24}

estoque_ingredientes = {'siri': 5, 'pao': 5, 'alface': 5, 'tomate': 5, 'queijo': 5, 'picles': 5, 'trigo': 5,
                        'fermento': 5, 'ovos': 5, 'manteiga': 5, 'batata': 5, 'arroz': 5}

preco_ingredientes = {'trigo': 3, 'fermento': 2, 'manteiga': 6, 'ovos': 2, 'batata': 4, 'arroz': 3, 'siri': 8,
                      'pao': 2, 'tomate': 2, 'alface': 1, 'picles': 3, 'queijo': 5}

informacoes_vendas = {'caixa total': 40}

pedidos_novas_receitas = dict()
# Iniciando pedidos
receita_fora_cardapio = 0
finished = False
while not finished:
    try:
        pedido = input()

    except EOFError:
        finished = True

    else:
        # Caso o pedido esteja no cardápio
        if pedido in cardapio:
            controle_preparo(pedido)
            controle_vendas(pedido)
            informacoes_vendas['caixa total'] += controle_caixa(pedido)
            print(f'{pedido} saindo...')

        #  Caso pedido não esteja no cardápio
        else:
            if pedido not in pedidos_novas_receitas:
                pedidos_novas_receitas[pedido] = 1
                print(f'{pedido} ainda não é uma opção disponível.')

            else:
                pedidos_novas_receitas[pedido] += 1
                if pedidos_novas_receitas[pedido] < 3:
                    print(f'{pedido} ainda não é uma opção disponível.')

                elif pedidos_novas_receitas[pedido] > 2:
                    # Adicionando pedido ao cardápio
                    if pedidos_novas_receitas[pedido] > 2:
                        try:
                            nova_receita = input().split()

                        except EOFError:
                            finished = True

                        else:
                            nova_receita = new_recipe(pedido, nova_receita)
                            cardapio.update(nova_receita[0])
                            preco_cardapio.update(nova_receita[1])
                            print(f'Atendendo demandas, {pedido} é a mais nova adição ao cardápio do Siri Cascudo.')

else:
    print(f'##### Fim do expediente #####')
    print(f'O lucro obtido no dia de hoje foi de R${informacoes_vendas["caixa total"] - 40}.')

    melhor_vendido = mais_vendido(informacoes_vendas)

    if melhor_vendido[0] == 'hamburguer de siri':
        print('O bom e tradicional hambúrguer de siri, líder em vendas, nunca será superado!')

    else:
        print(f'{melhor_vendido[0].capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o '
              f'lendário hambúrguer de siri.')
