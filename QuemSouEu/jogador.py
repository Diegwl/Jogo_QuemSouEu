import pandas as pd
import openpyxl
import os


class Jogador:
    def __init__(self, nome: str, pontos: int) -> None:
        self.__nome = nome
        self.__pontos = pontos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, value):
        self.__pontos = value

    def adicionar_jogador(self):
        jogador = pd.read_excel("Pontuacoes.xlsx")
        jogador.loc[len(jogador)] = [self.__nome, self.__pontos]
        jogador.to_excel("Pontuacoes.xlsx", index=False)

    @staticmethod
    def cria_planilha():
        d = {"Nome": [''], "Pontos": ['']}
        dados = pd.DataFrame(data=d)
        dados.to_excel("Pontuacoes.xlsx", index=False)

    @staticmethod
    def ler_ranking():
        planilha = pd.read_excel("Pontuacoes.xlsx")
        ranking = planilha.loc[:, ['Nome', 'Pontos']]
        ranking = ranking.sort_values(by=['Pontos'], ascending=False, na_position='last', ignore_index=True).head(5)
        print(ranking)
