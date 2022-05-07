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


def insertionsort(matriz):
    for i in range(1, len(matriz)):
        aux = matriz[i]
        a = i
        while aux < matriz[a-1] and a > 0:
            matriz[a] = matriz[a-1]
            a -= 1
        matriz[a] = aux


def troca(matriz,index1,index2):
    aux = matriz[index1]
    matriz[index1] = matriz[index2]
    matriz[index2] = aux


def quicksort(matriz, low, high):
    cutoff = 150
    if low+cutoff > high:
        insertionsort(matriz)
    else:
        meio = (low+high)//2
        if matriz[meio] < matriz[low]:
            troca(matriz, low, meio)
        if matriz[high] < matriz[low]:
            troca(matriz, low, high)
        if matriz[high] < matriz[meio]:
            troca(matriz, meio, high)
        troca(matriz, meio, high-1)
        pivot = matriz[high-1]
        i, j = low, high-1
        while i <= j:
            while matriz[i] <= pivot:
                i += 1
                if i == high:
                    break
            while pivot <= matriz[j]:
                j -= 1
                if j == low:
                    break
            troca(matriz, i, j)
        troca(matriz, i, high-1)
        quicksort(matriz, low, i-1)
        quicksort(matriz, i+1, high)


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
    linha = [random.randint(1, num) for i in range(num)]
    for i in range(num):
        low = 0
        high = num - 1
        while low <= high:
            mid = (high+low)//2
            if matriz[mid] == linha[i]:
                break
            if matriz[mid] < linha[i]:
                low = mid + 1
            else:
                high = mid - 1


def main():
    for n in range(10000, 100001, 10000):
        matriz = [random.randint(1, n) for i in range(n)]
        start = time.time()
        quicksort(matriz, 0, n-1)
        percentil(matriz, n)
        end = time.time()
        print(end - start)


if __name__ == "__main__":
    main()
