from listas import lista_ligada
from espalhamento import tabela_espalhamento


class Conjunto:
    def __init__(self):
        self.__elementos = tabela_espalhamento.TabelaEspalhamento()

    def inserir(self, elemento):
        self.__elementos.inserir_elemento(elemento)

    def __str__(self):
        return self.__elementos.__str__()

    def contem(self, elemento):
        return self.__elementos.contem(elemento)

    def esta_vazio(self):
        return self.__elementos.tamanho == 0

    def remover_elemento(self, elemento):
        self.__elementos.remover(elemento)
