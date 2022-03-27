import math

from application.util.enums import Enums


def perimetro(c, l):
    return int(2 * (c + l))


def area(c, l):
    return int(c * l)


def areaPorJogador(c, l):
    return int((c * l) / 22)


def areaDoCirculoCentral(raio):
    return int(3.14 * (math.pow(raio, 2)))


if __name__ == '__main__':
    print("Perímetro " +
          str(perimetro(Enums.Campo.comprimento.value, Enums.Campo.largura.value)))
    print("O campo de futebol possui " +
          str(area(Enums.Campo.comprimento.value, Enums.Campo.largura.value)) + "m2")
    print("Cada jogador pode ocupar uma área de " +
          str(areaPorJogador(Enums.Campo.comprimento.value, Enums.Campo.largura.value)) + "m2")
    print("Area do Gol " +
          str(area(Enums.Campo.comprimentoTrave.value,
                   Enums.Campo.larguraTrave.value)) + "m2, ou seja, a área que o goleiro tem que defender.")
    print("Area do círculo central " +
          str(areaDoCirculoCentral(Enums.Campo.circuloCentralRaio.value)) + "m2")
