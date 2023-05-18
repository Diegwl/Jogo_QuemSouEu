import datetime

class Pessoa(object):

    def __init__(self, nome, nascimento, endereco, telefone, cpf, email):
        self.__contador = 0
        self.nome = nome
        self.nascimento = nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.cpf = cpf
        self.email = email

    def __str__(self):
        return self.nome
        
    def obter_contador(self):
        return self.__contador
        
    def idade(self):
        self.__contador += 1
        hoje = datetime.date.today()
        idade = hoje.year - self.nascimento.year

        if hoje < datetime.date(hoje.year, self.nascimento.month, self.nascimento.day):
            idade -= 1

        return idade
        
    def validar_cpf(self):
        valido = False
        #chamar serviço do Serasa para validar o CPF
        #valido = serasa.validarCPF(self.cpf)

        return valido