class Veiculo():
    def __init__(self, dono, modelo):
        self._dono = dono
        self.nivel_tanque = 0
        self._modelo = modelo

    def abastecer(self, litros):
        self.nivel_tanque = self.nivel_tanque  + litros

    def verificar_ar_condicionado(self):
        return ("Veículo não possui ar condicionado")


class Carro(Veiculo):
    def __init__(self, dono, modelo):
        super().__init__(dono, modelo)

    def verificar_dono(self):
        return self._dono

    def verificar_ar_condicionado(self):
        return ("Veículo possui ar condicionado")

    def __str__(self):
        return self._modelo


class Moto(Veiculo):
    def __init__(self, dono, modelo):
        super().__init__(dono, modelo)

    def verificar_dono(self):
        return self._dono


if __name__ == "__main__":
    palio = Carro("Clebinho", "Palio")
    cg160 = Moto("Julia", "CG160")
    palio.abastecer(20)
    palio.abastecer(20)
    cg160.abastecer(10)
    print("Palio: ", palio.nivel_tanque)
    print("CG160: ", cg160.nivel_tanque)
    print("-"*30)

    print(palio.verificar_dono())
    print(cg160.verificar_dono())
    print("-" * 30)

    print(cg160.verificar_ar_condicionado())
    print(palio.verificar_ar_condicionado())
    print("-" * 30)

    print(palio)
    print(cg160)
