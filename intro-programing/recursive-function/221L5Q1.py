# Função para separar o número em uma lista
def converter_lista(lista_num):
    lista_num_separado = []
    for num in lista_num:
        lista_num_separado.append(int(num))

    return lista_num_separado


# Função para somar os digitos
def soma_digitos(lista_num):
    soma = 0
    if len(lista_num) == 1:
        soma += lista_num[0]

    else:
        lista_nao_somada = lista_num[1:]
        soma += lista_num[0] + soma_digitos(lista_nao_somada)

    return soma


# Função para encontrar MDC
def mdc(x, y):
    if x < y:
        return mdc(y, x)

    if y == 0:
        return x

    resto = x % y
    return mdc(y, resto)


digitos_somados = []
for i in range(3):
    numero = converter_lista(input())
    digitos_somados.append(soma_digitos(numero))


MDC = mdc(digitos_somados[0], digitos_somados[1])
MDC = mdc(MDC, digitos_somados[2])

print(f'O MDC obtido é: {MDC}')

