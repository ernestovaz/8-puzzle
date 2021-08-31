from collections import deque
from queue import PriorityQueue
from operator import itemgetter, attrgetter


ESQUERDA = -1
DIREITA = 1
ABAIXO = 3
ACIMA = -3
OBJETIVO = "12345678_"


def calc_manhattan ( estado : str ) :
    """
	Recebe um estado (string), retorna a distancia Manhattan correspondente a esse estado (inteiro), em relacao ao objetivo
	"""
    tamanho = len(estado)
    numeros = estado
    
    distancia = 0

    for i in range (tamanho):
        if numeros[i] != OBJETIVO[i]:
            if numeros[i] == '_':
                n = 9
                print ("ENTROU")
            else:
                n = int(numeros[i])
           
            print (numeros)
            print(i, numeros[i])
            print (type(numeros[i]))

            soma = abs (i%3 - (n-1)%3)
            resto = abs (i//3 - (n-1)//3)
            distancia += soma + resto
            
    return distancia


def calc_hamming(estado):
	"""
	Recebe um estado (string), retorna a distancia de Hamming correspondente a esse estado (inteiro), em relacao ao objetivo 
	"""
	assert len(estado) == len(OBJETIVO) #por hipotese a string de estado e string objetivo sao de mesmo tamanho
	chars_diff = 0

	for i in range(len(estado)):
		if estado[i] != OBJETIVO[i]:
			chars_diff += 1
	
	return chars_diff


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
                if idx != 3 and idx != 6: #se espaço vazio em pos. 3 ou 6, não pode se mover para esquerda
                    sucessores.append(('esquerda',moveEstado(estado,idx,ESQUERDA)))
                if idx > 2:
                    sucessores.append(('acima',moveEstado(estado,idx,ACIMA)))
            if idx < 8:
                if idx != 2 and idx != 5: #se espaço vazio em pos. 2 ou 5, não pode se mover para direita
                    sucessores.append(('direita',moveEstado(estado,idx,DIREITA)))
                if idx < 6:
                    sucessores.append(('abaixo',moveEstado(estado,idx,ABAIXO)))
    return sucessores


# Exercício 2
class Nodo:
    def __init__(self, estado: str, pai, acao: str, custo: int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        self.g = 0
        self.h = 0

    def setH(self, h):
        self.h = h

    def setG(self,g):
        self.g= g



    def __str__(self):
        return "Estado=" + str(self.estado) + ", Pai = {" + str(self.pai) + "}"


# Exercício 3
def expande (nodo : Nodo):
    sucessores = sucessor(nodo.estado)
    expandidos = []
    for succ in sucessores:
        expandidos.append(Nodo(succ[1], nodo, succ[0], nodo.custo+1))
    return expandidos


def devolveAcoes(nodo : Nodo): # recebe nodo objetivo e retorna as ações tomadas para chegar a ele, deve ser útil para todas buscas
    n = nodo
    acoes = []
    while n.pai is not None:
        acoes.insert(0,n.acao)
        n = n.pai
    return acoes




def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com 
    h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    g_value = 0 #implementar o calculo de distancia ate a origem
    
    h_value = calc_hamming(estado) #valor da heuristica

    f_value = g_value + h_value

    if estado == "":
        return []

    X = set()                               # conjunto, diminuiu muito o tempo de execução 
    F = deque([Nodo(estado,None,"",0)])     #aqui a estrutura deque será usada como fila (append= push, popleft= pop front)
    while len(F):
        v = F.popleft()
        if v.estado == OBJETIVO:
            print("achou")
            return devolveAcoes(v)
            
        elif v.estado not in X: 
            X.add(v.estado)
            #v.h = calc_hamming(v.estado)
            #v.setH(calc_hamming(v.estado))
            expandido = expande(v)
            
            for nodo in expandido:
                nodo.setH(calc_hamming(v.estado))

            sorted(expandido,  key = lambda nodo: nodo.h, reverse = True) ##
            
            for nodo in expandido: 
                print(nodo, nodo.h)
                F.append(nodo)
                
    return None
    

#print ("pulos necessarios", calc_manhattan ('1234567_8'))
#noUM = Nodo('Nodo 0', '2_3541687', '', 0)
#noUM = Nodo ('2_3541687', None, None,0)
basico = '1234567_8'
astar_hamming(basico)
#print (expande(noUM))
#print (sucessor(noUM.estado))
#expandido = expande (noUM)
#print(type (expandido))

#print (sorted(expandido,  key = lambda nodo: nodo.estado))

'''
exp = (sorted(expandido,  key = lambda nodo: nodo.estado))
list_orden = []


for nodo in exp:    
    print(nodo)
    c_h = calc_hamming(nodo.estado)
    list_orden.append ((nodo,c_h)) #insere nodo e valor h(v)
'''
#print ((sorted (list_orden, key = itemgetter(1)))) ##ordena lista