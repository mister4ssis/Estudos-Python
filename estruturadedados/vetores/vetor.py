class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    def inserir_elemento_posicao(self, elemento, posicao):
        vetor_inicio = self.__elementos[:posicao] + [None]
        vetor_final = self.__elementos[posicao:]
        vetor_inicio[len(vetor_inicio) - 1] = elemento

        self.__elementos = vetor_inicio + vetor_final

        self.__posicao += 1

    def inserir_elemento_final(self, elemento):
        if self.__posicao >= self.tamanho_vetor():
            self.__elementos = self.__elementos + [None]
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]

    def tamanho_vetor(self):
        return len(self.__elementos)

    def __str__(self):
        return '\n' .join([str(i) for i in self.__elementos])

    def contem(self, elemento_a_ser_procurado):
        for i in range(self.tamanho_vetor()):
            elemento_posicao_i = self.listar_elemento(i)
            if elemento_posicao_i == elemento_a_ser_procurado:
                return True

        return False

    def indice(self, elemento_a_ser_procurado):
        for i in range(self.tamanho_vetor()):
            elemento_posicao_i = self.listar_elemento(i)
            if elemento_posicao_i == elemento_a_ser_procurado:
                return i

        return -1

    def count_elementos(self, elemento_a_ser_procurado):
        count = 0
        for i in range(self.tamanho_vetor()):
            elemento_posicao_i = self.listar_elemento(i)
            if elemento_posicao_i == elemento_a_ser_procurado:
                count += 1

        return count

    def remover_elemento_posicao(self, posicao):
        vetor_inicio = self.__elementos[:posicao]
        vetor_final = self.__elementos[posicao + 1:]
        self.__elementos = vetor_inicio + vetor_final
        self.__posicao -= 1

    def remover_elemento(self, elemento):
        posicao = self.indice(elemento)
        self.remover_elemento_posicao(posicao)


