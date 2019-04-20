# Lista 3 - Algoritmos de Ordenação (O) = nlog(n)
# Alunos:
#   Lucas Soares Souza - 14/0151257
#   Thiago Ferreira - 15/0149948

import numpy as np
import time
import random
from random import randint
import matplotlib.pyplot as plt
from copy import deepcopy

# Algoritmos de Ordenação (O) = n² versus (O) = nlog(n)

# ALGORITMOS N²

# Bubble Sort

def bubbleSort(lista,printar_processo):
        elementos = len(lista)-1
        ordenado = False

        if(printar_processo == True):
            print(lista)

        while not ordenado:
            ordenado = True
            for i in range(elementos):
                if lista[i] > lista[i+1]:
                    lista[i], lista[i+1] = lista[i+1], lista[i]
                    ordenado = False
                    if(printar_processo == True):
                        print(lista)
        return lista

# Insertion Sort

def insertionSort(lista, printar_processo):

    tamanho_lista = len(lista)
    auxiliar_posicao_lista = 0
    auxiliar_swap = 0

    if(printar_processo == True):
        print(lista)


    for valor in range(1, tamanho_lista):

        auxiliar_posicao_lista = valor

        while((auxiliar_posicao_lista != 0) and lista[auxiliar_posicao_lista] < lista[auxiliar_posicao_lista - 1]):

            auxiliar_swap = lista[auxiliar_posicao_lista]
            lista[auxiliar_posicao_lista] = lista[auxiliar_posicao_lista - 1]
            lista[auxiliar_posicao_lista - 1] = auxiliar_swap
            auxiliar_posicao_lista -= 1

            if(printar_processo == True):
                print(lista)

    if(printar_processo == True):
        print(lista)

    return lista

# ALGORITIMOS NLOG(N)

# Bucket Sort
#Encontrado e adaptado a partir de: https://www.sanfoundry.com/python-program-implement-bucket-sort/
#Acesso em: 04/04/2019

def bucketSort(alist, printar_processo):

    #dimensionando baldes
    largest = max(alist)
    length = len(alist)
    size = largest/length

    #criando baldes
    buckets = [[] for _ in range(length)]

    if(printar_processo == True):
        print(buckets)

    #adicionando valores dentro dos baldes
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])

    if(printar_processo == True):
        print(buckets)

    #ordenando baldes usando o insertion sort
    for i in range(length):
        insertionSort(buckets[i],False)

    if(printar_processo == True):
        print(buckets)

    result = []
    for i in range(length):
        result = result + buckets[i]

    return result

 # Quick Sort

 #Encontrado em: https://stackoverflow.com/questions/18262306/quicksort-with-python
#Acesso em: 04/04/2019

def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quickSort(less)+equal+quickSort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

def gerarArraysDeTeste(tamanho_minimo_array,tamanho_maximo_array,valor_maximo):
    testes = []
    print("")
    print("Gerando arrays com valores aleatorios")
    print("")
    for tamanho in range(tamanho_minimo_array, tamanho_maximo_array+1):

        testes.append(random.sample(range(0,valor_maximo+1), tamanho))
        #print(str(testes[tamanho]))

    print("Arrays gerados com sucesso!")
    return testes

def gerarArrayDeIndices(tamanho_minimo_array,tamanho_maximo_array):

    indices = []
    for indice in range(tamanho_minimo_array, tamanho_maximo_array+1):

        indices.append(indice)

    return indices

# Entradas

tamanho_minimo_array = int(input("Entre com o tamanho minimo para os arrays: "))
tamanho_maximo_array = int(input("Entre com o tamanho maximo para os arrays: "))
valor_maximo = int(input("Entre com o valor máximo do intervalo: "))

testes = gerarArraysDeTeste(tamanho_minimo_array,tamanho_maximo_array,valor_maximo)
print("Quantidade de arrays criados: " + str(len(testes)))
indices = gerarArrayDeIndices(tamanho_minimo_array,tamanho_maximo_array)


# Ordenando arrays e coletando tempos

tempos_bubble = []
tempos_insertion = []
tempos_bucket = []
tempos_quick = []

contador = 1

print("Iniciando testes...")
for array in testes:

    bubble = deepcopy(array)
    insertion = deepcopy(array)
    bucket = deepcopy(array)
    quick = deepcopy(array)

    print("bubble teste " + str(contador))
    inicial_tempo_bubble = time.time()
    bubble = bubbleSort(bubble,False)
    final_tempo_bubble = time.time()
    tempos_bubble.append(final_tempo_bubble - inicial_tempo_bubble)

    print("insertion teste " + str(contador))
    inicial_tempo_insertion = time.time()
    insertion = insertionSort(insertion,False)
    final_tempo_insertion = time.time()
    tempos_insertion.append(final_tempo_insertion - inicial_tempo_insertion)

    print("bucket teste " + str(contador))
    inicial_tempo_bucket = time.time()
    bucket = bucketSort(bucket, False)
    final_tempo_bucket = time.time()
    tempos_bucket.append(final_tempo_bucket - inicial_tempo_bucket)

    print("quick teste " + str(contador))
    inicial_tempo_quick = time.time()
    quick = quickSort(quick)
    final_tempo_quick = time.time()
    tempos_quick.append(final_tempo_quick - inicial_tempo_quick)

    print("Teste " + str(contador) + "finalizado!")
    contador +=1

plt.plot(tempos_bubble,label='Bubble Sort')
plt.plot(tempos_insertion,label='Insertion Sort')
plt.plot(tempos_bucket,label='Bucket Sort')
plt.plot(tempos_quick,label='Quick Sort')
plt.legend()
plt.title("Comparando Tempos")
plt.xlabel("Tamanho dos Arrays")
plt.ylabel("Tempo de Execucao")
plt.show()
