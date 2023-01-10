# Função para separar o nome, ataque, defesa e colocar numa tupla
def tratar_string(string):
    string = string.split()
    ataque = string.pop(-2)
    defesa = string.pop(-1)
    nome = ' '.join(string)

    tupla = (nome, ataque, defesa)

    return tupla


deck = list()

qtd_cartas = int(input())
for i in range(qtd_cartas):
    carta = tratar_string(input())
    deck.append({'nome': carta[0], 'ataque': carta[1], 'defesa': carta[2]})

# Verificando carta com maior ataque
maior_ataque = 0
for carta in deck:
    if int(carta['ataque']) > maior_ataque:
        maior_ataque = int(carta['ataque'])

else:
    for carta in deck:
        if int(carta['ataque']) == maior_ataque:
            print(f'Carta com maior poder de ataque: {carta["nome"]}\n'
                  f'Ataque: {carta["ataque"]}')

            break

# Verificando carta com maior defesa
maior_defesa = 0
for carta in deck:
    if int(carta['defesa']) > maior_defesa:
        maior_defesa = int(carta['defesa'])

else:
    for carta in deck:
        if int(carta['defesa']) == maior_defesa:
            print(f'Carta com maior poder de defesa: {carta["nome"]}\n'
                  f'Defesa: {carta["defesa"]}')

            break
