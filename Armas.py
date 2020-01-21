class Armas:
    def __init__(self, tipo, nome, preco, dano, peso, propriedades,acerto =1) -> None:
        super().__init__()
        if tipo == 'coc':
            self.alcance = 3
        elif tipo == 'armasimples':
            self.alcance = 1
        elif tipo == 'marcialcoc':
            self.alcance = 2
        else:
            self.alcance = 1
        self.dano = dano
        self.acerto = acerto
        self.preco = preco
        self.peso = peso
        self.nome = nome
        self.propriedades = propriedades

