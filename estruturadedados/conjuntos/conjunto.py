from listas import lista_ligada


class Conjunto():
    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()

    def inserir(self, elemento):
        if not self.contem(elemento):
            self.__elementos.inserir_elemento(elemento)
            return True
        return False

    def inserir_posicao(self, posicao, elemento):
        if not self.contem(elemento):
            self.__elementos.inserir_elemento_posicao(posicao,elemento)
            return True
        return False

    def __str__(self):
        return self.__elementos.__str__()

    def conjunto_esta_vazio(self):
        return self.__elementos.lista_esta_vazia()

    def contem(self, elemento):
        return self.__elementos.contem(elemento)

    def recuperar_elemento_no(self, posicao):
        return self.__elementos.recuperar_elemento_no(posicao)

    def recuperar_no(self, posicao):
        return self.__elementos.recuperar_no(posicao)

    def tamanho(self):
        return self.__elementos.tamanho

    def esta_vazio(self):
        return self.__elementos.lista_esta_vazia()

    def remover_posicao(self, posicao):
        self.__elementos.remover_posicao(posicao)

    def remover_elemento(self,elemento):
        self.__elementos.remover_elemento(elemento)