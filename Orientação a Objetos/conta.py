class Cliente:
    def __init__(self, nome: str):
        """
        Instancia um objeto do tipo Cliente
        :param nome: str
        """
        self.__nome = nome

    @property
    def nome(self):
        print("ISSO É UMA FUNÇÃO, NÃO UM ATRIBUTO...")
        return self.__nome.upper()

    @nome.setter
    def nome(self, nome):
        print("CHAMANDO O SETTER NOME")
        self.__nome = nome


class Conta:

    CODIGO_BANCO = "001"

    def __init__(self, numero: int, titular: str, saldo: float, limite: float = 1000.0) -> None:
        """
        Construção de um Objeto do Tipo Conta
        :param self: Conta
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
        #self.__codigo_banco = "001"
        print("OBJETO INSTANCIADO:", self)

    @staticmethod
    def codigo_banco_cls_1():
        return "001"

    @staticmethod
    def codigo_banco_cls_2():
        return Conta.CODIGO_BANCO

    @classmethod
    def criar_conta(cls, nmr, ttlr, sld, lmt):
        ttlr = ttlr.title()
        if sld > 0:
            return cls(numero=nmr, saldo=sld, titular=ttlr, limite=lmt)
        else:
            return None

    # @property
    # def codigo_banco(self):
    #     return self.__codigo_banco

    def extrato(self) -> None:
        """
        Retorna o nome e o saldo do usuário
        :return: None
        """
        print("TITULAR: ", self.__titular, "SALDO: ", self.__saldo)

    def __verificar_saque(self, valor: float) -> bool:
        """
        Valida se o usuário pode ou não sacar determinado valor
        :param valor: float
        :return: bool
        """
        if valor > self.__limite + self.__saldo:
            return False
        return True

    def sacar(self, valor: float) -> None:
        """
        Saca determinado valor da conta de um usuário
        :param valor: float
        :return: None
        """
        if self.__verificar_saque(valor):
            self.__saldo -= valor
        else:
            print("VALOR ACIMA DO PERMITIDO...")

    def depositar(self, valor: float) -> None:
        """
        Deposita determinado valor na conta de um usuário
        :param valor: float
        :return: None
        """
        self.__saldo += valor

    def transferir(self, conta_destino, valor: float) -> None:
        """
        Transfere determinado valor de uma conta para outra
        :param conta_destino: Conta
        :param valor: float
        :return: None
        """
        # self é a conta de origem
        self.sacar(valor)
        conta_destino.depositar(valor)

    @property
    def limite(self) -> float:
        """
        Retorna o Limite
        :return: float
        """
        return self.__limite

    @limite.setter
    def limite(self, valor: float) -> None:
        """
        Determina um novo valor de limite para uma conta
        :param valor: float
        :return: none
        """
        if valor > 1.1*self.__limite:
            print("INFELIZMENTE O LIMITE ESTÁ ACIMA DE 10%")
            print("LIMITE NÃO ALTERADO: ", self.limite)
        else:
            self.__limite = valor
            print("LIMITE ALTERADO COM SUCESSO")
            print("NOVO VALOR: ", self.limite)


if __name__ == "__main__":
    conta_1 = Conta(123, "Fulano", 1000.0)
    print("OBJETO CRIADO:", conta_1)
    conta_1.extrato()

    # dic = conta_1.__dict__
    # print(dic)
    # print(vars(conta_1))

    conta_2 = Conta(numero=456, titular="Beltrano", saldo=0.0, limite=2000)
    print("OBJETO CRIADO:", conta_2)
    conta_1.transferir(conta_2, 100.0)
    print(vars(conta_1))
    dic = conta_2.__dict__
    print(dic)

    # cliente = Cliente("clebinho")
    # print(cliente.nome)
    # nome = input("ENTRE COM UM NOME: ")
    # cliente.nome = nome
    # print(cliente.nome)

    print(conta_1.limite)
    conta_1.limite = 1200.00
    conta_1.limite = 1100.00

    conta_1.sacar(1999)
    conta_1.extrato()

    # print(conta_1.codigo_banco)
    # print(conta_2.codigo_banco)
    print(Conta.codigo_banco_cls_1())
    print(conta_1.codigo_banco_cls_2())

    nova_conta = Conta.criar_conta(nmr=123, lmt=1000.0, ttlr="maria aparecida", sld=-1)
    print(nova_conta)
