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
                sucessores.append((ESQUERDA,moveEstado(estado,idx,ESQUERDA)))
                if idx > 2:
                    sucessores.append((ACIMA,moveEstado(estado,idx,ACIMA)))
            if idx < 8:
                sucessores.append((DIREITA,moveEstado(estado,idx,DIREITA)))
                if idx < 6:
                    sucessores.append((ABAIXO,moveEstado(estado,idx,ABAIXO)))
    return sucessores
