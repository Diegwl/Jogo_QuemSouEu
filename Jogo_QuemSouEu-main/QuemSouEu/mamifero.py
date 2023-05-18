from QuemSouEu.animal import animal


class mamifero(animal):
    _mama = "Possui Glândulas Mamárias"

    def __init__(self, especie, respiracao, habitat, gestacao, classe, tamanho, cor, curiosidade, alimentacao, dentes):
        super().__init__(especie, respiracao, habitat, gestacao, classe, tamanho, cor, curiosidade, alimentacao)
        self._dentes = dentes

    @property
    def dentes(self):
        return self._dentes

    @property
    def sangue(self):
        return "Possui Sangue Quente"

    @staticmethod
    def mama():
        return mamifero._mama

    @classmethod
    def criar_mamifero(cls, especie, respiracao, habitat, gestacao, classe, tamanho, cor, dentes, alimentacao, curiosidade):
        especie = especie.title()
        classe = classe.title()
        if classe != "Mamífero":
            return None
        else:
            return cls(especie=especie, respiracao=respiracao, habitat=habitat, gestacao=gestacao, classe=classe,
                       tamanho=tamanho, cor=cor, dentes=dentes, alimentacao=alimentacao, curiosidade=curiosidade)
