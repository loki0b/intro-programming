# Recebendo e convertendo quantidade de instruções
qtd_instru = int(input(), 2)

# Valores das instruções

# Planeta
planeta = False
beleza = False
e_t = False
agua = False
temperatura = False
qtd_luas = 0

# Galaxia
galaxia = False
qnt_planetas_em_milhoes = 0
buraco_negro_galaxia = False

# Buraco negro
buraco_negro = False
massa_buraco_negro = 0
spin_buraco_negro = 0
carga_buraco_negro = 0

# Recebendo instruções
for i in range(qtd_instru):
    instru = int(input(), 2)

    # Caso seja planeta
    if instru == 5:

        planeta = True
        while True:
            caracteristica = str(input())

            if caracteristica == 'Beleza':
                beleza = bool(int(input()))
            elif caracteristica == 'Possibilidade de vida extraterrestre':
                e_t = bool(int(input()))
            elif caracteristica == 'Agua aparente':
                agua = bool(int(input()))
            elif caracteristica == 'Temperatura adequada':
                temperatura = bool(int(input()))
            elif caracteristica == 'Quantidade de luas':
                qtd_luas = int(input(), 2)
            elif caracteristica == 'End':
                if agua and temperatura and beleza and e_t:
                    print(f'Achamos o planeta ideal e ainda tem {qtd_luas} lua(s)!')
                    print('Parece bom demais pra ser verdade, que tipo de vida sera que nos aguarda?')

                elif agua and temperatura and beleza and not e_t:
                    print('Ainda nao sabemos se o planeta e habitavel, parece nao haver vida')

                elif agua and temperatura and e_t and not beleza:
                    print(f'O planeta e possivelmente habitavel porem olha essa aparencia, mesmo que tenha {qtd_luas} '
                          f'lua(s) vamos omitir esse do relatorio!')
                elif not agua and not temperatura and not e_t:
                    print('Vish! Esse nao satisfaz nem as condicoes basicas, nao perderemos tempo')

                break

    # Caso seja galáxia
    elif instru == 13:

        galaxia = True
        qnt_planetas_em_milhoes = int(input(), 2)
        buraco_negro_galaxia = bool(int(input()))

        if buraco_negro_galaxia:
            print(f'Ha um buraco negro supermassivo nesta galaxia, demais! Alem da existencia de cerca de '
                  f'{qnt_planetas_em_milhoes} milhoes de planetas')
        else:
            print(
                f'Aparentemente nao ha nenhum buraco negro supermassivo no centro dessa galaxia, jurava que todas tinham!'
                f' Nao importa, ainda temos {qnt_planetas_em_milhoes} milhoes de planetas para observar algum '
                f'deve apresentar possiblidade de vida')

    # Caso seja buraco negro
    elif instru == 0:

        buraco_negro = True
        massa_buraco_negro = int(input(), 2)
        spin_buraco_negro = int(input())
        carga_buraco_negro = int(input(), 2)

        print('Conseguimos todas informacoes necessarias para classificar este buraco negro no nosso banco de dados!')
        print('De acordo com as analises, o buraco negro:')
        print(f'- Tem massa de aproximadamente {massa_buraco_negro} milhoes massas solares')
        print(f'- Possui em media {spin_buraco_negro} rotacao(oes) por segundo')
        if carga_buraco_negro == 0:
            carga_buraco_negro = 'Apresenta carga inexistente ou nula'

        elif carga_buraco_negro == 1:
            carga_buraco_negro = 'Apresenta carga positiva'

        else:
            carga_buraco_negro = 'Apresenta carga negativa'

        print(f'- {carga_buraco_negro}')

    # Planeta
    planeta = False
    beleza = False
    e_t = False
    agua = False
    temperatura = False
    qtd_luas = 0

    # Galaxia
    galaxia = False
    qnt_planetas_em_milhoes = 0
    buraco_negro_galaxia = False

    # Buraco negro
    buraco_negro = False
    massa_buraco_negro = 0
    spin_buraco_negro = 0
    carga_buraco_negro = 0
