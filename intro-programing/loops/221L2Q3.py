# Ponto de partida sempre 0
ponto_final = 0
# local-mapa onde se deseja chegar
local_mapa = int(input())

# iteração dos números
while True:
    n = int(input())
    if n > -1:
        for i in range(n+1):
            ponto_final += i
    else:
        break

# outputs de saída
if ponto_final < local_mapa:
    print('Ainda falta um pouco...')
elif ponto_final == local_mapa:
    print('Parabéns!!! Você é o mais inteligente')
elif local_mapa < ponto_final < local_mapa * 19:
    print('Parece que o gêniozinho passou um pouco do local...')
elif local_mapa < ponto_final and (local_mapa * 19 < ponto_final < local_mapa * 101):
    print('Acho que sua grande inteligência fez você se perder um pouco no caminho, onde estamos?')
elif ponto_final > local_mapa * 101:
    print('Hum... acho que o gêniozinho não tem mesmo doutorado ein...')
