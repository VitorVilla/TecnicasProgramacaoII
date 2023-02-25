from typing import Dict

from Algoritmo import Algoritmo
from TIpo import Tipo


class Papel(Algoritmo):
    def executar(self, pTipo: Tipo) -> Dict[str, str]:

        if pTipo == Tipo.PAPEL:
            valor = "Empate. Papel empata com papel!"
        elif pTipo == Tipo.TESOURA:
            valor = "Perdeu! Tesoura corta o papel!"
        elif pTipo == Tipo.PEDRA:
            valor = "Ganhou! Pedra embrulha o papel!"
        elif pTipo == Tipo.LAGARTO:
            valor = "Perdeu! Lagarto come o papel!"
        elif pTipo == Tipo.SPOCK:
            valor = "Ganhou! Papel refuta o Spock!"
        else:
            valor = "Opção inválida!"

        resultado = Algoritmo.KEY + valor
        return resultado
