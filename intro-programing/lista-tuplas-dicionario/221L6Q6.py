# Função para retornar as propriedades de um talismã
def propriedade_talisma(nome_talisma, lista_talisma):
    for talisma in lista_talisma:
        if talisma['nome'] == nome_talisma:
            propriedades_talisma = talisma.copy()

            return propriedades_talisma


# Função para verificar se Jackie vence o adversario
def turno_jackie(adversario_, jackie_, lista_talisma):
    talisma_adversario = propriedade_talisma(adversario_, lista_talisma)
    talisma_jackie = propriedade_talisma(jackie_, lista_talisma)
    win = False
    if talisma_jackie['habilidade'] == talisma_adversario['requisito']:
        win = True

        return win

    else:
        return win


# Função para verificar o talisma faltante
def talisma_faltante(nome_talisma, lista_talisma):
    resposta = ''

    talisma = propriedade_talisma(nome_talisma, lista_talisma)
    for item in lista_talisma:
        if talisma['requisito'] == item['habilidade']:
            resposta = item['nome']

            return resposta


# Lista com os talismãs e suas propriedades
talismas = [{'nome': 'Carneiro', 'habilidade': 'adormecer', 'requisito': 'imortalidade'},
            {'nome': 'Cao', 'habilidade': 'imortalidade', 'requisito': 'forca descomunal'},
            {'nome': 'Cobra', 'habilidade': 'invisibilidade', 'requisito': 'equilibrio espiritual'},
            {'nome': 'Coelho', 'habilidade': 'alta velocidade', 'requisito': 'metamorfose animal'},
            {'nome': 'Tigre', 'habilidade': 'equilibrio espiritual', 'requisito': 'adormecer'},
            {'nome': 'Dragao', 'habilidade': 'fogo', 'requisito': 'cura'},
            {'nome': 'Cavalo', 'habilidade': 'cura', 'requisito': 'levitacao'},
            {'nome': 'Macaco', 'habilidade': 'metamorfose animal', 'requisito': 'raio laser'},
            {'nome': 'Galo', 'habilidade': 'levitacao', 'requisito': 'animar objetos'},
            {'nome': 'Porco', 'habilidade': 'raio laser', 'requisito': 'fogo'},
            {'nome': 'Rato', 'habilidade': 'animar objetos', 'requisito': 'alta velocidade'},
            {'nome': 'Touro', 'habilidade': 'forca descomunal', 'requisito': 'invisibilidade'}]

# Jackie e seus talismãs
jackie_talisma = list()

qtd_talismas_jackie = int(input())
for i in range(qtd_talismas_jackie):
    jackie_talisma.append(input())

# Adversários e seus talismãs
adversarios_talismas = list()

qtd_talismas_adversario = int(input())
for i in range(qtd_talismas_adversario):
    adversarios_talismas.append(input())

status_win = []

status_turno = False
count = 0
# Iniciando os turnos
for turno in range(len(adversarios_talismas)):
    for jackie in jackie_talisma:
        status_turno = turno_jackie(adversarios_talismas[turno], jackie, talismas)

        if status_turno:
            break

    if status_turno:
        print(f'Boa! O talisma do {adversarios_talismas[turno]} vai ser nosso!')
        status_win.append(True)
        jackie_talisma.append(adversarios_talismas[turno])
        status_turno = False

    else:
        talisma_faltantes = talisma_faltante(adversarios_talismas[turno], talismas)
        print(f'Nao vai dar, melhor ir atras do talisma do {talisma_faltantes} antes.')


else:
    if len(status_win) == len(adversarios_talismas):
        print('Esse plano funciona, vamos agora!')

    else:
        print('Que mau dia!! Melhor pensarmos num plano de fuga.')
