from pygame_functions import *

telaAjuste = loadImage('Map/placaAjuste.png')
def menuJogar():
    drawRect(0, 0, 1920, 1080, (255, 255, 255))
    carregaImagem(telaAjuste, (0, 0))
    updateDisplay()
    while True:
        if mousePressed():
            x = mouseX()
            y = mouseY()
            if 720 < x < 1220 and 315 < y < 460:
                print('iniciar')
                return 1
            elif 720 < x < 1220 and 640 < y < 790:
                print('ajuste')

