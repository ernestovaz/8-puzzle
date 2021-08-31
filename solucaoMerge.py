ESQUERDA = -1
DIREITA = 1
ABAIXO = 3
ACIMA = -3

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

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, pai, estado, acao: str, custo: int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        #raise NotImplementedError

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


def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    #raise NotImplementedError

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


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    #raise NotImplementedError

    return sucessor(no)


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError



#Areateste
noUM = Nodo('Nodo 0', '2_3541687', '', 0)
print (sucessor(noUM.estado))