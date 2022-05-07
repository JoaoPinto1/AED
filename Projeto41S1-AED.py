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


def percentil(matriz, num):
    nova_matriz = flatten(matriz)
    novo = []
    linha = input().split()
    for i in range(num):
        aux = 0
        for a in nova_matriz:
            if a < int(linha[i]):
                aux += 1
        aux = int((aux/len(nova_matriz))*100)
        novo.append(aux)
    return novo


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
    matriz = [[]]
    while True:
        linha = input().split()
        if linha[0] == "RASTER":
            matriz = raster(int(linha[1]), int(linha[2]))
        elif linha[0] == "AMPLITUDE":
            print(amplitude(matriz))
        elif linha[0] == "PERCENTIL":
            aux = percentil(matriz, int(linha[1]))
            for i in range(len(aux)):
                if i == len(aux)-1:
                    print(aux[i])
                else:
                    print(aux[i], end=' ')
        elif linha[0] == "MEDIANA":
            print(mediana(matriz))
        elif linha[0] == "TCHAU":
            break


if __name__ == "__main__":
    main()
