import abc


class Carro(abc.ABC):
    """Classe carro pra instanciar novos carros"""

    def __init__(self, cor, qtdPortas, tipoCombustivel, potencia):
        self.cor = cor
        self.qtdPortas = qtdPortas
        self.tipoCombustivel = tipoCombustivel
        self.qtdCombustivel = 0
        self.potencia = potencia
        self.isLigado = False

    @abc.abstractmethod
    def abastecer(self, qtd):
        self.qtdCombustivel += qtd

    def ligar(self):
        if self.isLigado:
            print("Carro ja esta ligado")
        else:
            self.isLigado = True

    def desligar(self, qtdCombustivelUsada):
        if self.isLigado == False:
            print("Carro ja esta desligado")
        else:
            self.isLigado = False
            self.qtdCombustivel -= qtdCombustivelUsada
