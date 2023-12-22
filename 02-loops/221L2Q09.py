num_conv = int(input())

acertos = 0

for i in range(num_conv):
    op = input()

    if op == 'DEC':
        number = input()
        palpite = input()
        # Conversor Bin to Dec
        ctrl = 0
        dec_number = 0
        for j in range(len(number), 0, -1):
            dec_number += (2 ** ctrl) * int(number[j - 1])
            ctrl += 1

        if int(palpite) != dec_number:
            print(f'Palpite Incorreto, o valor {number} = {dec_number}')

        else:
            acertos += 1

    elif op == 'BIN':
        number = int(input())
        num = number
        palpite = input()
        # Conversor Dec to Bin
        bin_number = ''
        while True:
            if number == 0:
                bin_number = '0'
                break
            elif number == 1:
                bin_number = '1'
                break
            else:
                bin_number += str(number % 2)
                number = number // 2
                if number == 1:
                    bin_number += '1'
                    break

        if palpite != bin_number[::-1]:
            print(f'Palpite Incorreto, o valor {num} = {bin_number[::-1]}')

        else:
            acertos += 1
else:
    if acertos > num_conv * 0.5:
        print('Bazinga! Quem realizou esses cálculos foi o computador??')
    else:
        print('Parece que realizar conversões em binário não é o seu forte')
