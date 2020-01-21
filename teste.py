from Player import *
from listaArmas import *
from Map.Map import *
from Monster import *


def gameInit(jogadores: list, Inimigos=[]):
    """

    :type Inimigos: list
    """
    locaisIniciaisJ = []
    locaisIniciaisI = []

    for coluna in range(len(Map1)):
        for item in range(len(Map1[coluna])):
            if Map1[coluna][item] == 5:
                locaisIniciaisJ.append([coluna, item])
            elif Map1[coluna][item] == 6:
                locaisIniciaisI.append([coluna, item])
    if len(locaisIniciaisJ) == len(jogadores):
        for c in range(len(jogadores)):
            y, x = locaisIniciaisJ[c]
            Map1[y][x] = jogadores[c]
    if len(locaisIniciaisI) == len(Inimigos):
        for c in range(len(Inimigos)):
            y, x = locaisIniciaisI[c]
            Map1[y][x] = Inimigos[c]



def jogada(jogador: Player, listaInimigos: list, mapa):
    while jogador.acoes > 0:
        print(mapa)
        print(f'''
            {jogador.acoes} Ações disponiveis
            [0] - Passa a vez
            [1] - descolamento
            [2] - ataque
            ''')
        x = input('')
        if x == '0':
            print('Passou a vez')
            break
        elif x == '1':
            jogador.desloca(mapa)
        elif x == '2':
            jogador.atualizaPosAtual(mapa)
            inimigo: Player
            for inimigo in listaInimigos:
                inimigo.atualizaPosAtual(mapa)
                print(inimigo.nome)
            x = input('Quem?').lower()
            for inimigo in listaInimigos:
                if x == inimigo.nome.lower():
                    if jogador.ataca(inimigo) != 0:
                        jogador.acoes -= 1
                    else:
                        if inimigo.verificaVivo() == 0:
                            return 0
    jogador.acoes = 4


jogador1 = Player('Humano', 'Gabriel', armas['Machado'])
jogador2 = Monster('Esqueleto',13,13,3,10,16,18,4,7,2,'veneno',50,armas['espadaCurta'])
print(Map1)
gameInit([jogador1],[jogador2])
print(Map1)
while True:
    if jogada(jogador1, [jogador2], Map1) == 0:
        break
    print('Proxima rodada')
    if jogada(jogador2, [jogador1], Map1) == 0:
        break
