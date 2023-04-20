class mamifero(animal):
    mama = "Possui Glândulas Mamárias"

    def __init__(self, especie, sangue, respiracao, habitat, gestacao, classe, tamanho, cor, dentes, pelos):
        super().__init__(especie, sangue, respiracao, habitat, gestacao, classe, tamanho, cor)
        self._dentes = dentes
        self._pelos = pelos

    @staticmethod
    def mama():
        return mamifero.mama

    @classmethod
    def criar_mamifero(cls, especie, sangue, respiracao, habitat, gestacao, classe, tamanho, cor, dentes, pelos):
        especie = especie.title()
        classe = classe.title()
        if classe != "Mamífero":
            return None
        else:
            return cls(especie=especie, sangue=sangue, respiracao=respiracao, habitat=habitat, gestacao=gestacao, classe=classe)
