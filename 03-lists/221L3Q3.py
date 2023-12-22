# Guardando os alunos com todos sintomas e verificando se Max apareceu na lista e/ou está como todos sintomas
alunos_all_sint = []
max_in_list = False
max_all_sint = False

# Iterando até a variável descobrir se tornar !True
descobrir = False
while not descobrir:
    aluno_sint = str(input()).split(', ')

    if 'descobrir' in aluno_sint:
        descobrir = True

    else:
        # Verificando Max
        if 'Max' in aluno_sint[0]:
            max_in_list = True

            dor_cabeca = False
            insonia = False
            pesadelos = False
            suor_frio = False
            visoes = False

            for sintoma in aluno_sint:
                if sintoma == 'dor de cabeca':
                    dor_cabeca = True

                elif sintoma == 'insonia':
                    insonia = True

                elif sintoma == 'pesadelos':
                    pesadelos = True

                elif sintoma == 'suor frio':
                    suor_frio = True

                elif sintoma == 'visoes':
                    visoes = True

            if dor_cabeca and insonia and pesadelos and suor_frio and visoes:
                max_all_sint = True
                alunos_all_sint.append(aluno_sint[0])

        # Verificando demais alunos
        else:
            dor_cabeca = False
            insonia = False
            pesadelos = False
            suor_frio = False
            visoes = False

            for sintoma in aluno_sint:
                if sintoma == 'dor de cabeca':
                    dor_cabeca = True

                elif sintoma == 'insonia':
                    insonia = True

                elif sintoma == 'pesadelos':
                    pesadelos = True

                elif sintoma == 'suor frio':
                    suor_frio = True

                elif sintoma == 'visoes':
                    visoes = True

            if dor_cabeca and insonia and pesadelos and suor_frio and visoes:
                alunos_all_sint.append(aluno_sint[0])

# Output
# Caso nenhum aluno tenha todos os sintomas
if not alunos_all_sint:
    print('Não conseguimos encontrar ninguém com esses sintomas, o próximo ataque do Vecna será imprevisível.')

# Caso Max não esteja na entrada ou não tenha todos sintomas
elif not max_in_list or not max_all_sint and alunos_all_sint:
    print(f'Tem {len(alunos_all_sint)} pessoa(s) na mira do Vecna!')

# Caso Max tenha todos sintomas
elif max_all_sint:
    print('Oh não, Max está em perigo! Let\'s run up that hill com a Kate Bush e ajudar nossa amiga.')
    # Caso Max não seja a única com todos sintomas
    if len(alunos_all_sint) > 1:
        print(f'Além dela, tem mais {len(alunos_all_sint) - 1} pessoa(s) na mira do Vecna!')

# Output final
# Caso seja apenas um aluno não sendo a Max
if len(alunos_all_sint) == 1 and not max_all_sint:
    print(f'Precisamos avisar {alunos_all_sint[0]} para preparar sua música favorita.')

# Caso seja mais de um aluno, sem contar a Max
elif len(alunos_all_sint) > 1:
    if max_all_sint and len(alunos_all_sint) == 2:
        for aluno in alunos_all_sint:
            if aluno != 'Max':
                print(f'Precisamos avisar {aluno} para preparar sua música favorita.')
    else:
        print(f'Precisamos avisar', end=' ')
        for i in range(len(alunos_all_sint)):
            if i == len(alunos_all_sint) - 1:
                print(f'e {alunos_all_sint[i]} para prepararem suas músicas favoritas.')
            else:
                if alunos_all_sint[i] != 'Max':
                    if i == len(alunos_all_sint) - 2:
                        print(f'{alunos_all_sint[i]} ', end='')
                    else:
                        print(f'{alunos_all_sint[i]}, ', end='')
