import random
import time


class No:
    def __init__(self, categoria, valor, nivel):
        self.categoria = categoria
        self.valor = valor
        self.filhos = []
        self.nivel = nivel
        self.soma = valor

    def add_filhos(self, no):
        self.filhos.append(no)


def main():
    randomcenas(50)
    with open("teste.txt","r") as ya:
        lista1 = ya.readlines()
        ya.close()
    raiz = No(lista1[0].split()[0],int(lista1[0].split()[1]),0)
    n = int(lista1[0].split()[2])
    nivelmaximo = 0
    if n > 0:
        nivelmaximo = ciclo_input(int(n), raiz, 0, lista1, 1)
    start = time.time()
    raiz.soma = aplica_soma(raiz)  # atualiza o valor soma de cada categoria
    lista = [""] * (nivelmaximo + 1)
    lista[0] = raiz.categoria + "(" + str(raiz.soma) + ")"
    print(lista[0])
    print_correto(raiz, lista, 1)
    end = time.time()
    print(end-start)
    for i in range(1, nivelmaximo + 1):
        print(lista[i][:-1])
    return 0


def randomcenas(x10):
    with open("teste.txt", 'w') as file_output:
        for i in range(x10):
            if i == 0 and x10 != 0:
                file_output.write(
                    "Todos 0 3\nArte 5 2\nClassica 1000 0\nFotografia 50 0\nLivros 100 0\nMusica 0 3\nRock 20 1\nSoftRock 5 0\nPop 20 0\nCountry 20 1")
            elif i != x10 - 1:
                file_output.write(
                    "\nTodos 0 3\nArte 5 2\nClassica 1000 0\nFotografia 50 0\nLivros 100 0\nMusica 0 3\nRock 20 1\nSoftRock 5 0\nPop 20 0\nCountry 20 1")
            else:
                file_output.write(
                    "\nTodos 0 3\nArte 5 2\nClassica 1000 0\nFotografia 50 0\nLivros 100 0\nMusica 0 3\nRock 20 1\nSoftRock 5 0\nPop 20 0\nCountry 20 0")


def ciclo_input(n, no, nivel, lista, a):
    aux = nivel + 1
    laux = aux
    for i in range(n):
        cat, valor, num = lista[a].split()
        a+=1
        novoNo = No(cat, int(valor), aux)
        no.add_filhos(novoNo)
        if int(num) > 0:
            laux1 = ciclo_input(int(num), novoNo, aux, lista, a)
            if laux1 > laux:
                laux = laux1
    return laux


def aplica_soma(no):
    if len(no.filhos) == 0:
        return no.valor
    soma = no.valor
    for node in no.filhos:
        node.soma = aplica_soma(node)
        soma += node.soma
    return soma


def print_correto(no, lista, i):
    for node in no.filhos:
        lista[i] += node.categoria + "(" + str(node.soma) + ") "
        print_correto(node, lista, i + 1)


if __name__ == "__main__":
    main()
