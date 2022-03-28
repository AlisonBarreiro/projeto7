from math import pi

if __name__ == '__main__':

    C_D = 0.175  # Coeficiente de arrasto
    rho = 1.2  # Densidade do ar (kg m^-3)
    A = pi * 0.11 ** 2  # Área de seção transversal de futebol (m^2)
    m = 0.43  # Massa da bola (kg)
    g = 9.81  # Aceleração gravitacional (ms^-1)

    F_g = m * g

    speed_conversion = 1000.0 / 3600

    V = 47 * speed_conversion  # Velocidade de chute forte (m/s)
    F_d = 0.5 * C_D * rho * A * V ** 2
    print('Para um chute forte (v = %g), a força gravitacional é %g a \
        a força de arrasto é %g' % (V, F_g, F_d))

    V = 10 * speed_conversion  # Velocidade de chute suave (m/s)
    F_d = 0.5 * C_D * rho * A * V ** 2
    print('Para um chute suave (v = %g), a força gravitacional é %g and \
    a força de arrasto é %g' % (V, F_g, F_d))