pokedex = {}

finished = False
while not finished:
    try:
        pokemon = input().split()
        if pokemon[0] == 'ADD':
            if pokemon[1] in pokedex:
                print('Pokémon já adicionado na Pokédex')

            else:
                descricao = input()
                pokemon_add = {pokemon[1]: descricao}
                pokedex.update(pokemon_add)
                print('Pokémon adicionado com sucesso')

        elif pokemon[0] == 'DESC':
            if pokemon[1] not in pokedex:
                print('Ainda não há registro desse Pokémon')

            else:
                print(pokedex[pokemon[1]])

    except EOFError:
        finished = True
