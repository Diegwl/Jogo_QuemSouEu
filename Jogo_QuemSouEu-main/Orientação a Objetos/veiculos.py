class Veiculo():
    def __init__(self, dono) -> None:
        self._dono = dono
        self.nivel_tanque = 0 
    
    def abastecer(self, litros):
        self.nivel_tanque = litros

    def verificar_ar_condicionado(self):
        return("NÃO POSSUO AR CONDICIONADO")

class Carro(Veiculo):
    def __init__(self, dono, modelo) -> None:
        super().__init__(dono)
        self.modelo = modelo
    
    def verificar_dono(self):
        return self._dono

    def verificar_ar_condicionado(self):
        return("EU TENHO AR CONDICIONADO!!!")

    def __str__(self) -> str:
        return self.modelo

class Moto(Veiculo):
    def __init__(self, dono) -> None:
        super().__init__(dono)

if __name__ == "__main__":
    palio = Carro("Clebinho", "Palio 2010")
    cg160 = Moto("Fulana")
    palio.abastecer(20)
    cg160.abastecer(10)
    print("PALIO: ", palio.nivel_tanque)
    print("CG160: ", cg160.nivel_tanque)
    print(palio.verificar_dono())
    print("AR CONDICIONADO DA CG: ", cg160.verificar_ar_condicionado())
    print("AR CONDICIONADO DO PALIO: ", palio.verificar_ar_condicionado())
    print(palio)