from ModelRaca.ModelAnao import *
from ModelRaca.ModelDragonato import *
from ModelRaca.ModelElfo import *
from ModelRaca.ModelGnomo import *
from ModelRaca.ModelHalfling import *
from ModelRaca.ModelHumano import *
from ModelRaca.ModelMeioElfo import *
from ModelRaca.ModelMeioOrc import *
from ModelRaca.ModelTiefling import *


class Raca:
    def __init__(self, raca):
        super().__init__()
        self.nome = str(raca)
        self.modificadores = [0,0,0,0,0,0]
        self.deslocamento = 0
        self.criaRaca(self.nome.lower())

    def criaRaca(self, raca):
        if raca == 'anao':
            self.modificadores = ModelAnao.modificadores
            self.deslocamento = ModelAnao.deslocamento

        elif raca == 'elfo':
            self.modificadores =ModelElfo.modificadores
            self.deslocamento = ModelElfo.deslocamento

        elif raca == 'halfling':
            self.modificadores =ModelHalfling.modificadores
            self.deslocamento = ModelElfo.deslocamento

        elif raca == 'humano':
            self.modificadores =ModelHumano.modificadores
            self.deslocamento = ModelElfo.deslocamento

        elif raca == 'dragonato':
            self.modificadores =ModelDragonato.modificadores
            self.deslocamento = ModelDragonato.deslocamento

        elif raca == 'gnomo':
            self.modificadores =ModelGnomo.modificadores
            self.deslocamento = ModelGnomo.deslocamento

        elif raca == 'meioelfo':
            self.modificadores =ModelMeioElfo.modificadores
            self.deslocamento = ModelMeioElfo.deslocamento
        elif raca == 'meioorc':
            self.modificadores =ModelMeioOrc.modificadores
            self.deslocamento = ModelMeioOrc.deslocamento
        elif raca == 'tieling':
            self.modificadores =ModelTiefling.modificadores
            self.deslocamento = ModelTiefling.deslocamento
