music = input()
genre = input()

if genre == 'Xote' or genre == 'Forró':
    print(f"'{music}' foi adicionada com sucesso na playlist 'Dandrilha'.")
else:
    print(f"Ocorreu um erro ao adicionar '{music}' na playlist.")
