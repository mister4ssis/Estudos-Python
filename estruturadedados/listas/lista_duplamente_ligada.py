from .no_duplamente_ligada import NoDuplamenteLigada


class ListaDuplamenteLigada:
    def __init__(self):
        self.__primeiro_no = None
        self.__ultimo_no = None
        self.__tamanho = 0

    @property
    def tamanho(self):
        return self.__tamanho

    def inserir_elemento(self, elemento):
        novo_no = NoDuplamenteLigada(elemento)
        if self.lista_esta_vazia():
            self.__primeiro_no = novo_no
            self.__ultimo_no = novo_no
        else:
            self.__ultimo_no.proximo = novo_no
            novo_no.anterior = self.__ultimo_no
            self.__ultimo_no = novo_no

        self.__tamanho += 1

    def inserir_elemento_posicao(self,posicao,elemento):

        if posicao == 0:
            novo_no = NoDuplamenteLigada(elemento)
            novo_no.proximo = self.__primeiro_no
            self.__primeiro_no.anterior =novo_no
            self.__primeiro_no = novo_no
        elif posicao == self.__tamanho:
            novo_no = NoDuplamenteLigada(elemento)
            self.__ultimo_no.proximo = novo_no
            novo_no.anterior = self.__ultimo_no
            self.__ultimo_no = novo_no
        else:
            no_anterior = self.recuperar_no(posicao-1)
            no_atual = self.recuperar_no(posicao)
            novo_no = NoDuplamenteLigada(elemento)
            no_anterior.proximo = novo_no
            novo_no.proximo = no_atual
            no_atual.amterior = novo_no
            novo_no.anterior = no_anterior
        self.__tamanho += 1

    def lista_esta_vazia(self):
        return self.__tamanho == 0

    def __str__(self):
        temp = self.__primeiro_no
        elementos = ''
        while (temp):
            elementos = f'{elementos} {temp.elemento}'
            temp = temp.proximo

        return elementos

    def recuperar_elemento_no(self, posicao):
        no = self.recuperar_no(posicao)
        if no is not None:
            return no.elemento

        return None

    def recuperar_no(self, posicao):
        resultado = 0
        for i in range(posicao + 1):
            if i == 0:
                resultado = self.__primeiro_no
            else:
                resultado = resultado.proximo
        return resultado

    def contem(self,elemento):

        for i in range(self.__tamanho):
            no_atual = self.recuperar_no(i)
            if no_atual.elemento == elemento:
                return True

        return False

    def indice(self,elemento):

        for i in range(self.__tamanho):
            no_atual = self.recuperar_no(i)
            if no_atual.elemento == elemento:
                return i

        return -1

    def remover_posicao(self,posicao):
        if posicao == 0:
            proximo_no = self.__primeiro_no.proximo
            self.__primeiro_no.proximo = None
            self.__primeiro_no.anterior = None
            self.__primeiro_no = None
            self.__primeiro_no = proximo_no
        elif posicao == self.__tamanho - 1:
            no_anterior = self.__ultimo_no.anterior
            no_anterior.proximo = None
            self.__ultimo_no.anterior = None
            self.__ultimo_no = no_anterior
        else:
            no_atual = self.recuperar_no(posicao)
            no_anterior = no_atual.anterior
            no_proximo = no_atual.proximo
            no_anterior.proximo = no_proximo
            no_proximo.anterior = no_anterior
            no_atual.proximo = None
            no_atual.anterior = None
        self.__tamanho -= 1

    def remover_elemento(self,elemento):
        no_remover_posicao = self.indice(elemento)
        self.remover_posicao(no_remover_posicao) if no_remover_posicao >=0 else print("Elemento não existe")


