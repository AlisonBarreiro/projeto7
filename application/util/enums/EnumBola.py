from enum import Enum


class EnumBola(Enum):
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
