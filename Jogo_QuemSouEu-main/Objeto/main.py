class Conta:

    CODIGO_BANCO = "001"

    def __init__(self, numero: int, titular: str, saldo: float, limite: float = 1000.0):
        """
        Contrutor do objeto Conta
        :param numero: int
        :param titular: str
        :param saldo: float
        :param limite: float
        :return: Conta
        """
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        # self.__codigo_banco = "001"
        print("OBJETO INSTANCIADO", self)

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigo_banco2():
        return Conta.CODIGO_BANCO

    # @property
    # def codigo(self):
    #    return self.__codigo_banco

    @classmethod
    def criar_conta(cls, nmr, ttlr, sld, lmt):
        ttlr = ttlr.title()
        if sld > 0:
            return cls(numero=nmr, saldo=sld, titular=ttlr, limite=lmt)
        else:
            return None

    def extrato(self):
        print("TITULAR:", self.__titular, "SALDO:", self.__saldo)

    def __pode_sacar(self, valor_saque: float):  # Abstração
        if valor_saque > self.__saldo:
            return False
        return True

    def sacar(self, valor: float):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print(f"VALOR SACADO: {valor} | NOVO EXTRATO: {self.__saldo}")
        else:
            print("O VALOR PASSOU DOS LIMITES")

    def depositar(self, valor: float):
        self.__saldo += valor

    def tranferir(self, valor: float, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print(f"TRANSFERÊNCIA NO VALOR DE R${valor} DE '{self.__titular}' PARA '{destino.__titular}'")

    @property
    def limite(self):  # Abstração
        return self.__limite

    @limite.setter
    def limite(self, valor):
        if valor > 1.1 * self.__limite:
            print("INFELIZMENTE O LIMITE ESTÁ ACIMA DE 10%")
            print("LIMITE NÃO ALTERADO:", self.limite)
        else:
            self.__limite = valor
            print("LIMITE ALTERADO COM SUCESSO")
            print("NOVO VALOR:", self.limite)


class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property  # Getter -> ele é acessado por uma funçãe e não um atributo.
    def nome(self):
        print("CHAMANDO GETTER NOME")
        return self.__nome.title()

    @nome.setter  # Setter -> altera um atributo do meu objeto.
    def nome(self, nome):
        print("CHAMANDO SETTER NOME")
        self.__nome = nome


if __name__ == '__main__':
    conta1 = Conta(1, "Fulano", 1000.0)
    print("OBJETO CRIADO", conta1)
    conta2 = Conta(2, "Beltrano", 500.0)
    print("OBJETO CRIADO", vars(conta2))
    conta3 = Conta(1, "Ciclano", 1500.0, 2000.0)
    print("OBJETO CRIADO", conta3.__dict__)
    print("-"*35)

    conta1.extrato()
    conta1.tranferir(200.0, conta2)
    conta2.extrato()
    print("-" * 35)

    cliente = Cliente("diegO")
    print(cliente.nome)
    cliente.nome = "Julia"
    print(cliente.nome)
    print("-"*35)

    print(conta1.limite)
    conta1.limite = 1200.0
    conta1.limite = 1100.0
    print("-"*35)

    conta3.sacar(3000)
    conta3.sacar(1000)
    print("-" * 35)

    # print(conta1.codigo)
    print(conta2.codigo_banco())
    print(Conta.codigo_banco())
    print(Conta.codigo_banco2())
    print("-" * 35)

    nova_conta = Conta.criar_conta(nmr=123, ttlr="Diego", sld=2000.0, lmt=5000.0)
    print(nova_conta)


