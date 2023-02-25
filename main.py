import random

from Jokenpo import Jokenpo
from Papel import Papel
from TIpo import Tipo


def main():
    jokenpo = Jokenpo()

    print("Escolha uma das opções [ 1-PAPEL, 2-TESOURA, 3-PEDRA, LAGARTO-LAGARTO, 5-SPOCK ]\n")
    # jogada = int(input())
    computador = random.randint(1, 5)
    print("O COMPUTADOR escolheu:", computador)

    papel = Papel()
    jokenpo.setAlgoritmo(papel)

    jokenpo.jogar(Tipo.getInstance(computador))


if __name__ == '__main__':
    main()
