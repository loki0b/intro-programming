pe_mlq = input()
qtd_pe_mlq = int(input())
fat_pe_mlq = qtd_pe_mlq * 2

cocada = input()
qtd_cocada = int(input())
fat_cocada = qtd_cocada * 5

maca_amor = input()
qtd_maca_amor = int(input())
fat_maca_amor = qtd_maca_amor * 3

melhor_doce = ''
maior_faturamento = 0

if fat_pe_mlq > fat_cocada and fat_pe_mlq > fat_maca_amor:
    melhor_doce = pe_mlq
    maior_faturamento = fat_pe_mlq
elif fat_cocada > fat_maca_amor and fat_cocada > fat_pe_mlq:
    melhor_doce = cocada
    maior_faturamento = fat_cocada
elif fat_maca_amor > fat_cocada and fat_maca_amor > fat_pe_mlq:
    melhor_doce = maca_amor
    maior_faturamento = fat_maca_amor
else:
    if qtd_pe_mlq == 0 and qtd_pe_mlq == qtd_cocada and  qtd_pe_mlq == qtd_maca_amor:
        print('A ideia foi peba! Acho melhor encontrar um novo jeito de ganhar dinheiro...')
    elif fat_pe_mlq == fat_cocada and fat_pe_mlq == fat_maca_amor:
        if qtd_pe_mlq > qtd_cocada and qtd_pe_mlq > qtd_maca_amor:
            melhor_doce = pe_mlq
            maior_faturamento = fat_pe_mlq
        elif qtd_cocada > qtd_maca_amor:
            melhor_doce = cocada
            maior_faturamento = fat_cocada
        else:
            melhor_doce = maca_amor
            maior_faturamento = maca_amor
    elif fat_pe_mlq == fat_cocada:
        if qtd_pe_mlq > qtd_cocada:
            melhor_doce = pe_mlq
            maior_faturamento = fat_pe_mlq
        else:
            melhor_doce = cocada
            maior_faturamento = fat_cocada
    elif fat_pe_mlq == fat_maca_amor:
        if qtd_pe_mlq > qtd_maca_amor:
            melhor_doce = pe_mlq
            maior_faturamento = fat_pe_mlq
        else:
            melhor_doce = maca_amor
            maior_faturamento = fat_maca_amor
    elif fat_cocada == fat_maca_amor:
        if qtd_cocada > qtd_maca_amor:
            melhor_doce = cocada
            maior_faturamento = fat_cocada
        else:
            melhor_doce = maca_amor
            maior_faturamento = fat_maca_amor

if maior_faturamento > 0:
    print(f'Oxe! Você ganhou {maior_faturamento} reais vendendo {melhor_doce}. O povo gostou, visse?!')