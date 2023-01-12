nome_fogo = input()
dcb_fogo = int(input())
dcbmax_caruaru = int(input())
dcbmax_campina_grande = int(input())

if dcb_fogo <= dcbmax_campina_grande and dcb_fogo <= dcbmax_caruaru:
    print(f'Boa Felipe, o {nome_fogo} será um sucesso em Campina Grande e Caruaru!')
elif dcb_fogo <= dcbmax_campina_grande:
    print(f'Infelizmente em Caruaru não vai rolar, mas em Campina Grande o {nome_fogo} vai ser extouro!')
elif dcb_fogo <= dcbmax_caruaru:
    print(f'Infelizmente em Campina Grande não vai rolar, mas em Caruaru o {nome_fogo} vai ser extouro!')
else:
    print(f'Poxa Felipe, não vai ser dessa vez que {nome_fogo} fará um sucesso pelas festas juninas do Brasil')