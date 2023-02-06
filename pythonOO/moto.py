import carro


class Moto(carro.Carro):
    def __init__(self, cor, qtdPortas, tipoCombustivel, potencia):
        super().__init__(cor, qtdPortas, tipoCombustivel, potencia)
    def abastecer(self, qtd):
        self.qtdCombustivel += qtd
