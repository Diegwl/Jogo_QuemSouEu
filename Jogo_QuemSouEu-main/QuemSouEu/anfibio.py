from QuemSouEu.animal import animal


class anfibio(animal):
    _pele = "Sua pele é lisa, úmida e macia"

    def __init__(self, especie, respiracao, habitat, gestacao, classe, tamanho, cor, curiosidade, alimentacao, ordem):
        super().__init__(especie, respiracao, habitat, gestacao, classe, tamanho, cor, curiosidade, alimentacao)
        self._ordem = ordem

    @property
    def ordem(self):
        return self._ordem

    @property
    def temperatura(self):
        return "É Ectotérmico (depende de características do meio ambiente para controlar a sua temperatura)"

    @staticmethod
    def pele():
        return anfibio._pele

    @classmethod
    def criar_mamifero(cls, especie, respiracao, habitat, gestacao, classe, tamanho, cor, alimentacao, curiosidade, ordem):
        especie = especie.title()
        classe = classe.title()
        if classe != "Anfíbio":
            return None
        else:
            return cls(especie=especie, respiracao=respiracao, habitat=habitat, gestacao=gestacao, classe=classe,
                       tamanho=tamanho, cor=cor, alimentacao=alimentacao, curiosidade=curiosidade, ordem=ordem)
