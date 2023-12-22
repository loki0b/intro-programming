from math import pow, sqrt

def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


qtd_estrelas = int(input())

if qtd_estrelas <= 0:
    print('Isso está quebrado, acho que Howard pode me ajudar.')

elif qtd_estrelas < 3:
    print('Acho que bebi demais, eu juro que tinha mais estrelas!')

else:
    maior_distancia = 0
    soma_distancia = 0
    distancias = list()
    vetores_estrelas = list()

    for count in range(qtd_estrelas):
        
        estrela_x = float(input())
        estrela_y = float(input())
        vetores_estrelas.append([estrela_x, estrela_y])

    for i in range(qtd_estrelas):

        try:
            distancia = int(sqrt(pow(vetores_estrelas[i][0] - vetores_estrelas[i+1][0], 2) + pow(vetores_estrelas[i][1] - vetores_estrelas[i+1][1], 2)))
            
            soma_distancia += distancia

            distancias.append(distancia)

            if distancia > maior_distancia:
                maior_distancia = distancia

            print(f'Distância [star{i+1} <-> star{i+2}]: {distancia}')
        
        except IndexError:
            break
    
    count_fib = 0
    for num in distancias:   
        if is_fibonacci(num):
            count_fib += 1
    
    if count_fib == len(distancias):
        if is_prime(soma_distancia):
            print('Oh my god! Eu vou ganhar o Nobel primeiro que Sheldon!')
        
        else:
            print('Yes! Eu consegui!')
    
    elif count_fib == len(distancias) - 1:
        print('Oh, não! Eu quase consegui!')
    
    else:

        if is_prime(soma_distancia):
            print('Pelo menos o programa está funcionando...')
        else:
            print('Eu vou acabar como o Stuart :/')

