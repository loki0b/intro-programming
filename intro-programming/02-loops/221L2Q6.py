boa_noite = True

while boa_noite:
    # Recebendo inputs
    for i in range(3):
        toc = input()
        if toc == 'Boa noite':
            boa_noite = False
            break
        else:
            # Manipulando escolhas
            if toc == 'toc-toc-toc':
                penny = input()
                if penny == 'Boa noite':
                    boa_noite = False
                    break
                elif penny == 'Penny':
                    comparador = True
                else:
                    comparador = False
            else:
                comparador = False

        # Se tudo ok
        if comparador:
            print(i+1)
        else:
            # Se não
            print('Não pode entrar, se identifique!!!')
            break
    else:
        print('Pode entrar Sheldon')
else:
    print('Boa noite Penny')
