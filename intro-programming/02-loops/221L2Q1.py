rodadas = int(input())
pontos_sheldon = 0
pontos_raj = 0

for i in range(rodadas):
    escolha_sheldon = input()
    escolha_raj = input()

    if escolha_sheldon == 'lagarto':
        if escolha_raj == 'spock':
            pontos_sheldon += 1
        elif escolha_raj == 'tesoura':
            pontos_raj += 1
    elif escolha_sheldon == 'spock':
        if escolha_raj == 'tesoura':
            pontos_sheldon += 1
        elif escolha_raj == 'lagarto':
            pontos_raj += 1
    elif escolha_sheldon == 'tesoura':
        if escolha_raj == 'lagarto':
            pontos_sheldon += 1
        elif escolha_raj == 'spock':
            pontos_raj += 1

if pontos_sheldon > pontos_raj:
    print('BAZINGA! EU SOU O SENHOR DA SALA!')
elif pontos_raj > pontos_sheldon:
    print('ENGOLE ESSA, SHELDON!')
else:
    print('Oh não, precisamos de outra rodada.')
