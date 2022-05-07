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
    cutoff = 30
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
    novo = []
    linha = input().split()
    for i in range(num):
        aux = 0
        for a in matriz:
            if a < int(linha[i]):
                aux += 1
            if a >= int(linha[i]):
                break
        aux = int((aux / len(matriz)) * 100)
        novo.append(aux)
    return novo


def main():
    matriz = [[]]
    while True:
        linha = input().split()
        if linha[0] == "RASTER":
            matriz = raster(int(linha[1]), int(linha[2]))
            matriz = flatten(matriz)
            quicksort(matriz, 0, len(matriz) - 1)

        elif linha[0] == "AMPLITUDE":
            print(amplitude(matriz))
        elif linha[0] == "PERCENTIL":
            aux = percentil(matriz, int(linha[1]))
            for i in range(len(aux)):
                if i == len(aux) - 1:
                    print(aux[i])
                else:
                    print(aux[i], end=' ')
        elif linha[0] == "MEDIANA":
            print(mediana(matriz))
        elif linha[0] == "TCHAU":
            break


if __name__ == "__main__":
    main()
