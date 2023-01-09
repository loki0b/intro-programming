nome_1 = input()
pontuacao_1 = int(input())

nome_2 = input()
pontuacao_2 = int(input())

nome_3 = input()
pontuacao_3 = int(input())

primeiro = ''
segundo = ''
terceiro = ''

pontuacao_primeiro = 0
pontuacao_segundo = 0
pontuacao_terceiro = 0

if pontuacao_1 == pontuacao_2 and pontuacao_2 == pontuacao_3:
    if nome_1 < nome_2 and nome_1 < nome_3:
        primeiro = nome_1
        pontuacao_primeiro = pontuacao_1
        if nome_2 < nome_3:
            segundo = nome_2
            pontuacao_segundo = pontuacao_2
            terceiro = nome_3
            pontuacao_terceiro = pontuacao_3
        else:
            segundo = nome_3
            pontuacao_segundo = pontuacao_3
            terceiro = nome_2
            pontuacao_terceiro = nome_2
    elif nome_2 < nome_3:
        primeiro = nome_2
        pontuacao_primeiro = pontuacao_2
        if nome_1 < nome_3:
            segundo = nome_1
            pontuacao_segundo = pontuacao_1
            terceiro = nome_3
            pontuacao_terceiro = pontuacao_3
        else:
            segundo = nome_3
            pontuacao_segundo = pontuacao_3
            terceiro = nome_1
            pontuacao_terceiro = pontuacao_1
    else:
        primeiro = nome_3
        pontuacao_primeiro = pontuacao_3
        if nome_1 < nome_2:
            segundo = nome_1
            pontuacao_segundo = pontuacao_1
            terceiro = nome_2
            pontuacao_terceiro = pontuacao_2
        else:
            segundo = nome_2
            pontuacao_segundo = pontuacao_2
            terceiro = nome_1
            pontuacao_terceiro = pontuacao_1
elif pontuacao_1 == pontuacao_2 or pontuacao_2 == pontuacao_3 or pontuacao_3 == pontuacao_1:
    if pontuacao_1 == pontuacao_2 and pontuacao_1 < pontuacao_3:
        if nome_1 < nome_2:
            primeiro = nome_1
            pontuacao_primeiro = pontuacao_1
            segundo = nome_2
            pontuacao_segundo = pontuacao_2
            terceiro = nome_3
            pontuacao_terceiro = pontuacao_3
        else:
            primeiro = nome_2
            pontuacao_primeiro = pontuacao_2
            segundo = nome_1
            pontuacao_segundo = pontuacao_1
            terceiro = nome_3
            pontuacao_terceiro = pontuacao_3
    elif pontuacao_2 == pontuacao_3 and pontuacao_2 < pontuacao_1:
        if nome_2 < nome_3:
            primeiro = nome_2
            pontuacao_primeiro = pontuacao_2
            segundo = nome_3
            pontuacao_segundo = pontuacao_3
            terceiro = nome_1
            pontuacao_terceiro = pontuacao_1
        else:
            primeiro = nome_3
            pontuacao_primeiro = pontuacao_3
            segundo = nome_2
            pontuacao_segundo = pontuacao_2
            terceiro = nome_1
            pontuacao_terceiro = pontuacao_1
    elif pontuacao_3 == pontuacao_1 and pontuacao_3 < pontuacao_2:
        if nome_3 < nome_1:
            primeiro = nome_3
            pontuacao_primeiro = pontuacao_3
            segundo = nome_1
            pontuacao_segundo = pontuacao_1
            terceiro = nome_2
            pontuacao_terceiro = pontuacao_2
        else:
            primeiro = nome_1
            pontuacao_primeiro = pontuacao_1
            segundo = nome_3
            pontuacao_segundo = pontuacao_3
            terceiro = nome_2
            pontuacao_terceiro = pontuacao_2

if pontuacao_1 < pontuacao_2 and pontuacao_1 < pontuacao_3:
    primeiro = nome_1
    pontuacao_primeiro = pontuacao_1
    if pontuacao_2 == pontuacao_3:
        if nome_2 < nome_3:
            segundo = nome_2
            pontuacao_segundo = pontuacao_2
            terceiro = nome_3
            pontuacao_terceiro = pontuacao_3
        else:
            segundo = nome_3
            pontuacao_segundo = pontuacao_3
            terceiro = nome_2
            pontuacao_terceiro = pontuacao_2
    elif pontuacao_2 < pontuacao_3:
        segundo = nome_2
        pontuacao_segundo = pontuacao_2
        terceiro = nome_3
        pontuacao_terceiro = pontuacao_3
    else:
        segundo = nome_3
        pontuacao_segundo = pontuacao_3
        terceiro = nome_2
        pontuacao_terceiro = pontuacao_2

if pontuacao_2 < pontuacao_1 and pontuacao_2 < pontuacao_3:
    primeiro = nome_2
    pontuacao_primeiro = pontuacao_2
    if pontuacao_1 == pontuacao_3:
        if nome_1 < nome_3:
            segundo = nome_1
            pontuacao_segundo = pontuacao_1
            terceiro = nome_3
            pontuacao_terceiro = pontuacao_3
        else:
            segundo = nome_3
            pontuacao_segundo = pontuacao_3
            terceiro = nome_1
            pontuacao_terceiro = pontuacao_1
    elif pontuacao_1 < pontuacao_3:
        segundo = nome_1
        pontuacao_segundo = pontuacao_1
        terceiro = nome_3
        pontuacao_terceiro = pontuacao_3
    else:
        segundo = nome_3
        pontuacao_segundo = pontuacao_3
        terceiro = nome_1
        pontuacao_terceiro = pontuacao_1

if pontuacao_3 < pontuacao_1 and pontuacao_3 < pontuacao_2:
    primeiro = nome_3
    pontuacao_primeiro = pontuacao_3
    if pontuacao_1 == pontuacao_2:
        if nome_1 < nome_2:
            segundo = nome_1
            pontuacao_segundo = pontuacao_1
            terceiro = nome_2
            pontuacao_terceiro = pontuacao_2
        else:
            segundo = nome_2
            pontuacao_segundo = pontuacao_2
            terceiro = nome_1
            pontuacao_terceiro = pontuacao_1
    elif pontuacao_1 < pontuacao_2:
        segundo = nome_1
        pontuacao_segundo = pontuacao_1
        terceiro = nome_2
        pontuacao_terceiro = pontuacao_2
    else:
        segundo = nome_2
        pontuacao_segundo = pontuacao_2
        terceiro = nome_1
        pontuacao_terceiro = pontuacao_1

print(f'{primeiro} {pontuacao_primeiro}\n{segundo} {pontuacao_segundo}\n{terceiro} {pontuacao_terceiro}')
