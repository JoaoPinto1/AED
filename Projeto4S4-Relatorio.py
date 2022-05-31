import random
import time


def raster(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        aux = input().split()
        for a in range(colunas):
            linha.append(int(aux[a]))
        matriz.append(linha)
    print("RASTER GUARDADO")
    return matriz


def flatten(matriz):
    aux = []
    for i in matriz:
        for a in i:
            aux.append(a)
    return aux


def mediana(matriz):
    if len(matriz) % 2 == 0:
        return int((matriz[int(len(matriz)/2-1)]+matriz[int(len(matriz)/2)])/2)
    else:
        return matriz[int(len(matriz)/2)]


def amplitude(matriz):
    return matriz[len(matriz)-1]-matriz[0]


def percentil(matriz, num):
    linha = [random.randint(1,num) for i in range(num)]
    lista = []
    for i in range(num):
        inicio = 0
        fim = len(matriz) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if int(linha[i]) == matriz[meio]:
                lista.append(meio)
                break
            if int(linha[i]) < matriz[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1


def counting_sort(matriz,num):
    end = [0] * len(matriz)
    count = [0] * (num+1)
    for i in range(len(matriz)):
        count[matriz[i]] += 1
    for i in range(1,num+1):
        count[i] += count[i-1]
    for i in range(len(matriz)-1, -1, -1):
        end[count[matriz[i]]-1] = matriz[i]
        count[matriz[i]] -= 1
    return end


def main():
    for n in range(10000,100001,10000):
        matriz = [random.randint(1, n) for i in range(n)]
        start = time.time()
        counting_sort(matriz,n)
        percentil(matriz, n)
        end = time.time()
        print(end - start)


if __name__ == "__main__":
    main()
