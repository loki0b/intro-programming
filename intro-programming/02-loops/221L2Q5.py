total_reacao = 0
reacao_bazinga = 0

while True:
    piada = input()
    if piada == 'Fim do Show!':
        break
    reacao = input()

    if reacao == 'BAZINGA!':
        reacao_bazinga += 1
        total_reacao += 1
    else:
        total_reacao += 1

# Outputs
if reacao_bazinga > total_reacao * 0.6:
    print('BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!')
elif reacao_bazinga < total_reacao * 0.4:
    print('Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!')
else:
    print('Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!')
