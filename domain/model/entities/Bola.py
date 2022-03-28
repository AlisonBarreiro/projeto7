from application.util.enums.EnumBola import EnumBola


class Bola:
    def __init__(self, id):
        self.id = id
        self.circunferencia = EnumBola.circunferencia.value
        self.peso = EnumBola.peso.value

    def get_pesoEmkg(self):
        return self.peso / 1000
