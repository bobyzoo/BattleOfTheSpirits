from FunctionsDados import *
from ModelRaca.Raca import *
from pygame_functions import *


class Player():
    def __init__(self, raca, nome: str, armas) -> None:
        super().__init__()
        self.armas = armas
        self.equipamento = [armas]
        self.nome = nome
        self.raca = Raca(raca)
        self.vida = 10
        self.movimento = self.raca.deslocamento
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
        self.posAtual = 0
        self.xp= 0
        self.acoes = 4



    def action(self):
        if (self.posAtual[0] + self.armas.alcance >= jogador.posAtual[0] and self.posAtual[1] == jogador.posAtual[1] and
            self.posAtual[0] < jogador.posAtual[0]) or (
                self.posAtual[0] - self.armas.alcance <= jogador.posAtual[0] and self.posAtual[1] == jogador.posAtual[
            1] and self.posAtual[0] > jogador.posAtual[0]) or (
                self.posAtual[0] == jogador.posAtual[0] and self.posAtual[1] + self.armas.alcance >= jogador.posAtual[
            1] and self.posAtual[1] < jogador.posAtual[1]) or (
                self.posAtual[0] == jogador.posAtual[0] and self.posAtual[1] - self.armas.alcance <= jogador.posAtual[
            1] and self.posAtual[1] > jogador.posAtual[1]):
            return True
        return False

    def atualizaVida(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print(f'{self.nome} morreu!')
        return self.vida

    def desloca(self, mapa: list,sentido):
        self.atualizaPosAtual(mapa)
        if not self.movMap(mapa, sentido):
            return 0
        else:
            self.acoes -= 1
            return 1


    def movMap(self, mapa, mov):
        if mov == 4:
            if self.posAtual[0] + 1 < len(mapa):
                if mapa[self.posAtual[0] + 1][self.posAtual[1]] == 0:
                    mapa[self.posAtual[0]][self.posAtual[1]] = 0
                    mapa[self.posAtual[0] + 1][self.posAtual[1]] = self
                    self.atualizaPosAtual(mapa)
                    return True
                else:
                    return False
            else:
                return False
        elif mov == 1:
            if self.posAtual[1] - 1 >= 0:
                if mapa[self.posAtual[0]][self.posAtual[1] - 1] == 0:
                    mapa[self.posAtual[0]][self.posAtual[1]] = 0
                    mapa[self.posAtual[0]][self.posAtual[1] - 1] = self
                    self.atualizaPosAtual(mapa)
                    return True
                else:
                    return False
            else:
                return False
        elif mov == 2:
            if self.posAtual[0] - 1 >= 0:
                if mapa[self.posAtual[0] - 1][self.posAtual[1]] == 0:
                    mapa[self.posAtual[0]][self.posAtual[1]] = 0
                    mapa[self.posAtual[0] - 1][self.posAtual[1]] = self
                    self.atualizaPosAtual(mapa)
                    return True
                else:
                    return False
            else:
                return False
        elif mov == 3:
            if self.posAtual[1] + 1 < len(mapa[self.posAtual[0]]):
                if mapa[self.posAtual[0]][self.posAtual[1] + 1] == 0:
                    mapa[self.posAtual[0]][self.posAtual[1]] = 0
                    mapa[self.posAtual[0]][self.posAtual[1] + 1] = self
                    self.atualizaPosAtual(mapa)
                    return True
                else:
                    return False
            else:
                return False
    def atualizaPosAtual(self, mapa):
        for x in range(len(mapa)):
            for y in range(len(mapa[x])):
                if mapa[x][y] == self:
                    self.posAtual = [x, y]

    def modificaDados(self):
        atr = [self.forca, self.destreza, self.constituicao, self.inteligencia, self.sabedoria, self.carisma]
        for c in range(6):
            dados = dado(6, 4)
            atr[c] = sum(dados) - min(dados) + self.raca.modificadores[c]

    def ataca(self, jogador):
        """
        :type jogador: Player
        """
        if self.verificaAlcance(jogador):
            dano = sum(dado(int(self.armas.dano[2]), int(self.armas.dano[0])))

            print(f'{self.nome} atacou e deu {dano} de dano')

            if jogador.atualizaVida(dano) <= 0:
                return 0
            print(f'{jogador.nome} ficou com {jogador.vida} de vida')
        else:
            print('Sem alcance para ataque')
            return 0

    def verificaAlcance(self, jogador):
        """
        :type jogador: Player
        """
        if (self.posAtual[0] + self.armas.alcance >= jogador.posAtual[0] and self.posAtual[1] == jogador.posAtual[1] and self.posAtual[0] < jogador.posAtual[0]) or (self.posAtual[0] - self.armas.alcance <= jogador.posAtual[0] and self.posAtual[1] == jogador.posAtual[1] and self.posAtual[0] > jogador.posAtual[0]) or (self.posAtual[0] == jogador.posAtual[0] and self.posAtual[1] + self.armas.alcance >= jogador.posAtual[1] and self.posAtual[1] < jogador.posAtual[1]) or (self.posAtual[0] == jogador.posAtual[0] and self.posAtual[1] - self.armas.alcance <= jogador.posAtual[1] and self.posAtual[1] > jogador.posAtual[1]):
            return True
        return False

    def verificaVivo(self):
        if self.vida>=1:
            return 1
        else:
            return 0