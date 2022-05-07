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


def amplitude(matriz):
    nova_matriz = flatten(matriz)
    min, max = min_and_max(nova_matriz)
    return max-min


def min_and_max(matriz):
    min = matriz[0]
    max = matriz[0]
    for i in matriz:
        if i > max:
            max = i
        if i < min:
            min = i
    return min, max


def flatten(matriz):
    aux = []
    for i in matriz:
        for a in i:
            aux.append(a)
    return aux


def percentil(matriz, num, linha):
    for i in range(num):
        aux = 0
        for a in matriz:
            if a < linha[i]:
                aux += 1


def mediana(matriz):
    aux = flatten(matriz)
    while len(aux) > 1:
        min, max = min_and_max(aux)
        aux.remove(min)
        aux.remove(max)
        if len(aux) == 2:
            return int((aux[0]+aux[1])/2)
    return aux[0]


def main():
    for n in range(10000,100001,10000):
        matriz = [random.randint(1,n) for i in range(n)]
        linha = [random.randint(1, n) for i in range(n)]
        start = time.time()
        percentil(matriz, n, linha)
        end = time.time()
        print(end-start)


if __name__ == "__main__":
    main()
