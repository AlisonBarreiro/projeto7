class GrandeArea:
    def __init__(self, id, largura, altura, penalidade):
        self.id = id
        self.largura = largura
        self.altura = altura
        self.penalidade = penalidade

    def set_id(self, valor):
        self.id = valor

    def get_id(self):
        return self.id

    def set_largura(self, valor):
        self.largura = valor

    def get_largura(self):
        return self.largura

    def set_altura(self, valor):
        self.altura = valor

    def get_altura(self):
        return self.altura

    def set_penalidade(self, valor):
        self.penalidade = valor

    def get_penalidade(self):
        return self.penalidade