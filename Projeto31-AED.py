lista = []


def main():
    cat, valor, n = input("").split(" ")
    dic = {"categoria": cat, "valor": int(valor), "filhos": int(n), "nivel": 0}
    lista.append(dic)
    l = 0
    if int(n) > 0:
        l = cicloInput(int(n), 0)
    for i in range(l + 1):
        c = 0
        for a in range(len(lista)):
            if lista[a]["nivel"] == i:
                soma = lista[a]["valor"]
                if lista[a]["filhos"] > 0:
                    b = a + 1
                    while lista[b]["nivel"] > lista[a]["nivel"]:
                        soma += lista[b]["valor"]
                        b += 1
                        if b == len(lista):
                            break
                if c != 0:
                    print(" ", end="")
                print(lista[a]["categoria"] + "(" + str(soma) + ")", end="")
                c += 1
        print("")
    return 0


def cicloInput(n, l):
    l += 1
    laux = l
    for i in range(n):
        cat, valor, n = input("").split(" ")
        dic = {"categoria": cat, "valor": int(valor), "filhos": int(n), "nivel": l}
        lista.append(dic)
        if int(n) > 0:
            laux1 = cicloInput(int(n), l)
            if laux1 > laux:
                laux = laux1
    return laux


if __name__ == "__main__":
    main()
