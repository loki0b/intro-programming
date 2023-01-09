# Funções de detecção de interferências
def detectar_insetos():
    global trasmissao
    for palavra in trasmissao:
        if palavra == 'crcrcrcrcr' or palavra == 'uuuuuuuoooooo' or palavra == 'ooooooeeeeeeee':
            return True


def detectar_aeronaves():
    global trasmissao
    for palavra in trasmissao:
        if palavra == 'ppprrrrrooon' or palavra == 'tutututututututu' or palavra == 'eeeeeeeeoooooo':
            return True


# Loop até que não seja detectado nenhum barulho
nao_detectado = False
while not nao_detectado:
    trasmissao = input().split(' ')

    # Variáveis para verificações
    inseto_detectado = detectar_insetos()
    aeronave_detectada = detectar_aeronaves()

    if not inseto_detectado and not aeronave_detectada:
        nao_detectado = True
        print('Não é possível determinar a origem da transmissão… Isso deverá levar mais algum tempo.')

    elif inseto_detectado and aeronave_detectada:
        print('A transmissão sugere que tropas estrangeiras e as criaturas do Mar Podre irão se confrontar!'
              ' Precisamos impedi-los antes que mais mortes desnecessárias ocorram!')

    elif inseto_detectado:
        print('É apenas o Mar Podre se comunicando, podemos ficar tranquilos, por enquanto…')

    elif aeronave_detectada:
        print('São sinais de aeronaves estrangeiras! Devemos preparar nossas defesas??')
