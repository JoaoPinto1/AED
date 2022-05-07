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
    cat, valor, n = input().split()
    raiz = No(cat, int(valor), 0)
    nivelmaximo = 0
    if int(n) > 0:
        nivelmaximo = ciclo_input(int(n), raiz, 0)
    raiz.soma = aplica_soma(raiz)  # atualiza o valor soma de cada categoria
    lista = [""] * (nivelmaximo + 1)
    lista[0] = raiz.categoria + "(" + str(raiz.soma) + ")"
    print(lista[0])
    print_correto(raiz, lista, 1)
    for i in range(1, nivelmaximo + 1):
        print(lista[i][:-1])
    return 0


def ciclo_input(n, no, nivel):
    aux = nivel + 1
    laux = aux
    for i in range(n):
        cat, valor, num = input("").split(" ")
        novoNo = No(cat, int(valor), aux)
        no.add_filhos(novoNo)
        if int(num) > 0:
            laux1 = ciclo_input(int(num), novoNo, aux)
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
