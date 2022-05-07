def roda90(matriz, linhas, colunas):
    novamatriz = []
    for i in range(colunas):
        aux = []
        for a in range(linhas):
            aux.append(matriz[linhas - a - 1][i])
        novamatriz.append(aux)
    return novamatriz


def printmatriz(matriz):
    for i in range(len(matriz)):
        for a in range(len(matriz[i])):
            if a != 0:
                print(" ", end="")
            print(matriz[i][a], end="")
        print()
    return 0


def main():
    matriz = []
    linhas, colunas = input("").split(" ")
    for i in range(int(linhas)):
        matriz.append(input("").split(" "))
    novamatriz = roda90(matriz, int(linhas), int(colunas))
    print(90)
    printmatriz(novamatriz)
    print(180)
    novamatriz2 = roda90(novamatriz, int(colunas), int(linhas))
    printmatriz(novamatriz2)
    print(270)
    printmatriz(roda90(novamatriz2, int(linhas), int(colunas)))
    return 0


if __name__ == "__main__":
    main()
