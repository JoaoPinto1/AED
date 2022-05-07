class No:
    def __init__(self, username):
        self.username = username
        self.cartoes = []
        self.fesquerdo = None
        self.fdireito = None

    def getfe(self):
        if self.fesquerdo is None:
            auxesquerdo = 0
        else:
            auxesquerdo = self.fesquerdo.getaltura()
        if self.fdireito is None:
            auxdireito = 0
        else:
            auxdireito = self.fdireito.getaltura()
        return auxesquerdo - auxdireito

    def getaltura(self):
        if self.fesquerdo is None:
            auxesquerdo = 0
        else:
            auxesquerdo = self.fesquerdo.getaltura()
        if self.fdireito is None:
            auxdireito = 0
        else:
            auxdireito = self.fdireito.getaltura()
        return 1 + max(auxesquerdo, auxdireito)

    def rotacaoDD(self):
        self.username = self.fesquerdo.username
        self.cartoes = self.fesquerdo.cartoes
        self.fesquerdo.username = self.username
        self.fesquerdo.cartoes = self.cartoes
        aux = self.fdireito
        self.fesquerdo = self.fesquerdo.fesquerdo
        self.fdireito = self.fesquerdo
        self.fdireito.fesquerdo = self.fdireito.fdireito
        self.fdireito.fdireito = aux

    def rotacaoEE(self):
        self.username = self.fdireito.username
        self.cartoes = self.fdireito.cartoes
        self.fesquerdo.username = self.username
        self.fesquerdo.cartoes = self.cartoes
        aux = self.fesquerdo
        self.fesquerdo = self.fdireito
        self.fdireito = self.fesquerdo.fesquerdo
        self.fesquerdo.fesquerdo = aux
        self.fesquerdo.fdireito = self.fesquerdo.fesquerdo

    def rotacaoED(self):
        self.fesquerdo.rotacaoEE()
        self.rotacaoDD()

    def rotacaoDE(self):
        self.fdireito.rotacaoDD()
        self.rotacaoEE()

    def addcartao(self, cartao):
        for card in self.cartoes:
            if cartao[0] == card[0]:
                card[1] = cartao[1]
                return 0
        self.cartoes.append(cartao)
        return 1

    def inserir(self, username, cartao):
        if username == self.username:
            aux = self.addcartao(cartao)
            if aux == 0:
                print("CARTAO ATUALIZADO")
            if aux == 1:
                print("NOVO CARTAO INSERIDO")
        elif username < self.username:
            if self.fesquerdo is None:
                self.fesquerdo = No(username)
                self.addcartao(cartao)
                print("NOVO UTILIZADOR CRIADO")
            else:
                self.fesquerdo.inserir(username, cartao)
        elif username > self.username:
            if self.fdireito is None:
                self.fdireito = No(username)
                self.addcartao(cartao)
                print("NOVO UTILIZADOR CRIADO")
            else:
                self.fdireito.inserir(username, cartao)
        # Efetuar rotacoes
        fe = self.getfe()
        if fe > 1:
            if self.fesquerdo.getfe() > 0:
                self.rotacaoDD()
            else:
                self.rotacaoED()
        elif fe < -1:
            if self.fdireito.getfe() < 0:
                self.rotacaoEE()
            else:
                self.rotacaoDE()

    def consulta(self, username):
        if self.fesquerdo is not None:
            self.fesquerdo.consulta()
        if self.username == username:
            for cartao in self.cartoes:
                print(str(cartao[0])+" "+ str(cartao[1]))
            return True
        if self.fdireito is not None:
            self.fdireito.consulta()

    def listagem(self, lista):
        if self.fesquerdo is not None:
            self.fesquerdo.listagem()
        lista.append(self)
        if self.fdireito is not None:
            self.fdireito.listagem()

    def apaga(self):
        if self.fesquerdo is not None:
            self.fesquerdo.listagem()
        if self.fdireito is not None:
            self.fdireito.listagem()
        del self


def lerinput(raiz):
    while True:
        linha = input().split()
        if linha[0] == "ACRESCENTA":
            raiz.inserir(linha[1], [linha[2], linha[3]])
        elif linha[0] == "CONSULTA":
            aux = raiz.consulta(linha[1])
            if not aux:
                print("NAO ENCONTRADO")
        elif linha[0] == "LISTAGEM":
            lista = []
            raiz.listagem(lista)
            lista.sort()
            for no in lista:
                for cartao in no.cartoes:
                    print(no.username + " " + str(cartao[0]) + " " + str(cartao[1]))
            print("FIM")
        elif linha[0] == "APAGA":
            raiz.apaga()
            print("LISTAGEM APAGADA")
        elif linha[0] == "FIM":
            break

