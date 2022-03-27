# Plotting the ball along with the position of the ball
# Run with createPitch([]) to just display the pitch
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from application.util.enums.EnumCampo import EnumCampo
from domain.model.entities.Campo import Campo

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_facecolor('xkcd:green')

    # a função plot funciona assim: [x1, x2] [y1, y2]

    campo = Campo(0)

    # Criar linhas fundo, laterais e Central
    plt.plot([0, 0], [0, campo.get_linha_de_fundo()], color="white")
    plt.plot([0, campo.get_linha_lateral()], [campo.get_linha_de_fundo(), campo.get_linha_de_fundo()], color="white")
    plt.plot([campo.get_linha_lateral(), campo.get_linha_lateral()], [campo.get_linha_de_fundo(), 0], color="white")
    plt.plot([campo.get_linha_lateral(), 0], [0, 0], color="white")
    plt.plot([campo.get_comprimento2(), campo.get_comprimento2()], [0, campo.get_linha_de_fundo()], color="white")

    # Atribuir círculos a variáveis sem preencher o círculo central!
    centreCircle = plt.Circle((campo.get_comprimento2(), campo.get_largura2()), campo.raioCentral, color="white", fill=False)
    centreSpot = plt.Circle((campo.get_comprimento2(), campo.get_largura2()), campo.saidaDiametro, color="white")
    # Desenhe os círculos para o nosso plot
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)

    # Área Penal Esquerda
    plt.plot([campo.larguraGrandeArea, campo.larguraGrandeArea],
             [campo.get_y2comprimentoGrandeArea(), campo.get_y1comprimentoGrandeArea()], color="white")
    plt.plot([0, campo.larguraGrandeArea], [campo.get_y2comprimentoGrandeArea(), campo.get_y2comprimentoGrandeArea()],
             color="white")
    plt.plot([campo.larguraGrandeArea, 0], [campo.get_y1comprimentoGrandeArea(), campo.get_y1comprimentoGrandeArea()],
             color="white")
    # Pequena Area Esquerda
    plt.plot([0, campo.comprimentoPequenaArea], [campo.get_y2larguraPequenaArea(),
                                                 campo.get_y2larguraPequenaArea()], color="white")
    plt.plot([campo.comprimentoPequenaArea, campo.comprimentoPequenaArea],
             [campo.get_y2larguraPequenaArea(), campo.get_y1larguraPequenaArea()], color="white")
    plt.plot([campo.comprimentoPequenaArea, 0.0], [campo.get_y1larguraPequenaArea(),
                                                   campo.get_y1larguraPequenaArea()], color="white")
    # Area Penal  Esquerda
    penalEsquerdo = plt.Circle((campo.penalidade, campo.get_largura2()), 0.4, color="white")
    ax.add_patch(penalEsquerdo)
    # Arco Esquerdo
    arcoEsquerdo = Arc((campo.penalidade, campo.get_largura2()), height=18.32, width=18.32, angle=0, theta1=310,
                       theta2=50, color="white")
    ax.add_patch(arcoEsquerdo)

    # Área Penal Direita
    plt.plot([campo.get_linha_lateral(), campo.get_y1compGraAreaD()],
             [campo.get_y2comprimentoGrandeArea(), campo.get_y2comprimentoGrandeArea()], color="white")
    plt.plot([campo.get_y1compGraAreaD(), campo.get_y1compGraAreaD()],
             [campo.get_y2comprimentoGrandeArea(), campo.get_y1comprimentoGrandeArea()], color="white")
    plt.plot([campo.get_y1compGraAreaD(), campo.get_linha_lateral()],
             [campo.get_y1comprimentoGrandeArea(), campo.get_y1comprimentoGrandeArea()], color="white")
    # Pequena Area Direita
    plt.plot([campo.get_linha_lateral(), campo.get_y1compPeqAreaD()],
             [campo.get_y2larguraPequenaArea(), campo.get_y2larguraPequenaArea()], color="white")
    plt.plot([campo.get_y1compPeqAreaD(), campo.get_y1compPeqAreaD()],
             [campo.get_y2larguraPequenaArea(), campo.get_y1larguraPequenaArea()], color="white")
    plt.plot([campo.get_y1compPeqAreaD(), campo.get_linha_lateral()],
             [campo.get_y1larguraPequenaArea(), campo.get_y1larguraPequenaArea()], color="white")
    # Area Penal  Direita
    penalDireito = plt.Circle((campo.get_penalD(), campo.get_largura2()), 0.4, color="white")
    ax.add_patch(penalDireito)
    # Arco Direito
    arcoDireito = Arc((campo.get_penalD(), campo.get_largura2()), height=18.32, width=18.32, angle=0,
                       theta1=130, theta2=230, color="white")
    ax.add_patch(arcoDireito)

    plt.show()
