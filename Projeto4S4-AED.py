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
    matriz = [[]]
    while True:
        linha = input().split()
        if linha[0] == "RASTER":
            matriz = raster(int(linha[1]), int(linha[2]))
            matriz = flatten(matriz)
            num = max(matriz)
            matriz = counting_sort(matriz,num)

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
