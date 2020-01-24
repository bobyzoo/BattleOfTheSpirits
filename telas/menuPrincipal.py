from pygame_functions import *

telaInicial = loadImage('Map/menuIniciar.png')


def menuPrincipal():
    carregaImagem(telaInicial, (0, 0))
    updateDisplay()
    while True:
        if mousePressed():
            x = mouseX()
            y = mouseY()
            if 720 < x < 1220 and 315 < y < 460:
                print('inicia')
                return 1
            elif 720 < x < 1220 and 640 < y < 790:
                return 2
