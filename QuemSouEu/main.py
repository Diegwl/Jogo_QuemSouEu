from random import randint
from QuemSouEu.mamifero import mamifero
import pandas as pd
import openpyxl

class jogo():
    def __init__(self):
        self.cont = "S"

    def nome(self):
        nome = input("Digite o seu Nome: ")
        return nome

    def continua(self):
        while True:
            escolha = input("Deseja jogar novamente? [S/N]: ").upper()
            self.cont = escolha
            if self.cont == "S" or self.cont == "N":
                break
            else:
                print("Digite apenas S ou N!")

    def palavra(self):
        num = randint(1, 2)
        if num == 1:
            leao = mamifero("Espécie: Leão", "Respiração: Pulmonar", "Habitat: Savana", "Gestação: Ulterina",
                            "Classe: Mamífero", "Tamanho: Médio", "Cor: Amarelo", "Curiosidade: É o Rei da selva",
                            "Alimentação: Carnívoro", "Dentes: Afiados")
            return leao
        if num == 2:
            ornitorrinco = mamifero("Espécie: Ornitorrinco", "Respiração: Pulmonar", "Habitat: Rios, Lagoas",
                                    "Gestação: Bota ovos",
                                    "Classe: Mamífero", "Tamanho: Pequeno", "Cor: Marrom",
                                    "Curiosidade: Esse animal é um agente secreto em um desenho famoso",
                                    "Alimentação: Herbívoro", "Possui Bico")
            return ornitorrinco

    def game(self):
        print("--- QUEM SOU EU ---")
        while self.cont == "S":
            nome = self.nome()
            animal = self.palavra()
            resposta = animal.especie
            dicas = [animal.respiracao, animal.habitat, animal.gestacao, animal.classe, animal.tamanho, animal.cor,
                     animal.curiosidade, animal.alimentacao, animal.dentes, animal.sangue]
            numeros = []
            jogadas = 0
            pontos = 0

            while jogadas <= 5:
                jogadas += 1
                while True:
                    num = randint(0, len(dicas)-1)
                    if num not in numeros:
                        numeros.append(num)
                        break
                print(dicas[num])
                print("-" * 30)
                palpite = "Espécie: " + input(f"Digite seu {jogadas}º palpite: ").title()
                print("-" * 30)
                if palpite == resposta:
                    pontos = (6 - jogadas) * 10
                    print(f"Parabéns, você acertou em {jogadas} jogadas e ganhou {pontos} pontos")
                    print("-" * 30)
                    break
                elif palpite != resposta and jogadas == 5:
                    print(f"Sinto muito, você perdeu\nA resposta era: {resposta}")
                    print("-" * 30)
                    break
                else:
                    print("Você errou, tente novamente")
                    print("-"*30)
            self.tabela(nome, pontos)
            self.continua()

    def tabela(self, nome, pontos):
        pontuacoes = pd.read_excel("Pontuacoes.xlsx")
        df = pd.DataFrame(pontuacoes)
        insert = [[nome, pontos]]
        novo = pd.DataFrame(data=insert, columns=['Nome', 'Pontuação'])
        print(novo)
        final = pd.concat([df, novo], ignore_index=True, sort=True)

        final.to_excel("Pontuacoes.xlsx")


if __name__ == "__main__":
    j1 = jogo()
    j1.game()
