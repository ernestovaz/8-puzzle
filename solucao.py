ESQUERDA = -1
DIREITA = 1
ABAIXO = 3
ACIMA = -3

#função que move peça, dado estado inicial, índice do espaço vazio e direção
def moveEstado(estado: str, idxVazio: int, dir: int):
    proxEstado = []
    idxProx = idxVazio + dir
    for idx,n in enumerate(estado):
        if idx == idxVazio:
            proxEstado.append(estado[idxProx])
        elif idx == idxProx:
            proxEstado.append("_")
        else:
            proxEstado.append(n)
    return "".join(proxEstado)

# Exercício 1
def sucessor(estado: str):
    sucessores = []
    for idx,n in enumerate(estado):
        if n == "_":
            if idx > 0:
                #sucessores.append((ESQUERDA,moveEstado(estado,idx,ESQUERDA)))
                sucessores.append(('ESQUERDA',moveEstado(estado,idx,ESQUERDA)))
                if idx > 2:
                    #sucessores.append((ACIMA,moveEstado(estado,idx,ACIMA)))
                    sucessores.append(('ACIMA',moveEstado(estado,idx,ACIMA)))
            if idx < 8:
                #sucessores.append((DIREITA,moveEstado(estado,idx,DIREITA)))
                sucessores.append(('DIREITA',moveEstado(estado,idx,DIREITA)))
                if idx < 6:
                    #sucessores.append((ABAIXO,moveEstado(estado,idx,ABAIXO)))
                    sucessores.append(('ABAIXO',moveEstado(estado,idx,ABAIXO)))
    return sucessores


# Exercício 2
class Nodo:
    def __init__(self, pai: str , estado, acao: str, custo: int):
        self.pai = pai
        self.estado = estado
        self.acao = acao
        self.custo = custo

    def insereNo (self, pai, novoNo):
        pass

    def sucessorNo(estado: str):
        sucessores = []
        for idx,n in enumerate(estado):
            if n == "_":
                if idx > 0:
                    #sucessores.append((ESQUERDA,moveEstado(estado,idx,ESQUERDA)))
                    sucessores.append(('ESQUERDA',moveEstado(estado,idx,ESQUERDA)))
                    if idx > 2:
                        #sucessores.append((ACIMA,moveEstado(estado,idx,ACIMA)))
                        sucessores.append(('ACIMA',moveEstado(estado,idx,ACIMA)))
                if idx < 8:
                    #sucessores.append((DIREITA,moveEstado(estado,idx,DIREITA)))
                    sucessores.append(('DIREITA',moveEstado(estado,idx,DIREITA)))
                    if idx < 6:
                        #sucessores.append((ABAIXO,moveEstado(estado,idx,ABAIXO)))
                        sucessores.append(('ABAIXO',moveEstado(estado,idx,ABAIXO)))
        return sucessores

    def expandeNo (self) :
        return sucessor(self)


# Exercício 3
def expande (no : Nodo):
    return sucessor(no)

#Areateste
noUM = Nodo('Nodo 0', '2_3541687', '', 0)
print (sucessor(noUM.estado))