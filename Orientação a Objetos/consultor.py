import datetime
from pessoa import Pessoa

class Consultor(Pessoa):

    def __init__(self, nome, nascimento, endereco, telefone, cpf, email, cnpj, nome_fantasia):
        super().__init__(nome, nascimento, endereco, telefone, cpf, email)
        self.cnpj = cnpj
        self.nome_fantasia = nome_fantasia

    def __str__(self):
        return self.nome
        
    def idade(self):
        hoje = datetime.date.today()
        idade = (hoje.year - self.nascimento.year) + 20 #SOBRESCREVI O MÉTODO DE idade DA CLASSE PESSOA E SOMEI MAIS 20 ANOS!

        if hoje < datetime.date(hoje.year, self.nascimento.month, self.nascimento.day):
            idade -= 1

        return idade