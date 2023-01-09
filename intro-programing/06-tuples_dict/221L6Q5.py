# Função para estabelecer status dos adversários
def status_adversario(nome):
    dicionario_adversario = dict()
    if nome == 'Vingador':
        dicionario_adversario['nome'] = nome
        dicionario_adversario['vida'] = 30

    elif nome == 'Tiamat':
        dicionario_adversario['nome'] = nome
        dicionario_adversario['vida'] = 20

    elif nome == 'Vingador das Sombras':
        dicionario_adversario['nome'] = nome
        dicionario_adversario['vida'] = 14

    else:
        dicionario_adversario['nome'] = nome
        dicionario_adversario['vida'] = 9

    return dicionario_adversario


# Função para retornar status baseado no nome do personagem escolhido
def status_personagem(nome_personagem, lista_personagem):
    status = dict()
    for personagem in lista_personagem:
        if personagem['nome'] == nome_personagem:
            dano = 0
            armadura = 0
            if personagem['arma'] == 'chifre':
                dano = 2

            elif personagem['arma'] == 'cajado':
                dano = 4

            elif personagem['arma'] == 'espada':
                dano = 6

            elif personagem['arma'] == 'grande espada':
                dano = 8

            elif personagem['arma'] == 'dardo':
                dano = 12

            if personagem['armadura'] == 'armadura media':
                armadura = 1

            elif personagem['armadura'] == 'armadura leve':
                armadura = 3

            status['nome'] = personagem['nome']
            status['dano'] = dano
            status['armadura'] = armadura

            return status


# Definindo status dos adversários
adversario = status_adversario(input())
turno_maximo = int(input())
adversario['turnos'] = turno_maximo

# Lista dos personagens jogáveis
personagens_jogaveis = [{'nome': 'Bobby', 'arma': 'grande espada', 'armadura': 'armadura media'},
                        {'nome': 'Diana', 'arma': 'dardo', 'armadura': 'armadura leve'},
                        {'nome': 'Eric', 'arma': 'grande espada', 'armadura': 'armadura pesada'},
                        {'nome': 'Hank', 'arma': 'espada', 'armadura': 'armadura media'},
                        {'nome': 'Presto', 'arma': 'cajado', 'armadura': 'armadura leve'},
                        {'nome': 'Sheila', 'arma': 'espada', 'armadura': 'armadura leve'},
                        {'nome': 'Uni', 'arma': 'chifre', 'armadura': 'armadura leve'}]

# Iniciando turnos
for turno in range(turno_maximo):
    try:
        personagem_atacante = input()
    except EOFError:
        break

    if personagem_atacante == 'Mestre dos Magos':
        print(f'Muito obrigado amigo, que nos vejamos novamente um dia')
        break

    caracteristicas_personagem = status_personagem(personagem_atacante, personagens_jogaveis)

    adversario['vida'] -= caracteristicas_personagem['dano']
    adversario['turnos'] -= caracteristicas_personagem['armadura']
    adversario['turnos'] -= 1

    if adversario['vida'] <= 0:
        print(f'{caracteristicas_personagem["nome"]} executou o ultimo golpe em {adversario["nome"]}, estamos livres!')
        break

    elif adversario['turnos'] <= 0:
        print(f'Oh nao, {adversario["nome"]} e muito forte, este e o fim!')
        break

else:
    print(f'Oh nao, {adversario["nome"]} e muito forte, este e o fim!')
