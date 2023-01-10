dono_lista = str(input())
tamanho_lista = int(input())

nome_filme = []
nota_filme = []

# Separando nomes e notas dos filmes por index
for i in range(tamanho_lista):
    aux = str(input()).split(' - ')
    nome_filme.append(aux[0])
    nota_filme.append((aux[1]))

# Organizando notas e nomes dos filmes, do maior para a menor
for item in nota_filme:
    for i in range(tamanho_lista - 1):
        if nota_filme[i] < nota_filme[i + 1]:
            # Notas
            aux_nota = nota_filme.pop(i)
            nota_filme.insert(i + 1, aux_nota)

            # Nomes
            aux_nome = nome_filme.pop(i)
            nome_filme.insert(i + 1, aux_nome)

# Output
if dono_lista == 'Bonna':
    print('Os filmes sugeridos por Bonna são:')
elif dono_lista == 'João':
    print('Os filmes sugeridos por João são:')

for i in range(tamanho_lista):
    print(f'{nome_filme[i]} - {nota_filme[i]}')
