import random
import sys
import time


class No:
    def __init__(self, nome, hash, valor):
        self.nome = nome
        self.hash = hash
        self.valor = valor
        self.pai = None
        self.fesquerdo = None
        self.fdireito = None


class ArvoreSlay:
    def __init__(self):
        self.raiz = None

    def listagem(self, no):
        if no is not None:
            self.listagem(no.fesquerdo)
            print(no.nome + " " + str(no.hash) + " " + str(no.valor))
            self.listagem(no.fdireito)

    def consulta(self, no, nome):
        if not no or nome == no.nome:
            return no
        if nome < no.nome:
            return self.consulta(no.fesquerdo, nome)
        else:
            return self.consulta(no.fdireito, nome)

    def inserir(self, nome, hash, valor):
        novoNo = No(nome, hash, valor)
        x = self.raiz
        y = None

        while x is not None:
            y = x
            if nome == x.nome:
                return None
            if nome < x.nome:
                x = x.fesquerdo
            else:
                x = x.fdireito
        novoNo.pai = y
        if y is None:
            self.raiz = novoNo
        elif nome < y.nome:
            y.fesquerdo = novoNo
        else:
            y.fdireito = novoNo

        return novoNo

    def splay(self, no):
        # enquanto o no nao for a raiz continua em loop
        while no.pai is not None:
            if not no.pai.pai:
                if no == no.pai.fesquerdo:
                    self.zig(no.pai)
                else:
                    self.zag(no.pai)
            elif no == no.pai.fesquerdo and no.pai == no.pai.pai.fesquerdo:
                self.zig(no.pai.pai)
                self.zig(no.pai)
            elif no == no.pai.fdireito and no.pai == no.pai.pai.fdireito:
                self.zag(no.pai.pai)
                self.zag(no.pai)
            elif no == no.pai.fdireito and no.pai == no.pai.pai.fesquerdo:
                self.zag(no.pai)
                self.zig(no.pai)
            else:
                self.zig(no.pai)
                self.zag(no.pai)

    def zig(self, no):
        aux = no.fesquerdo
        no.fesquerdo = aux.fdireito
        if aux.fdireito is not None:
            aux.fdireito.pai = no
        aux.pai = no.pai
        if not no.pai:
            self.raiz = aux
        elif no == no.pai.fdireito:
            no.pai.fdireito = aux
        else:
            no.pai.fesquerdo = aux
        aux.fdireito = no
        no.pai = aux

    def zag(self, no):
        aux = no.fdireito
        no.fdireito = aux.fesquerdo
        if aux.fesquerdo is not None:
            aux.fesquerdo.pai = no
        aux.pai = no.pai
        if not no.pai:
            self.raiz = aux
        elif no == no.pai.fesquerdo:
            no.pai.fesquerdo = aux
        else:
            no.pai.fdireito = aux
        aux.fesquerdo = no
        no.pai = aux


def lerinput(arvore, n):
    i = 0
    while i < 2*n:
        linha = ["ARTIGO",i,"123abc",1]
        if i == n:
            start = time.time()
        if i > n -1:
            linha = ["CONSULTA",random.randint(0,int(n*0.05))]
        if i > n + int(n*0.9):
            linha = ["CONSULTA", random.randint(int(n*0.05)+1, n)]
        if linha[0] == "ARTIGO":
            no = arvore.inserir(linha[1], linha[2], int(linha[3]))
            if not no:
                #print("ARTIGO JA EXISTENTE")
                continue
            else:
                # inserido no final da arvore, altura de mover para a raiz
                arvore.splay(no)
                #print("NOVO ARTIGO INSERIDO")

        elif linha[0] == "OFERTA":
            no = arvore.consulta(arvore.raiz, linha[1])
            if not no:
                print("ARTIGO NAO REGISTADO")
            else:
                no.valor = int(linha[2])
                arvore.splay(no)
                print("OFERTA ATUALIZADA")
        elif linha[0] == "CONSULTA":
            no = arvore.consulta(arvore.raiz, linha[1])
            if not no:
                print("ARTIGO NAO REGISTADO")
            else:
                #print(str(no.nome) + " " + str(no.hash) + " " + str(no.valor))
                arvore.splay(no)
                #print("FIM")
        elif linha[0] == "LISTAGEM":
            arvore.listagem(arvore.raiz)
            print("FIM")
        elif linha[0] == "APAGA":
            arvore.raiz = None
            print("CATALOGO APAGADO")
        elif linha[0] == "FIM":
            break
        i += 1
    end = time.time()
    print(end-start)


def main():
    sys.setrecursionlimit(10000)
    arvore = ArvoreSlay()
    n = 3000
    lerinput(arvore, n)
    return 0


if __name__ == "__main__":
    main()
