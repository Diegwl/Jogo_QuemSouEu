class animal():

    def __init__(self, especie, respiracao, habitat, gestacao, classe, tamanho, cor, curiosidade, alimentacao):
        self._especie = especie
        self._respiracao = respiracao
        self._habitat = habitat
        self._gestacao = gestacao
        self._classe = classe
        self._tamanho = tamanho
        self._cor = cor
        self._curiosidade = curiosidade
        self._alimentacao = alimentacao

    @property
    def sangue(self):
        return " "

    @property
    def especie(self):
        return self._especie

    @property
    def respiracao(self):
        return self._respiracao

    @property
    def habitat(self):
        return self._habitat

    @property
    def gestacao(self):
        return self._gestacao

    @property
    def classe(self):
        return self._classe

    @property
    def tamanho(self):
        return self._tamanho

    @property
    def cor(self):
        return self._cor

    @property
    def curiosidade(self):
        return self._curiosidade

    @property
    def alimentacao(self):
        return self._alimentacao
