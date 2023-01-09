temperatura = 30
fome = True
internet = 0

parar = True

while parar:
    acao = input()
    if acao == 'ir para o grad':
        temperatura -= 5
        internet += 300
    elif acao == 'sair para a rua':
        temperatura += 5
    elif acao == 'comer uma quentinha':
        fome = False
    elif acao == 'conectar no wifi':
        internet += 100
    elif acao == 'parar':
        parar = False
    else:
        print('Entrada inválida')
        continue
else:
    if temperatura >= 30:
        print('A temperatura aqui não está agradável')
    elif temperatura <= 25:
        print('Agora sim, está aconchegante')

    if fome:
        print('Meu corpo precisa de comida')

    if internet < 100:
        print('Essa conexão está horrível')

    if not fome and temperatura <= 25 and internet >= 300:
        print('Finalmente um lugar preciso para mim!')
