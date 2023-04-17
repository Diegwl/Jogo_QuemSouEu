import datetime
from pessoa import Pessoa

class Colaborador(Pessoa):

    def __init__(self, nome, nascimento, endereco, telefone, cpf, email, cargo):
        super().__init__(nome, nascimento, endereco, telefone, cpf, email)
        self.cargo = cargo

    def __str__(self):
        return self.nome
        
    def idade(self):
        hoje = datetime.date.today()
        idade = (hoje.year - self.nascimento.year) + 10 #SOBRESCREVENDO O MÉTODO E SOMANDO MAIS 10 NA IDADE!

        if hoje < datetime.date(hoje.year, self.nascimento.month, self.nascimento.day):
            idade -= 1

        return idade