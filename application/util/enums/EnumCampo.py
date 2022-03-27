from enum import Enum


class EnumCampo(Enum):
    largura = 68
    larguraMin = 45
    larguraMax = 90

    # Dimensões para jogos internacionais
    larguraInterMin = 64
    larguraInterMax = 75

    comprimento = 105
    comprimentoMin = 90
    comprimentoMax = 120

    # Dimensões para jogos internacionais
    comprimentoInterMin = 100
    comprimentoInterMax = 110

    larguraGrandeArea = 16.5
    comprimentoGrandeArea = 42.32

    larguraPequenaArea = 18.32
    comprimentoPequenaArea = 5.5

    penalidade = 11
    meiaLuaRaio = 9.15
    recuoEscanteio = 9.15
    circuloCentralRaio = 9.15
    arcoDeEscanteio = 1
    espessuraDaLinha = 0.12
    larguraTrave = 2.44
    comprimentoTrave = 7.32
    profundidadeTrave = 2
    profundidadeRede = 1.5
    espessuraDaTrave = 0.12
    saidaDiametro = 0.24

    bandeiraAltura = 1.5
    bandeiraAlturaMeio = 1