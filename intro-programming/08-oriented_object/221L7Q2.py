# Classe que criará os participantes e modificará seus estados
class Jogador:
    # Dicionário com todos os personagens criados
    personagens_criados = dict()

    def __init__(self, nome, poder, subclasse):
        self.nome = nome
        self.poder = int(poder)
        self.subclasse = subclasse
        self.adversarios_vencidos = list()

    def modificar_atributos(self, poder, subclasse):
        self.poder = int(poder)
        self.subclasse = subclasse

    def adversario_vencido(self, adversario):
        self.adversarios_vencidos.append(adversario)

    def aumentar_poder(self):
        if self.subclasse == 'Saiyajin':
            self.poder += self.poder * 0.1

        elif self.subclasse == 'Hibrido-Saiyajin':
            self.poder += self.poder * 0.2


# Classe que cuidará do torneio
class Torneio:
    def __init__(self):
        # Dicionário com todos os participantes adicionados no torneio
        self.participantes_torneio = dict()
        self.vencedor = None

    def adicionar_torneio(self, participante):
        self.participantes_torneio.update({participante.nome: participante})

    def remover_torneio(self, participante):
        self.participantes_torneio.pop(participante)

    def media_poderes(self):
        media = 0
        for participante in self.participantes_torneio.keys():
            media += int(self.participantes_torneio[participante].poder)
        media /= self.contar_jogadores()

        return media

    def contar_jogadores(self):
        count = 0
        for _ in self.participantes_torneio:
            count += 1

        return count

    def ordem_alfabetica(self):
        dict_sorted = dict()
        for key in sorted(self.participantes_torneio):
            dict_sorted.update({key: self.participantes_torneio[key]})

        else:
            self.participantes_torneio = dict_sorted

    def separar_grupos(self):
        # Separando os grupos
        etapas = [list(), list()]
        count = 0
        for participante in self.participantes_torneio:
            if count <= 3:
                etapas[0].append(participante)

            else:
                etapas[1].append(participante)

            count += 1

        else:

            return etapas

    def batalhar(self, jogador1, jogador2):
        if self.participantes_torneio.get(jogador1).poder == self.participantes_torneio.get(jogador2).poder:
            if self.participantes_torneio.get(jogador1).nome > self.participantes_torneio.get(jogador2).nome:
                return {'winner': jogador1, 'loser': jogador2}

            else:
                return {'winner': jogador2, 'loser': jogador1}

        elif self.participantes_torneio.get(jogador1).poder > self.participantes_torneio.get(jogador2).poder:
            return {'winner': jogador1, 'loser': jogador2}

        else:
            return {'winner': jogador2, 'loser': jogador1}


torneio = Torneio()

finished = False
while not finished:
    jogador = input().split()
    acao = jogador.pop(0)

    if acao == 'ADD':
        jogador = {'nome': jogador[0], 'poder': jogador[1], 'subclasse': jogador[2]}

        # Criando personagem
        if jogador['nome'] not in Jogador.personagens_criados:
            personagem = Jogador(jogador['nome'], jogador['poder'], jogador['subclasse'])
            Jogador.personagens_criados.update({personagem.nome: personagem})

        # Modifica personagem já existente
        else:
            Jogador.personagens_criados.get(jogador['nome']).modificar_atributos(jogador['poder'], jogador['subclasse'])
            personagem = Jogador.personagens_criados.get(jogador['nome'])

        # Adicionando ao torneio
        if personagem.nome not in torneio.participantes_torneio:
            if not torneio.participantes_torneio:
                print(f'{personagem.nome} foi o primeiro a entrar no torneio e aguarda os outros competidores.')

            elif torneio.media_poderes() < personagem.poder:
                print(f'Adversários se preparem!! {personagem.nome} está no Torneio e é um dos maiores favoritos'
                      f' a conquistar.')

            else:
                print(f'{personagem.nome} acabou de entrar no torneio, mas acho que não vai muito longe.')

            torneio.adicionar_torneio(personagem)

        else:
            print(f'{personagem.nome} já está no torneio e não pode ser adicionado')

    else:
        jogador = {'nome': jogador[0]}

        # Deletando participante
        if jogador['nome'] not in torneio.participantes_torneio:
            print(f'{jogador["nome"]} ainda não está no Torneio para ser removido.')

        else:
            print(f'Infelizmente {jogador["nome"]} saiu do Torneio.')
            torneio.remover_torneio(jogador['nome'])

    if torneio.contar_jogadores() == 8:
        finished = True

# Organizando participantes em ordem alfabética
torneio.ordem_alfabetica()

# Separando os grupos
quartas_finais = torneio.separar_grupos()
semifinais = [list(), list()]
final = list()

print()

print('### QUARTAS DE FINAL ###')
for i in range(4):
    resultado = torneio.batalhar(quartas_finais[0][0], quartas_finais[1][0])

    print(f'{resultado["winner"]} numa dura batalha vence {resultado["loser"]}.')

    Jogador.personagens_criados.get(resultado['winner']).adversario_vencido(resultado['loser'])
    Jogador.personagens_criados.get(resultado['winner']).aumentar_poder()

    if i < 2:
        semifinais[0].append(resultado['winner'])

    else:
        semifinais[1].append(resultado['winner'])

    quartas_finais[0].pop(0)
    quartas_finais[1].pop(0)

print()

print('### SEMI-FINAL ###')
for i in range(2):
    resultado = torneio.batalhar(semifinais[0][0], semifinais[1][0])

    print(f'{resultado["winner"]} numa dura batalha vence {resultado["loser"]}.')

    Jogador.personagens_criados.get(resultado['winner']).adversario_vencido(resultado['loser'])
    Jogador.personagens_criados.get(resultado['winner']).aumentar_poder()

    final.append(resultado['winner'])
    semifinais[0].pop(0)
    semifinais[1].pop(0)

print()

print('### FINAL ###')
resultado = torneio.batalhar(final[0], final[1])
torneio.vencedor = resultado['winner']
print(f'{resultado["winner"]} numa dura batalha vence {resultado["loser"]}.')
Jogador.personagens_criados.get(resultado['winner']).adversario_vencido(resultado['loser'])
Jogador.personagens_criados.get(resultado['winner']).aumentar_poder()

print()

print(f'{torneio.vencedor}, venceu o Torneio do Poder passando pelos adversários '
      f'{", ".join(Jogador.personagens_criados[torneio.vencedor].adversarios_vencidos)} '
      f'com um poder de luta incrível de {Jogador.personagens_criados[torneio.vencedor].poder:.0f}.')
