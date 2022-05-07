import random
import time


class No:
    def __init__(self, username):
        self.username = username
        self.cartoes = []
        self.fesquerdo = None
        self.fdireito = None
        self.altura = 1


def getaltura(no):
    if not no:
        return 0
    return no.altura


def getfe(raiz):
    if not raiz:
        return 0
    if not raiz.fesquerdo:
        auxesquerdo = 0
    else:
        auxesquerdo = getaltura(raiz.fesquerdo)
    if not raiz.fdireito:
        auxdireito = 0
    else:
        auxdireito = getaltura(raiz.fdireito)
    return auxesquerdo - auxdireito


def rotacaoDD(no):
    # auxiliares para fazer rotacao
    aux1 = no.fesquerdo
    aux2 = aux1.fdireito
    # rotacao
    aux1.fdireito = no
    no.fesquerdo = aux2
    # atualizar as alturas após as rotacoes
    no.altura = 1 + max(getaltura(no.fesquerdo), getaltura(no.fdireito))
    aux1.altura = 1 + max(getaltura(aux1.fesquerdo), getaltura(aux1.fdireito))

    return aux1  # retornar a nova raiz da arvore


def rotacaoEE(no):
    # auxiliares para fazer rotacao
    aux1 = no.fdireito
    aux2 = aux1.fesquerdo
    # rotacao
    aux1.fesquerdo = no
    no.fdireito = aux2
    # atualizar alturas apos a rotacao
    no.altura = 1 + max(getaltura(no.fesquerdo), getaltura(no.fdireito))
    aux1.altura = 1 + max(getaltura(aux1.fesquerdo), getaltura(aux1.fdireito))

    return aux1


def addcartao(cartao, no):
    for card in no.cartoes:
        if cartao[0] == card[0]:
            card[1] = cartao[1]
            return 0
    no.cartoes.append(cartao)
    no.cartoes.sort(key=lambda x: x[0])  # ordenar por ordem crescente o numero de cartao
    return 1


class ArvoreAVL:

    def inserir(self, username, cartao, raiz):
        if not raiz:
            no = No(username)
            no.cartoes.append(cartao)
            #print("NOVO UTILIZADOR CRIADO")
            return no
        if username == raiz.username:
            aux = addcartao(cartao, raiz)

            return raiz
        if username < raiz.username:
            raiz.fesquerdo = self.inserir(username, cartao, raiz.fesquerdo)
        if username > raiz.username:
            raiz.fdireito = self.inserir(username, cartao, raiz.fdireito)

        raiz.altura = 1 + max(getaltura(raiz.fesquerdo), getaltura(raiz.fdireito))
        # Efetuar rotacoes
        fe = getfe(raiz)
        if fe > 1:
            if getfe(raiz.fesquerdo) > 0:
                return rotacaoDD(raiz)
            else:
                raiz.fesquerdo = rotacaoEE(raiz.fesquerdo)
                return rotacaoDD(raiz)
        elif fe < -1:
            if getfe(raiz.fdireito) < 0:
                return rotacaoEE(raiz)
            else:
                raiz.fdireito = rotacaoDD(raiz.fdireito)
                return rotacaoEE(raiz)

        return raiz

    def consulta(self, username, raiz):
        if raiz.fesquerdo:
            if self.consulta(username, raiz.fesquerdo):
                return True
        if raiz.username == username:
            return True
        if raiz.fdireito:
            if self.consulta(username, raiz.fdireito):
                return True

    def listagem(self, lista, raiz):
        if raiz.fesquerdo:
            self.listagem(lista, raiz.fesquerdo)
        lista.append(raiz)
        if raiz.fdireito:
            self.listagem(lista, raiz.fdireito)


def lerinput(arvore, n, insercoes):
    raiz = None
    i = 0
    linha = ["ACRESCENTA", random.randint(1,int(n*insercoes)),random.randint(1,10000),random.randint(1,1000),raiz]
    while i != n:
        if i == n*insercoes:
            linha = ["CONSULTA", random.randint(1,int(n*insercoes))]

        if linha[0] == "ACRESCENTA":
            raiz = arvore.inserir(linha[1], [linha[2], linha[3]], raiz)
        elif linha[0] == "CONSULTA":
            if i == int(n*(1-insercoes)):
                linha=["FIM"]
            else:
                if not raiz:
                    return
                else:
                    aux = False
                    aux = arvore.consulta(linha[1], raiz)
                    if aux:
                        return
                    else:
                        return
        elif linha[0] == "LISTAGEM":
            if not raiz:
                print("FIM")
            else:
                lista = []
                arvore.listagem(lista, raiz)
                for no in lista:
                    print(no.username, end=" ")
                    for i in range(len(no.cartoes)):
                        if i == len(no.cartoes) - 1:
                            print(str(no.cartoes[i][0]) + " " + str(no.cartoes[i][1]))
                        else:
                            print(str(no.cartoes[i][0]) + " " + str(no.cartoes[i][1]), end=" ")
                print("FIM")
        elif linha[0] == "APAGA":
            print("LISTAGEM APAGADA")
            raiz = None
        elif linha[0] == "FIM":
            break
        i+=1

def main():
    arvore = ArvoreAVL()
    insercoes = 0.1
    for i in range(15000,50001,5000):
        start = time.time()
        lerinput(arvore, i, insercoes)
        end = time.time()
        print(end-start)


if __name__ == "__main__":
    main()
