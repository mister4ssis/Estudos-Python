from array import array
from vetores import vetor
from listas import lista_ligada
from listas import lista_duplamente_ligada
from pilhas import pilhas
from filas import filas

print(30*'-', "MENU", 30*'-')
print('1. Vetores')
print('2. Lista Ligadas')
print('3. listas Duplamente Ligadas')
print('4. Pilhas')
print('5. Filas')

# menu = int(input("Digite a opção desejada: "))
menu = 5
if menu == 1:
    vetor_teste = vetor.Vetor(3)
    # vetor_teste.inserir_elemento_posicao(1,0)
    vetor_teste.inserir_elemento_final(1)
    vetor_teste.inserir_elemento_final(2)
    vetor_teste.inserir_elemento_final(3)
    vetor_teste.inserir_elemento_final(6)
    vetor_teste.inserir_elemento_final(6)
    vetor_teste.inserir_elemento_final(6)

    print(vetor_teste.contem(6))
    print(vetor_teste.indice(6))
    print(vetor_teste.count_elementos(6))
    print(vetor_teste)
    vetor_teste.remover_elemento(2)
    print(vetor_teste)
elif menu==2:
    lista_teste = lista_ligada.ListaLigada()
    lista_teste.inserir_elemento(1)
    lista_teste.inserir_elemento(2)
    lista_teste.inserir_elemento(2)
    lista_teste.inserir_elemento_posicao(0,4)
    lista_teste.inserir_elemento_posicao(4,6)
    lista_teste.inserir_elemento_posicao(2,15)
    print(lista_teste)
    lista_teste.remover_posicao(0)
    print(lista_teste)
    lista_teste.remover_elemento(15)
    print(lista_teste)
    print(lista_teste.indice(15))
elif menu ==3:
    lista_teste = lista_duplamente_ligada.ListaDuplamenteLigada()

    lista_teste.inserir_elemento(1)
    lista_teste.inserir_elemento(2)
    lista_teste.inserir_elemento(2)
    lista_teste.inserir_elemento_posicao(0,4)
    lista_teste.inserir_elemento_posicao(4,6)
    lista_teste.inserir_elemento_posicao(2,15)
    print(lista_teste)
    lista_teste.remover_posicao(0)
    print(lista_teste)
    lista_teste.remover_elemento(15)
    print(lista_teste)
    print(lista_teste.indice(15))
elif menu == 4:
    pilha_teste = pilhas.Pilha()
    pilha_teste.empilhar(1)
    print(pilha_teste.desempilhar())
elif menu == 5:
    fila_teste = filas.Filas()
    fila_teste.enfileirar(1)
    fila_teste.enfileirar(3)
    fila_teste.enfileirar(5)
    print(fila_teste)
    print(fila_teste.desinfileirar())
    print(fila_teste.desinfileirar())
    print(fila_teste.desinfileirar())
    print(fila_teste.desinfileirar())
    print(fila_teste)


