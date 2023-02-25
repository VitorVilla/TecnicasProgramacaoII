from enum import Enum


class Tipo(Enum):
    PAPEL = 1
    TESOURA = 2
    PEDRA = 3
    LAGARTO = 4
    SPOCK = 5

    def __init__(self, pId):
        self.id = pId

    def getId(self):
        return self.id

    @staticmethod
    def getInstance(pId):
        for t in Tipo:
            if t.getId() == pId:
                return t
        raise RuntimeError(f"Tipo inválido. Id: {pId}")
