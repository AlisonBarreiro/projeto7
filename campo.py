
# Plotting the ball along with the position of the ball
# Run with createPitch([]) to just display the pitch
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from application.util.enums import Enums

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_facecolor('xkcd:green')

    # a função plot funciona assim: [x1, x2] [y1, y2]

    largura = Enums.Campo.largura.value
    largura2 = largura / 2

    comprimento = Enums.Campo.comprimento.value
    comprimento2 = comprimento / 2

    raioCentral = Enums.Campo.circuloCentralRaio.value
    saidaDiametro = Enums.Campo.saidaDiametro.value

    larguraGrandeArea = Enums.Campo.larguraGrandeArea.value
    comprimentoGrandeArea = Enums.Campo.comprimentoGrandeArea.value

    y1comprimentoGrandeArea = (largura-comprimentoGrandeArea) / 2
    y2comprimentoGrandeArea = (comprimentoGrandeArea+y1comprimentoGrandeArea)


    #Criar linhas fundo, laterais e Central
    plt.plot([0, 0], [0, Enums.Campo.largura.value], color="white")
    plt.plot([0, comprimento], [largura, largura], color="white")
    plt.plot([comprimento, comprimento], [largura, 0], color="white")
    plt.plot([comprimento, 0], [0, 0], color="white")
    plt.plot([comprimento2, comprimento2], [0, largura], color="white")

    # Atribuir círculos a variáveis sem preencher o círculo central!
    centreCircle = plt.Circle((comprimento2, largura2), raioCentral, color="white", fill=False)
    centreSpot = plt.Circle((comprimento2, largura2), saidaDiametro, color="white")




    plt.show()