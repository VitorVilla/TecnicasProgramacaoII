from typing import Dict

from Algoritmo import Algoritmo
from TIpo import Tipo


class Jokenpo:
    def __init__(self):
        self.algoritmo = None

    def setAlgoritmo(self, algoritmo: Algoritmo):
        self.algoritmo = algoritmo

    def jogar(self, ptipo: Tipo):
        map_resultado: Dict[str, str] = self.algoritmo.executar(ptipo)
        print(map_resultado)
