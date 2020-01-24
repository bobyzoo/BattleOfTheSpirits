from pygame_functions import *
from Map.Map import *
import pygame

screenSize(640, 850,fullscreen=True)
setAutoUpdate(False)

#
# # testSprite = makeSprite("image/spriteCapoerista.png",16)  # We create the sprite with the default image
#
# moveSprite(testSprite, 800/2, 800/2)
# showSprite(testSprite)

nextFrame = clock()
chao = loadImage("Map/chao1.png")
frame = 0

from Player import *
from listaArmas import *
from Map.Map import *
from Monster import *
MovimentarText = makeLabel("MOVIMENTAR", 35, 55, 670, "white")
AtaqueText = makeLabel("ATAQUE", 40, 90, 740, "white")
PassaVezText = makeLabel("Passa vez", 40, 350, 670, "white")
setar = loadImage('Map/direcionalSeta.png')
def limpaMenu():
    drawRect(0, 640, 640, 300, (60, 60, 60))

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
            print(type(jogadores[c]))
    if len(locaisIniciaisI) == len(Inimigos):
        for c in range(len(Inimigos)):
            y, x = locaisIniciaisI[c]
            Map1[y][x] = Inimigos[c]


def printMenuAcoes(MovimentarText,AtaqueText,PassaVezText):
    limpaMenu()
    drawRect(50, 660, 250, 60, (80, 80, 80))
    drawRect(50, 730, 250, 60, (80, 80, 80))
    drawRect(75 + 250, 660, 250, 60, (80, 80, 80))
    drawRect(75 + 250, 730, 250, 60, (80, 80, 80))
    showLabel(MovimentarText)
    showLabel(AtaqueText)
    showLabel(PassaVezText)
    updateDisplay()
    time.sleep(0.5)
    while True:
        if mousePressed():
            x = mouseX()
            y = mouseY()
            if 50 < x < 300 and 660 < y < 715:
                hideLabel(MovimentarText)
                hideLabel(AtaqueText)
                hideLabel(PassaVezText)
                return 1
            elif 50 < x < 300 and 730 < y < 790:
                hideLabel(MovimentarText)
                hideLabel(AtaqueText)
                hideLabel(PassaVezText)
                return 2
            elif 330 < x < 570 and 660 < y < 715:
                hideLabel(MovimentarText)
                hideLabel(AtaqueText)
                hideLabel(PassaVezText)
                return 0
            else:
                return 3
def ataque(jogador,mapa,listaInimigos):
    jogador.atualizaPosAtual(mapa)
    inimigo: Player
    for inimigo in listaInimigos:
        inimigo.atualizaPosAtual(mapa)
        print(inimigo.nome)
    x = input('Quem?').lower()
    for inimigo in listaInimigos:
        if x == inimigo.nome.lower():
            if jogador.ataca(inimigo) != 0:
                acaoAtaqueImg(loadImage("Map/corte.png"), inimigo.posAtual)
                jogador.acoes -= 1
            else:
                if inimigo.verificaVivo() == 0:
                    acaoAtaqueImg(loadImage("Map/corte.png"), inimigo.posAtual)
                    updateDisplay()
                    tick(120)
                    return 0
    updateDisplay()
    tick(120)

def quadradosPossiveis(jogador,mapa):
    pedraSelecionado = loadImage("Map/selectRed.png")
    jogador.atualizaPosAtual(mapa)
    if jogador.posAtual[0] + 1 < len(mapa):
        if mapa[jogador.posAtual[0] + 1][jogador.posAtual[1]] == 0:
            mapa[jogador.posAtual[0] + 1][jogador.posAtual[1]]
            carregaImagem(pedraSelecionado, ((jogador.posAtual[0] + 1) * 64, jogador.posAtual[1] * 64))
    if jogador.posAtual[1] - 1 >= 0:
        if mapa[jogador.posAtual[0]][jogador.posAtual[1] - 1] == 0:
            carregaImagem(pedraSelecionado, (jogador.posAtual[0]*64, (jogador.posAtual[1] - 1) * 64))
            pass
    if jogador.posAtual[0] - 1 >= 0:
        if mapa[jogador.posAtual[0] - 1][jogador.posAtual[1]] == 0:
            carregaImagem(pedraSelecionado, ((jogador.posAtual[0] - 1) * 64, jogador.posAtual[1] * 64))
            pass
    if jogador.posAtual[1] + 1 < len(mapa[jogador.posAtual[0]]):
        if mapa[jogador.posAtual[0]][jogador.posAtual[1] + 1] == 0:
            carregaImagem(pedraSelecionado, (jogador.posAtual[0]*64, (jogador.posAtual[1] + 1) * 64))
            pass
    updateDisplay()


    time.sleep(1)

def printMenuDeslocamento(mapa,jogador):
    limpaMenu()
    setad = loadImage('Map/direcionalSeta.png')
    carregaImagem(setad, (180, 625))
    updateDisplay()
    quadradosPossiveis(jogador,mapa)
    while True:
        if mousePressed():
            x = mouseX()
            y = mouseY()
            print(x,y)
            if x > 285 and x < 328 and y > 658 and y < 714:
                return 1
            elif x > 218 and x < 280 and y > 722 and y < 766:
                return 2
            elif x > 283 and x < 331 and y > 773 and y < 831:
                return 3
            elif x > 335 and x < 390 and y > 718 and y < 770:
                return 4

def jogada(jogador, listaInimigos: list, mapa):
    while jogador.acoes > 0:
        carregaMapa(mapa)
        updateDisplay()
        x = printMenuAcoes(MovimentarText,AtaqueText,PassaVezText)

        if x == 0:
            print('Passou a vez')
            break
        elif x == 1:
            mov = printMenuDeslocamento(mapa,jogador)
            while True:
                if jogador.desloca(mapa, mov):
                   break
                mov = printMenuDeslocamento()
            updateDisplay()
            tick(120)
        elif x == 2:
           ataque(jogador,mapa,listaInimigos)
    updateDisplay()
    tick(120)
    jogador.acoes = 4


def jogo():
    jogador1 = Player('Humano', 'Gabriel', armas['Machado'])
    jogador2 = Monster('Esqueleto', 13, 13, 3, 10, 16, 18, 4, 7, 2, 'veneno', 50, armas['espadaCurta'])
    print(Map1)
    gameInit([jogador1], [jogador2])
    print(Map1)
    updateDisplay()
    tick(120)

    while True:

        if jogada(jogador1, [jogador2], Map1) == 0:
            break
        print('Proxima rodada')
        if jogada(jogador2, [jogador1], Map1) == 0:
            break

        updateDisplay()
        tick(120)

    endWait()
