# Funções para cada operação
def soma(x, lista_nums):
    resultd = x
    for num in lista_nums[1:]:
        resultd += num

    return resultd


def subtracao(x, lista_nums):
    resultd = x
    for num in lista_nums[1:]:
        resultd -= num

    return resultd


def multiplicacao(x, lista_nums):
    resultd = x
    for num in lista_nums[1:]:
        resultd *= num

    return resultd


def divisao(x, lista_nums):
    resultd = x
    for num in lista_nums[1:]:
        resultd /= num

    return resultd


# Loop até que finished == 1
finished = 1
while finished == 1:
    # Determinando operação a ser feita e recebendo quantidade de números
    operacao = input()
    qtd_nums = int(input())

    numeros = []
    for i in range(qtd_nums):
        numeros.append(int(input()))

    if operacao == 'S':
        resultado = soma(numeros[0], numeros)
        print(resultado)
        numeros.clear()

    elif operacao == 'sub':
        resultado = subtracao(numeros[0], numeros)
        print(resultado)
        numeros.clear()

    elif operacao == 'M':
        resultado = multiplicacao(numeros[0], numeros)
        print(resultado)
        numeros.clear()

    elif operacao == 'D':
        resultado = divisao(numeros[0], numeros)
        print(resultado)
        numeros.clear()

    finished = int(input())
