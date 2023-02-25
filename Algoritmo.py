from typing import Dict
from abc import ABC, abstractmethod

from TIpo import Tipo


class Algoritmo(ABC):
    KEY = "resultado: "

    def __init__(self):
        self.valor = ""
        self.resultado = {}

    @abstractmethod
    def executar(self, pTipo: Tipo) -> Dict[str, str]:
        pass
