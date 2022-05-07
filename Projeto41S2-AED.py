def ordena(matriz):
    for i in range(1, len(matriz)):
        aux = matriz[i]
        a = i
        while aux < matriz[a-1] and a > 0:
            matriz[a] = matriz[a-1]
            a -= 1
        matriz[a] = aux


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
    return matriz[len(matriz)-1]-matriz[0]


def percentil(matriz, num):
    novo = []
    linha = input().split()
    for i in range(num):
        aux = 0
        for a in range(len(matriz)):
            if matriz[a] == linha[i]:
                novo.append(((a-1) / len(matriz)) * 100)
                break
    return novo


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


def main():
    matriz = [[]]
    while True:
        linha = input().split()
        if linha[0] == "RASTER":
            matriz = raster(int(linha[1]), int(linha[2]))
            matriz = flatten(matriz)
            ordena(matriz)
            print(matriz)

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