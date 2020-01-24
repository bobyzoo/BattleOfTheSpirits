from main import *
from pygame_functions import *
import pygame
from telas.menuPrincipal import *
from telas.menuJogar import *
from telas.menuAjuste import *
largura, altura = 1920, 1080
screenSize(largura, altura,fullscreen=True)
setAutoUpdate(False)
nextFrame = clock()
telaAtual = 0

while True:
    if telaAtual == 0:
        telaAtual = menuPrincipal()
    elif telaAtual == 1:
        print('ajust')
        print(telaAtual)
        telaAtual = menuJogar()
    elif telaAtual == 2:
        telaAtual = menuAjuste()


    updateDisplay()
    tick(60)
