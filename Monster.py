from Armas import *
from FunctionsDados import *
class Monster():
    def __init__(self, nome, armadura, vida, deslocamento, forc, dest, con, inte, sab, car, imunidade, xp,arma) -> None:
        super().__init__()
        self.xp = xp
        self.armas = arma
        self.nome = nome
        self.vida = vida
        self.classArmadura = armadura
        self.movimento = deslocamento
        self.forca = forc
        self.destreza = dest
        self.constituicao = con
        self.inteligencia = inte
        self.sabedoria = sab
        self.carisma = car
        self.posAtual = [0, 0]
        self.imunidade = imunidade
        self.acoes = 4

    def atualizaVida(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print(f'{self.nome} morreu!')
        return self.vida

    def desloca(self, mapa: list):
        self.atualizaPosAtual(mapa)
        while True:
            print('''
                       ^
                       |        
                       8
                  <--4 0 6-->
                       2
                       |
                       v
                   ''')

            mov = input('Voce deseja se movimentar para? y x ')
            if not self.movMap(mapa, mov):
                print('Jogada errada... Repita')
            else:
                self.acoes -= 1
                print('Andou')
                break

    def movMap(self, mapa, mov):
        if mov == '6':
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
        elif mov == '8':
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
        elif mov == '4':
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
        elif mov == '2':
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

    def ataca(self, jogador):
        """
        :type jogador: Player
        """
        if self.verificaAlcance(jogador):
            dano = sum(dado(int(self.armas.dano[2]), int(self.armas.dano[0]))) + int(self.armas.dano[4])
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
        print(self.armas.alcance)

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

    def verificaVivo(self):
        if self.vida >= 1:
            return 1
        else:
            return 0

    def verificaAtingirAtaque(self):
        if dado() > self.armas.acerto:
            return True
        return False

