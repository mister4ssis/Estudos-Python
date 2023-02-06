from listas import lista_ligada


class Filas:
    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()

    def enfileirar(self, elemento):
        self.__elementos.inserir_elemento(elemento)

    def fila_esta_vazia(self):
        return self.__elementos.lista_esta_vazia()

    def desinfileirar(self):
        if self.fila_esta_vazia():
            return None
        resultado = self.__elementos.recuperar_elemento_no(0)
        self.__elementos.remover_posicao(0)
        return resultado

    def __str__(self):
        temp = self.__elementos.__str__()
        return temp
