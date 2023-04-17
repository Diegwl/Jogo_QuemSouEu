import datetime
from pessoa import *
from colaborador import *
from consultor import *

if __name__ == "__main__":
    pessoa = Pessoa(
        nome = "Cleber",
        nascimento = datetime.date(2000, 1, 1), # year, month, day
        endereco = "Rua Xxxxxxx, Campinas - SP",
        telefone = "+55 19 9XXXX-XXXX",
        cpf = "123456789-10",
        email = "cleber.augusto@br.bosch.com"
    )

    print(" ")
    #print(str(pessoa))
    print("******* Pessoa ******************************")
    print("Contador: ", pessoa.obter_contador())
    print("Nome: ", pessoa.nome)
    print("Nascimento: ", pessoa.nascimento)
    print("Endereço: ", pessoa.endereco)
    print("Telefone: ", pessoa.telefone)
    print("CPF: ", pessoa.cpf)
    print("Email: ", pessoa.email)
    print("Idade: ", pessoa.idade())
    print("Contador: ", pessoa.obter_contador())
    print("*********************************************")
    print(" ")



    colaborador = Colaborador(
        nome = "Fulano",
        nascimento = datetime.date(2000, 1, 1), # year, month, day
        endereco = "Rua Xxxxxxx, Hortolândia - SP",
        telefone = "+55 19 9XXXX-XXXX",
        cpf = "123456788-10",
        email = "fulano@example.com",
        cargo = "Engenheiro de sistemas"
    )

    print(" ")
    print("******* colaborador ******************************")
    print("Nome: ", colaborador.nome)
    print("Nascimento: ", colaborador.nascimento)
    print("Endereço: ", colaborador.endereco)
    print("Telefone: ", colaborador.telefone)
    print("CPF: ", colaborador.cpf)
    print("Email: ", colaborador.email)
    print("Cargo: ", colaborador.cargo)
    print("Idade: ", colaborador.idade())
    print("*********************************************")
    print(" ")



    consultor = Consultor(
        nome = "Beltrana",
        nascimento = datetime.date(2000, 1, 1), # year, month, day
        endereco = "Rua Xxxxxxx, Sumaré - SP",
        telefone = "+55 19 9XXXX-XXXX",
        cpf = "123456789-11",
        email = "beltrana@example.com",
        cnpj = "000.XXX.XXX.XXX-00",
        nome_fantasia = "Desenvolvimento e Arquitetura de Software"
    )

    print(" ")
    print("******* consultor ******************************")
    print("Nome: ", consultor.nome)
    print("Nascimento: ", consultor.nascimento)
    print("Endereço: ", consultor.endereco)
    print("Telefone: ", consultor.telefone)
    print("CPF: ", consultor.cpf)
    print("Email: ", consultor.email)
    print("CNPJ: ", consultor.cnpj)
    print("Nome fantasia: ", consultor.nome_fantasia)
    print("Idade: ", consultor.idade())
    print("*********************************************")
    print(" ")




