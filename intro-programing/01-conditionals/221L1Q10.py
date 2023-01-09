poderes = 'fogo gelo eletricidade'
magia = 'null'

# Entidade Sao Joao
saojoao = 'São João'
vida_saojoao = int(input())
ataque_saojoao = int(input())
defesa_saojoao = int(input())
fraqueza_saojoao = ''
poder = str(input())
if poder in poderes:
    fraqueza_saojoao = poder
resistencia_saojoao = ''
poder = str(input())
if poder in poderes:
    resistencia_saojoao = poder

# Entidade adversária
nome_entidade = str(input())
vida_entidade = int(input())
ataque_entidade = int(input())
defesa_entidade = int(input())
fraqueza_entidade = ''
poder = str(input())
if poder in poderes:
    fraqueza_entidade = poder
resistencia_entidade = ''
poder = str(input())
if poder in poderes:
    resistencia_entidade = poder

dano_geral_saojoao = ataque_saojoao - defesa_entidade
dano_geral_entidade = ataque_entidade - defesa_saojoao
dano_ataque = 0

# Turno 1
anular = False
print(f'Turno: {1}')

ataque_1 = str(input())

if ataque_1 == 'Ataque Físico':
    magia = 'null'
    dano_ataque = dano_geral_saojoao
elif ataque_1 == 'Agi':
    magia = 'fogo'
    if resistencia_entidade == magia:
        dano_ataque = dano_geral_saojoao // 2
    elif fraqueza_entidade == magia:
        dano_ataque = int(dano_geral_saojoao + dano_geral_saojoao * 0.7)
        anular = True
    else:
        dano_ataque = dano_geral_saojoao
elif ataque_1 == 'Bufu':
    magia = 'gelo'
    if resistencia_entidade == magia:
        dano_ataque = dano_geral_saojoao // 2
    elif fraqueza_entidade == magia:
        dano_ataque = int(dano_geral_saojoao + dano_geral_saojoao * 0.7)
        anular = True
    else:
        dano_ataque = dano_geral_saojoao
elif ataque_1 == 'Zio':
    magia = 'eletricidade'
    if resistencia_entidade == magia:
        dano_ataque = dano_geral_saojoao // 2
    elif fraqueza_entidade == magia:
        dano_ataque = int(dano_geral_saojoao + dano_geral_saojoao * 0.7)
        anular = True
    else:
        dano_ataque = dano_geral_saojoao

vida_entidade -= dano_ataque
if vida_entidade < 0:
    vida_entidade += abs(vida_entidade)

if magia == fraqueza_entidade:
    print(f'Isso! {saojoao} usou {ataque_1} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {nome_entidade} que agora tem {vida_entidade} de vida.')
elif magia == resistencia_entidade:
    print(f'{saojoao} usou {ataque_1}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {nome_entidade} que agora tem {vida_entidade} de vida.')
else:
    print(f'{saojoao} usou {ataque_1} e causou {dano_ataque} de dano em {nome_entidade} que agora tem {vida_entidade} de vida.')

# Fim turno 1
if vida_entidade == 0:
    print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
else:
    # Turno 2
    print(f'Turno: {2}')

    if anular:
        print(f'{nome_entidade} teve sua fraqueza em {magia} acertada, portanto não poderá agir.')

        # Turno 3 se ataque anulado
        print(f'Turno: {3}')

        ataque_3 = str(input())

        if ataque_3 == 'Ataque Físico':
            magia = 'null'
            dano_ataque = dano_geral_saojoao
        elif ataque_3 == 'Agi':
            magia = 'fogo'
            if resistencia_entidade == magia:
                dano_ataque = dano_geral_saojoao // 2
            elif fraqueza_entidade == magia:
                dano_ataque = int(dano_geral_saojoao + dano_geral_saojoao * 0.7)
                anular = True
            else:
                dano_ataque = dano_geral_saojoao
        elif ataque_3 == 'Bufu':
            magia = 'gelo'
            if resistencia_entidade == magia:
                dano_ataque = dano_geral_saojoao // 2
            elif fraqueza_entidade == magia:
                dano_ataque = int(dano_geral_saojoao + dano_geral_saojoao * 0.7)
                anular = True
            else:
                dano_ataque = dano_geral_saojoao
        elif ataque_3 == 'Zio':
            magia = 'eletricidade'
            if resistencia_entidade == magia:
                dano_ataque = dano_geral_saojoao// 2
            elif fraqueza_entidade == magia:
                dano_ataque = int(dano_geral_saojoao + dano_geral_saojoao * 0.7)
                anular = True
            else:
                dano_ataque = dano_geral_saojoao

        vida_entidade -= dano_ataque
        if vida_entidade < 0:
            vida_entidade += abs(vida_entidade)

        if magia == fraqueza_entidade:
            print(f'Isso! {saojoao} usou {ataque_3} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {nome_entidade} que agora tem {vida_entidade} de vida.')
        elif magia == resistencia_entidade:
            print(f'{saojoao} usou {ataque_3}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {nome_entidade} que agora tem {vida_entidade} de vida.')
        else:
            print(f'{saojoao} usou {ataque_3} e causou {dano_ataque} de dano em {nome_entidade} que agora tem {vida_entidade} de vida.')

        if vida_entidade == 0:
            print(f'Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        elif vida_entidade > 0:
            print(f'Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…')
    else:
        ataque_2 = str(input())

        if ataque_2 == 'Ataque Físico':
            magia = 'null'
            dano_ataque = dano_geral_entidade
        elif ataque_2 == 'Agi':
            magia = 'fogo'
            if fraqueza_saojoao == magia:
                dano_ataque = int(dano_geral_entidade + dano_geral_entidade * 0.7)
                anular = True
            elif resistencia_saojoao == magia:
                dano_ataque = dano_geral_entidade // 2
            else:
                dano_ataque = dano_geral_entidade
        elif ataque_2 == 'Bufu':
            magia = 'gelo'
            if resistencia_saojoao == magia:
                dano_ataque = dano_geral_entidade // 2
            elif fraqueza_saojoao == magia:
                dano_ataque = int(dano_geral_entidade + dano_geral_entidade * 0.7)
                anular = True
            else:
                dano_ataque = dano_geral_entidade
        elif ataque_2 == 'Zio':
            magia = 'eletricidade'
            if resistencia_saojoao == magia:
                dano_ataque = dano_geral_entidade // 2
            elif fraqueza_saojoao == magia:
                dano_ataque = int(dano_geral_entidade + dano_geral_entidade * 0.7)
                anular = True
            else:
                dano_ataque = dano_geral_entidade

        vida_saojoao -= dano_ataque
        if vida_saojoao < 0:
            vida_saojoao += abs(vida_saojoao)

        if magia == fraqueza_saojoao:
            print(f'Vixe! {nome_entidade} usou {ataque_2} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {saojoao} que agora tem {vida_saojoao} de vida.')
        elif magia == resistencia_saojoao:
            print(f'{nome_entidade} usou {ataque_2}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {saojoao} que agora tem {vida_saojoao} de vida.')
        else:
            print(f'{nome_entidade} usou {ataque_2} e causou {dano_ataque} de dano em {saojoao} que agora tem {vida_saojoao} de vida.')

        if vida_saojoao == 0:
            print(f'Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…')
        elif anular:
            print(f'Turno: 3')
            print(f'{saojoao} teve sua fraqueza em {fraqueza_saojoao} acertada, portanto não poderá agir.')
            print('Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…')
        # Fim turno 2
        else:
            # Turno 3 se ataque not anulado
            print(f'Turno: {3}')

            ataque_3 = str(input())

            if ataque_3 == 'Ataque Físico':
                magia = 'null'
                dano_ataque = dano_geral_saojoao
            elif ataque_3 == 'Agi':
                magia = 'fogo'
                if resistencia_entidade == magia:
                    dano_ataque = dano_geral_saojoao // 2
                elif fraqueza_entidade == magia:
                    dano_ataque = int(dano_geral_saojoao + dano_geral_saojoao * 0.7)
                    anular = True
                else:
                    dano_ataque = dano_geral_saojoao
            elif ataque_3 == 'Bufu':
                magia = 'gelo'
                if resistencia_entidade == magia:
                    dano_ataque = dano_geral_saojoao // 2
                elif fraqueza_entidade == magia:
                    dano_ataque = int(dano_geral_saojoao + dano_geral_saojoao * 0.7)
                    anular = True
                else:
                    dano_ataque = dano_geral_saojoao
            elif ataque_3 == 'Zio':
                magia = 'eletricidade'
                if resistencia_entidade == magia:
                    dano_ataque = dano_geral_saojoao // 2
                elif fraqueza_entidade == magia:
                    dano_ataque = int(dano_geral_saojoao + dano_geral_saojoao * 0.7)
                    anular = True
                else:
                    dano_ataque = dano_geral_saojoao

            vida_entidade -= dano_ataque
            if vida_entidade < 0:
                vida_entidade += abs(vida_entidade)

            if magia == fraqueza_entidade:
                print(f'Isso! {saojoao} usou {ataque_3} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {nome_entidade} que agora tem {vida_entidade} de vida.')
            elif magia == resistencia_entidade:
                print(f'{saojoao} usou {ataque_3}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {nome_entidade} que agora tem {vida_entidade} de vida.')
            else:
                print(f'{saojoao} usou {ataque_3} e causou {dano_ataque} de dano em {nome_entidade} que agora tem {vida_entidade} de vida.')

            if vida_entidade == 0:
                print(f'Vitória! Parece que o Nahobino São João reinará nesse solstício!')
            elif vida_entidade > 0:
                print(f'Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…')