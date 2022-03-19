
class Campo:
    def __init__(self, id, linha_lateral, linha_de_fundo):
        self.id = id
        self.linha_lateral = linha_lateral
        self.linha_de_fundo = linha_de_fundo

    def set_id(self, valor):
        self.id = valor

    def get_id(self):
        return self.id

    def set_linha_lateral(self, valor):
        self.linha_lateral = valor

    def get_linha_lateral(self):
        return self.linha_lateral

    def set_linha_de_fundo(self, valor):
        self.linha_de_fundo = valor

    def get_linha_de_fundo(self):
        return self.linha_de_fundo

    def __str__(self):
        print(self.linha_lateral + " " + self.linha_de_fundo)


