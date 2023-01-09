quadrilha = input()
step1 = input()
step2 = input()
step3 = input()
step4 = input()
step5 = input()

steps = 'Cumprimento Balancê Passeio Túnel Serrote Casamento Despedida'

finalscore = 0.0

if step1 == 'Cumprimento':
    finalscore += 100
elif step1 == 'Balancê':
    finalscore += 50
elif step1 == 'Passeio':
    finalscore += 70
elif step1 == 'Serrote':
    finalscore += 100
elif step1 == 'Túnel':
    finalscore -= finalscore * 0.1

if step2 == 'Cumprimento':
    finalscore += 10
elif step2 == 'Balancê':
    finalscore += 50
elif step2 == 'Passeio':
    finalscore += 70
elif step2 == 'Serrote':
    finalscore += 100
elif step2 == 'Túnel':
    finalscore -= finalscore * 0.1

if step3 == 'Cumprimento':
    finalscore += 10
elif step3 == 'Balancê':
    finalscore += 50
elif step3 == 'Passeio':
    finalscore += 70
elif step3 == 'Serrote':
    finalscore += 100
elif step3 == 'Túnel':
    finalscore -= finalscore * 0.1

if step4 == 'Cumprimento':
    finalscore += 10
elif step4 == 'Balancê':
    finalscore += 50
elif step4 == 'Passeio':
    finalscore += 70
elif step4 == 'Serrote':
    finalscore += 100
elif step4 == 'Túnel':
    finalscore -= finalscore * 0.1

if step5 == 'Cumprimento':
    finalscore += 10
elif step5 == 'Balancê':
    finalscore += 50
elif step5 == 'Passeio':
    finalscore += 70
elif step5 == 'Serrote':
    finalscore += 100
elif step5 == 'Despedida':
    finalscore += 35
elif step5 == 'Túnel':
    finalscore -= finalscore * 0.1

if step1 == 'Casamento' or step2 == 'Casamento' or step3 == 'Casamento' or step4 == 'Casamento' or step5 == 'Casamento':
    finalscore *= 2

if step1 not in steps or step2 not in steps or step3 not in steps or step4 not in steps or step5 not in steps:
    finalscore = 0

if finalscore == 0:
    print(f'Poxa, {quadrilha}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')
elif finalscore > 0:
    print(f'Parabéns, {quadrilha}! Bela apresentação. A pontuação foi de {finalscore:.1f}!')
