from random import randint
from QuemSouEu.mamifero import mamifero
from QuemSouEu.anfibio import anfibio
from QuemSouEu.jogador import Jogador
from time import sleep


class jogo():
    def __init__(self):
        self.cont = "S"
        self.dicas = list()

    def nome(self):
        nome = input("Digite o seu Nome: ")
        return nome

    def continua(self):
        while True:
            while True:
                opcao = input("Deseja ver o ranking? [S/N]: ").upper()
                if opcao == "S":
                    Jogador.ler_ranking()
                    break
                elif opcao == "N":
                    break
                else:
                    print("Digite S ou N!")
            escolha = input("Deseja jogar novamente? [S/N]: ").upper()
            self.cont = escolha
            if self.cont == "S" or self.cont == "N":
                break
            else:
                print("Digite apenas S ou N!")

    def palavra(self):
        x = randint(1, 2)
        if x == 1:
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
        elif x == 2:
            num = randint(1, 1)
            if num == 1:
                sapo = anfibio("Espécie: Sapo", "Respiração: Pulmonar e Cutânea", "Habitat: Riachos, Lagoas, Igarapés",
                               "Gestação: Bota ovos", "Classe: Anfíbio", "Tamanho: Pequeno", "Cor: Verde",
                               "Curiosidade: Não Lava o Pé", "Alimentação: Come Insetos", "Ordem: Anura")
                return sapo

    def game(self):
        print("--- QUEM SOU EU ---")
        while self.cont == "S":
            nome = self.nome()
            animal1 = self.palavra()
            resposta = animal1.especie
            self.dicas.clear()
            if animal1.classe == "Classe: Mamífero":
                self.dicas = [animal1.respiracao, animal1.habitat, animal1.gestacao, animal1.classe, animal1.tamanho, animal1.cor, animal1.curiosidade, animal1.alimentacao, animal1.dentes, animal1.sangue, animal1.mama]
            elif animal1.classe == "Classe: Anfíbio":
                self.dicas = [animal1.respiracao, animal1.habitat, animal1.gestacao, animal1.classe, animal1.tamanho, animal1.cor, animal1.curiosidade, animal1.alimentacao, animal1.temperatura, animal1.ordem, animal1.pele]
            numeros = []
            jogadas = 0
            pontos = 0

            while jogadas <= 5:
                jogadas += 1
                while True:
                    num = randint(0, len(self.dicas)-1)
                    if num not in numeros:
                        numeros.append(num)
                        break
                print(self.dicas[num])
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
        j1 = Jogador(nome, pontos)
        try:
            j1.adicionar_jogador()
        except:
            print("Algo inesperado ocorreu.")
            sleep(2.5)

"""
    def tabela(self, nome, pontos):
        pontuacoes = pd.read_excel("Pontuacoes.xlsx")
        df = pd.DataFrame(pontuacoes)
        insert = [[nome, pontos]]
        novo = pd.DataFrame(data=insert, columns=['Nome', 'Pontuação'])
        final = pd.concat([df, novo], ignore_index=True, sort=True)

        final.to_excel("Pontuacoes.xlsx")
"""


if __name__ == "__main__":
    j1 = jogo()
    j1.game()
