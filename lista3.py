# Lista 3 - Algoritmos de Ordenação (O) = nlog(n)
# Alunos:
#   Lucas Soares Souza - 14/0151257
#   Thiago Ferreira - 15/0149948

import numpy as np
import time
import random
from random import randint
import matplotlib.pyplot as plt

print("hello world")

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

def gerarArraysDeTeste(tamanho_minimo_array,tamanho_maximo_array,valor_minimo,valor_maximo):
    testes = []
    print("")
    print("Gerando arrays com valores aleatorios")
    print("")
    for tamanho in range(tamanho_minimo_array, tamanho_maximo_array):

        testes.append(random.sample(range(valor_minimo,valor_maximo+1), tamanho+1))
        #print(str(testes[tamanho]))

    print("Arrays gerados com sucesso!")


# Entradas

tamanho_minimo_array = int(input("Entre com o tamanho minimo para os arrays: "))
tamanho_maximo_array = int(input("Entre com o tamanho maximo para os arrays: "))
valor_minimo = int(input("Entre com o valor minimo do intervalo: "))
valor_maximo = int(input("Entre com o valor máximo do intervalo: "))

testes = gerarArraysDeTeste(tamanho_minimo_array,tamanho_maximo_array,valor_minimo,valor_maximo)
#print(str(testes))
