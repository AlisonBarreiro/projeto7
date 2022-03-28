# coeficiente de arrasto
# O coeficiente de arrasto Cd é igual ao arrasto D dividido pela quantidade:
# densidade r vezes metade da velocidade V ao quadrado vezes a área de referência A .
# cd = D / (A * .5 * r * V ^ 2)
from math import pi

import numpy as np
from matplotlib import pyplot as plt

from domain.model.entities.Bola import Bola

if __name__ == '__main__':
    bola = Bola(0)


    # Variação
    t = 12  # s
    v = 24  # m/s
    m = bola.get_pesoEmkg()  # kg
    g = 9.81  # m/s
    rho = 1.2
    v_term = 18

    area = pi * (0.019 / 2) ** 2

    C_d = (2 * 0.0025 * g /
           (rho * area * v_term ** 2))

    print(C_d)

    a, b = 0.17, 0.18
    c = np.linspace(a, b, 20)
    f = g * m / c * (1 - np.exp(-c / m * t)) - v

    plt.plot(c, f, 'k--o')
    plt.xlabel('c')
    plt.ylabel('f(c)')
    plt.grid(True)

    plt.show()
