import random, time


def busca_linear(numeros, numero_a_ser_pesquisado):
    for i in range(len(numeros)):
        if numeros[i] == numero_a_ser_pesquisado:
            return i
    return -1


def selection_sort(numeros):
    for i in range(len(numeros)):
        indice_menor = i
        for j in range(int(i+1),  len(numeros)):
            if numeros[j] < numeros[indice_menor]:
                indice_menor = j
        temp = numeros[indice_menor]
        numeros[indice_menor] = numeros[i]
        numeros[i] = temp
    return numeros


def busca_binaria(list_numeros, numero_busca):
    inicio = 0
    meio = 0
    fim = len(list_numeros) -1
    while inicio <= fim:
        meio = int((inicio+fim)/2)
        if list_numeros[meio] < numero_busca:
            inicio = meio +1
        elif list_numeros[meio] > numero_busca:
            fim = meio - 1
        else:
            return meio
    return -1


list_numeros = list()


for i in range(10000):
    # list_numeros.append(i+1)
    list_numeros.append(random.randint(1,30000))
    # numeros.append(random.randint(1,30))

numero_a_ser_pesquisado = 20

# Busca Linear

print(" ----  Busca Linear  ----  ")
start_time = time.time()
posicao_resultado = busca_linear(list_numeros,numero_a_ser_pesquisado)
print("--- %s seconds ---" % (round(time.time() - start_time, 5)))
if posicao_resultado >= 0:
    print(f"Valor - {numero_a_ser_pesquisado} - encontrado na posição {posicao_resultado}")
else:
    print(f"Valor - {numero_a_ser_pesquisado} - não encontrado")

# Busca Binaria
print(" ---- Busca Binária ----  ")

start_time = time.time()
numeros_ordenado = selection_sort(list_numeros)

posicao_resultado = busca_binaria(numeros_ordenado,numero_a_ser_pesquisado)
print("--- %s seconds ---" % (round(time.time() - start_time, 5)))
if posicao_resultado >= 0:
    print(f"Valor - {numero_a_ser_pesquisado} - encontrado na posição {posicao_resultado}")
else:
    print(f"Valor - {numero_a_ser_pesquisado} - não encontrado")



