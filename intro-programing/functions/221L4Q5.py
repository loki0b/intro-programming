# Funções auxiliares
def decompor_numero(numero):
    if numero <= 9:
        return numero

    else:
        soma_num = (numero // 10) + (numero % 10)

        return soma_num


# Serviços que podem ser feitos
def pedras_quentes(gorjeta_atual, tempo_decorrido):
    gorjeta_coletada = (tempo_decorrido + gorjeta_atual) // 2

    return gorjeta_coletada


def massagem_pes(gorjeta_atual):
    if gorjeta_atual % 2 == 0:
        gorjeta_coletada = (gorjeta_atual % 7) * 6

    else:
        gorjeta_coletada = (gorjeta_atual % 7) ** 2

    return gorjeta_coletada


def servir_refeicao(gorjeta_atual):
    gorjeta = gorjeta_atual

    if gorjeta % 10 == 0:
        gorjeta_coletada = 5

        return gorjeta_coletada

    else:
        finished_ = False
        while not finished_:
            if gorjeta % 10 != 0:
                gorjeta += 1

            else:
                finished_ = True

        gorjeta_coletada = gorjeta - gorjeta_atual

        return gorjeta_coletada


def massagem_completa(gorjeta_atual):
    gorjeta_coletada = decompor_numero(gorjeta_atual)

    return gorjeta_coletada


# Iniciando
tempo = 0
total_gorjetas = 10

finished = False
while not finished:
    servico = input()

    if servico == 'pedras':
        total_gorjetas += pedras_quentes(total_gorjetas, tempo)
        tempo += 20
        print(f'Voce concluiu o servico de {"Pedras Quentes"} e agora possui {total_gorjetas} gorjetas.')

    elif servico == 'pes':
        total_gorjetas += massagem_pes(total_gorjetas)
        tempo += 30
        print(f'Voce concluiu o servico de {"Massagem nos Pes"} e agora possui {total_gorjetas} gorjetas.')

    elif servico == 'refeicao':
        total_gorjetas += servir_refeicao(total_gorjetas)
        tempo += 15
        print(f'Voce concluiu o servico de {"Servir Refeicao"} e agora possui {total_gorjetas} gorjetas.')

    elif servico == 'completa':
        total_gorjetas += massagem_completa(total_gorjetas)
        tempo += 50
        print(f'Voce concluiu o servico de {"Massagem Completa"} e agora possui {total_gorjetas} gorjetas.')

    else:
        tempo += 5
        print(f'O cliente fez voce perder tempo, voce ainda possui {total_gorjetas} gorjetas.')

    if total_gorjetas >= 50:
        finished = True

    elif tempo > 120:
        finished = True


if total_gorjetas >= 50:
    print(f'Você acumulou {total_gorjetas} gorjetas, com essa quantidade voce conseguira comprar sua passagem '
          f'de saida e salvar seus pais.')

else:
    print(f'Voce nao conseguiu o minimo necessario para comprar a passagem de saida desse mundo e salvar '
          f'seus pais.')
