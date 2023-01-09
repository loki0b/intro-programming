# Recebendo número de planetas
while True:
    n_planetas = int(input())
    if n_planetas < 2:
        print('Número inválido, tente novamente')
    else:
        break

mais_habitavel = 10
planeta = ''
indice_anterior = 0

for i in range(n_planetas):
    nome_planeta = input()
    raio_planeta = float(input())
    massa_planeta = float(input())
    temperatura_planeta = int(input())

    # Calculo de habitabilidade
    indice_habitabilidade = (raio_planeta + massa_planeta + temperatura_planeta/288) / 3

    # Julgando o mais habitavel
    if i == 0:
        # Primeiro planeta
        mais_habitavel = indice_habitabilidade
        planeta = nome_planeta
        indice_anterior = indice_habitabilidade
    # Demais planetas
    elif indice_anterior > indice_habitabilidade > 1:
        mais_habitavel = indice_habitabilidade
        planeta = nome_planeta
    elif indice_anterior < indice_habitabilidade < 1:
        mais_habitavel = indice_habitabilidade
        planeta = nome_planeta
        indice_anterior = indice_habitabilidade
    elif indice_habitabilidade == 1:
        mais_habitavel = indice_habitabilidade
        planeta = nome_planeta
        break

else:
    # Outputs
    if mais_habitavel == 1:
        print(f'{planeta} é perfeito!')
    elif mais_habitavel < 1:
        print(f'{planeta} vai dar pro gasto')
    elif mais_habitavel > 1:
        print(f'{planeta} vai ter que servir')
