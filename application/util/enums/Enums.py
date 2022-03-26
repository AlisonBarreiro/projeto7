from enum import Enum


class Campo(Enum):
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


class Bola(Enum):
    # circunferência em metros
    circunferencia = 0.69
    circunferênciaMin = 0.68
    circunferênciaMax = 0.70
    # peso em gramas
    peso = 430
    pesoMin = 410
    pesoMax = 450
    # pressão atmosferas (600 – 1100 g/cm2) ao nível do mar
    psi = 0.6
    psiMin = 0.6
    psiMax = 1.1

    ####### Padrão aprovado pela FIFA  ###########
    # Teste de rebote uniforme <= 10cm
    # Perda de pressão <= 20%
    # Absorção de água <= 10%  de aumento de peso
    # Diâmetro  1,5% de diferença


print(Campo.comprimentoCampo.value)
