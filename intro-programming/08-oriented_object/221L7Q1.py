# Definição da classe Sonic, seus métodos e atributos
class Sonic:
    def __init__(self):
        self.anel_coletado = 0
        self.esmeralda_caos = 0
        self.escudo = False
        self.morreu = False
        self.super_sonic = False

    def coletar_aneis(self, qtd_aneis):
        self.anel_coletado += qtd_aneis

    def receber_escudo(self):
        self.escudo = True

    def coletar_esmeralda(self):
        self.esmeralda_caos += 1

    def receber_dano(self):
        if self.escudo:
            self.escudo = False

        elif self.anel_coletado > 0:
            self.anel_coletado = 0

        else:
            self.morreu = True


# Objeto Sonic
sonic = Sonic()

finished = False
while not finished:
    comando = input()

    if comando == 'aneis':
        aux = int(input())
        sonic.coletar_aneis(aux)
        print(f'Sonic esta agora com {sonic.anel_coletado} aneis! Gotta go fast!!!')

    elif comando == 'escudo':
        if sonic.escudo:
            print('Sonic ja esta equipado com uma protecao extra!!!')
        else:
            sonic.receber_escudo()
            print('Sonic esta agora com uma camada a mais de protecao!!! Let\'s go!!!')

    elif comando == 'esmeralda':
        sonic.coletar_esmeralda()
        if sonic.esmeralda_caos > 7:
            print('Sonic ja possui todas as esmeraldas!!!')

        elif sonic.esmeralda_caos != 7:
            print(f'Sonic ainda precisa encontrar mais {7 - sonic.esmeralda_caos} esmeraldas!!!')

        elif sonic.esmeralda_caos == 7:
            print(f'Sonic acabou de encontrar a esmeralda que faltava!!!')

    elif comando == 'dano':
        print(f'Maldito robo do Eggman!!! Este sera seu fim, bigodudo!!!')
        sonic.receber_dano()

    if sonic.morreu:
        print(f'Infelizmente, nosso heroi nao conseguiu correr o bastante para derrotar seu nemesis...')
        finished = True

    elif sonic.esmeralda_caos == 7 and sonic.anel_coletado >= 50:
        print(f'Com o poder das esmeraldas do caos, Super Sonic conseguiu deter os planos malignos do Dr. Robotinik!!!')
        finished = True
