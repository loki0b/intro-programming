# Salvando linha do tempo e xingamentos para uso posterior
linha_tempo = 'Começou a Trabalhar na Caltech,Trabalho sobre a String Theory,Ganhar o Chancellor de ciência,Pensar na Teoria de Cooper-Hofstader,Criou a Super Assimetria,Ganhar o Nobel'.split(',')
xingamentos = 'Tinha que ser o engenheiro sem Phd do Wolowitz,Leonard seu anão covarde,Tu é muito burro Raj'.split(',')

# Variável para verificação dos "Bazingas" após conquistas válidas
conquista_valida = False

contador_conquista = 0
parabens_sheldon = False
while not parabens_sheldon:
    while True:
        conquista = input()

        # Caso Sheldon desista
        if conquista == 'É o fim da Estrada pra Sheldon Cooper':
            parabens_sheldon = True
            break
        # Verificando se é Bazinga, ou se é outra frase qualquer, ou se é um xingamento
        elif conquista == 'Bazinga' and conquista_valida:
            contador_conquista -= 1
            conquista_valida = False
            continue
        elif conquista in xingamentos:
            conquista_valida = False
            print('Não xingue seus amigos Sheldon!')
            continue
        elif conquista not in linha_tempo:
            conquista_valida = False
            continue

        # Caso sejam as conquistas corretas
        if conquista == linha_tempo[0] and contador_conquista == 0:
            contador_conquista += 1
            conquista_valida = True
        elif conquista == linha_tempo[1] and contador_conquista == 1:
            contador_conquista += 1
            conquista_valida = True
        elif conquista == linha_tempo[2] and contador_conquista == 2:
            contador_conquista += 1
            conquista_valida = True
        elif conquista == linha_tempo[3] and contador_conquista == 3:
            contador_conquista += 1
            conquista_valida = True
        elif conquista == linha_tempo[4] and contador_conquista == 4:
            contador_conquista += 1
            conquista_valida = True
        # Caso ele chegue no Nobel
        elif conquista == linha_tempo[5] and contador_conquista == 5:
            parabens_sheldon = True
            contador_conquista += 1
            break
else:
    # Outputs
    if contador_conquista == 0:
        print('Que potencial desperdiçado...')
    elif contador_conquista == 1 or contador_conquista == 2:
        print('Tão perto, mas tão longe')
    elif contador_conquista == 3 or contador_conquista == 4:
        print('Não desista Sheldon, você ainda têm muito para alcançar!')
    elif contador_conquista == 5:
        print('Nãoooooo, esse momento ia ser seu Sheldon')
    # Usando a mesma variável do while indicando se sheldon ganhou o Nobel
    elif parabens_sheldon:
        print('Você conseguiu Sheldon, o Nobel é seu!!!')
