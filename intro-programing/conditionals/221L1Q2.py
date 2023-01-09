day = int(input())

if day == 20 or day < 17 or day > 26:
    print('Você escolheu um dia que não irá acontecer nenhum show, tente novamente!')
elif day % 2 == 0:
    print('Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!')
elif day % 2 == 1:
    print('Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!')