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
                sucessores.append(('esquerda',moveEstado(estado,idx,ESQUERDA)))
                if idx > 2:
                    sucessores.append(('acima',moveEstado(estado,idx,ACIMA)))
            if idx < 8:
                sucessores.append(('direita',moveEstado(estado,idx,DIREITA)))
                if idx < 6:
                    sucessores.append(('abaixo',moveEstado(estado,idx,ABAIXO)))
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
        return sucessor(self.estado)

    def expandeNo () :
        return sucessor(self.estado)


# Exercício 3
def expande (no : Nodo):
    return sucessor(no)

#Areateste
noUM = Nodo('Nodo 0', '2_3541687', '', 0)
print (sucessor(noUM.estado))
