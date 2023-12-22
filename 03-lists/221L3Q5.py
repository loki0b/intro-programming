# Recebendo inputs e separando em listas
sequencia_partidas = input().split(' ')
sequencia_modificacao = input().split(' ')

# Pontos totais antes da verificação de interferência
pontos_total_sem_verificacao = 0
for partida in sequencia_partidas:
    if partida == 'V':
        pontos_total_sem_verificacao += 3

    elif partida == 'E':
        pontos_total_sem_verificacao += 1

# Verificando as interferências e as modificando
for i in range(len(sequencia_partidas)):
    if sequencia_modificacao[i] == '1':
        if sequencia_partidas[i] == 'V':
            sequencia_partidas.pop(i)
            sequencia_partidas.insert(i, 'E')
            print('O maldito sapo interferiu no resultado! O que parecia uma vitória garantida terminou em um empate.')

        elif sequencia_partidas[i] == 'E':
            sequencia_partidas.pop(i)
            sequencia_partidas.insert(i, 'D')
            print('O anfíbio da maldição interferiu no resultado! Um empate tranquilo virou uma frustrante derrota.')

        elif sequencia_partidas[i] == 'D':
            print('O que já era ruim, se tornou uma humilhante derrota. Desgraçado desse sapo!')

# Pontos totais depois da verificação de interferência
pontuacao_final = 0

# Verificando desempenho da equipe a cada 4 jogos
count = 0
n_fatia = 1
while count < 9:
    soma_pont_4jogos = 0
    for partida in sequencia_partidas[count:count + 4]:
        if partida == 'V':
            soma_pont_4jogos += 3
            pontuacao_final += 3

        elif partida == 'E':
            soma_pont_4jogos += 1
            pontuacao_final += 1

    else:
        if soma_pont_4jogos == 7:
            print(f'A pontuação na {n_fatia}ª fatia de 4 jogos está dentro do planejado.')

        elif soma_pont_4jogos > 7:
            print(f'A pontuação na {n_fatia}ª fatia de 4 jogos está com uma gordurinha de {soma_pont_4jogos - 7} pontos.')

        elif soma_pont_4jogos < 7:
            print(f'A pontuação na {n_fatia}ª fatia de 4 jogos está abaixo da planejada em {7 - soma_pont_4jogos} pontos.')

    count += 4
    n_fatia += 1

# Verificando pontos perdidos
pontos_perdidos = pontos_total_sem_verificacao - pontuacao_final

if pontos_perdidos > 0:
    print(f'A maldição do sapo fez o Vascão perder {pontos_perdidos} pontos. Um número preocupante, que pode fazer diferença.')

elif pontos_perdidos == 0:
    print(f'A maldição parece que não teve impacto relevante! Não houve nenhuma perda de pontos.')

# Contando número de vitórias, empates e derrotas
vitorias = 0
empates = 0
derrotas = 0

for resultado in sequencia_partidas:
    if resultado == 'V':
        vitorias += 1

    elif resultado == 'E':
        empates += 1

    elif resultado == 'D':
        derrotas += 1
else:
    # Output final
    if pontuacao_final >= 21:
        print(f'Na reta final do campeonato, o Vasco garantiu um total de {pontuacao_final} pontos, com {vitorias} '
              f'vitórias, {empates} empates e {derrotas} derrotas, e alcançou o tão esperado acesso. '
              f'O Clube do Fomento Corporal vibra num SJ lotado!')

    else:
        print(f'Na reta final do campeonato, o Vasco fez somente {pontuacao_final} pontos, com {vitorias} vitórias, '
              f'{empates} empates e {derrotas} derrotas, e não conseguiu o acesso. Mais um ano de série B e '
              f'sofrimento. Mob, o clube e a torcida estão completamente desolados.')
