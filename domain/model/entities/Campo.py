import math

from application.util.enums.EnumCampo import EnumCampo


class Campo:
    def __init__(self, id):
        self.id = id
        self.linha_lateral = EnumCampo.comprimento.value
        self.linha_de_fundo = EnumCampo.largura.value
        self.raioCentral = EnumCampo.circuloCentralRaio.value
        self.saidaDiametro = EnumCampo.saidaDiametro.value
        self.larguraGrandeArea = EnumCampo.larguraGrandeArea.value
        self.comprimentoGrandeArea = EnumCampo.comprimentoGrandeArea.value

        self.penalidade = EnumCampo.penalidade.value
        self.espessuraDaLinha = EnumCampo.espessuraDaLinha.value

        self.comprimentoPequenaArea = EnumCampo.comprimentoPequenaArea.value

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

    def get_largura2(self):
        return self.linha_de_fundo / 2

    def get_comprimento2(self):
        return self.linha_lateral / 2

    def get_y1comprimentoGrandeArea(self):
        return (self.linha_de_fundo - EnumCampo.comprimentoGrandeArea.value) / 2

    def get_y2comprimentoGrandeArea(self):
        return EnumCampo.comprimentoGrandeArea.value + self.get_y1comprimentoGrandeArea()

    def get_y1larguraPequenaArea(self):
        return (self.linha_de_fundo - EnumCampo.larguraPequenaArea.value) / 2

    def get_y2larguraPequenaArea(self):
        return self.get_y1larguraPequenaArea() + EnumCampo.larguraPequenaArea.value

    def get_y1compGraAreaD(self):
        return self.linha_lateral - EnumCampo.larguraGrandeArea.value

    def get_y1compPeqAreaD(self):
        return self.linha_lateral - EnumCampo.comprimentoPequenaArea.value

    def get_penalD(self):
        return self.linha_lateral - EnumCampo.penalidade.value

    def get_perimetro(self):
        return int(2 * (self.linha_lateral + self.linha_de_fundo))

    def get_area(self):
        return int(self.linha_lateral * self.linha_de_fundo)

    def get_areaDoGol(self):
        return int(EnumCampo.comprimentoTrave.value * EnumCampo.larguraTrave.value)

    def get_areaPorJogador(self):
        return int((self.linha_lateral * self.linha_de_fundo) / 22)

    def get_areaDoCirculoCentral(self):
        return int(math.pi * (math.pow(self.raioCentral, 2)))
