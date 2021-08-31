from collections import deque
import heapq

ESQUERDA = -1
DIREITA = 1
ABAIXO = 3
ACIMA = -3
OBJETIVO = "12345678_"

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
		
	def __lt__(self, next): #metodo de comparacao entre nodos para criterio de desempate na heapq
		return self.estado < next.estado
		
	def insereNo (self, pai, novoNo):
		pass

	def sucessorNo(estado: str):
		return sucessor(self.estado)

	def expandeNo () :
		return sucessor(self.estado)


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


# Exercício 4
def bfs(estado):
    if estado == "":
        return []
    X = set()                               # conjunto, diminuiu muito o tempo de execução 
    F = deque([Nodo(estado,None,"",0)])     #aqui a estrutura deque será usada como fila (append= push, popleft= pop front)
    while len(F):
        v = F.popleft()
        if v.estado == OBJETIVO:
            return devolveAcoes(v)          
        elif v.estado not in X: 
            X.add(v.estado)
            for nodo in expande(v): F.append(nodo)
    return None

def dfs(estado):
	if estado == "":
		return []
	X = set()
	F = deque([Nodo(estado, None, "", 0)])
	while len(F):
		v = F.pop() #retorna o elemento do topo da pilha (lado direito do deque)
		if v.estado == OBJETIVO:
			return devolveAcoes(v)
		elif v.estado not in X:
			X.add(v.estado)
			for nodo in expande(v): F.append(nodo)
	return None	

def calc_hamming(estado):
	assert len(estado) == len(OBJETIVO) #por hipotese a string de estado e string objetivo sao de mesmo tamanho
	chars_diff = 0

	for i in range(len(estado)):
		if estado[i] != OBJETIVO[i]:
			chars_diff += 1
	
	return chars_diff

def astar_hamming(estado):
	if estado == "":
		return []
	X = set()
	F = [] #inicializando a fila de prioridades
	heapq.heappush(F, (0, Nodo(estado, None, "", 0)))
	while len(F):
		v = heapq.heappop(F)[1] #v recebe o Nodo do par (valor,  Nodo) do topo da lista de prioridades
		if v.estado == OBJETIVO:
			return devolveAcoes(v)
		elif v.estado not in X:
			X.add(v.estado)
			for nodo in expande(v):
				g_value = nodo.custo
				h_value = calc_hamming(nodo.estado) #valor da heuristica
				f_value = g_value + h_value #valor final do nodo na fila de prioridades
				heapq.heappush(F, (f_value, nodo))

	return None

def calc_manhattan(estado):
    manhattan = 0
    for pos,numChar in enumerate(estado):
        if numChar == "_":
            num = 9
        else:                   #variaveis recebem Quociente e Resto da divisão inteira por 3, representando suas coordenadas no plano:
            num = int(numChar)                                                                      # -------------
        qPos,rPos = divmod(pos,3)                                                                   # |0,0|1,0|2,0|    
        qNum,rNum = divmod(num-1,3)                                                                 # ------------- 
        manhattan += abs(qPos-qNum)+abs(rPos-rNum)                                                  # |0,1|1,1|2,1|
    return manhattan                                                                                # -------------
                                                                                                    # |0,2|1,2|2,2|
                                                                                                    # -------------
	

def astar_manhattan(estado):
	if estado == "":
		return []
	X = set()
	F = [] #inicializando a fila de prioridades
	heapq.heappush(F, (0, Nodo(estado, None, "", 0)))
	while len(F):
		v = heapq.heappop(F)[1] #v recebe o Nodo do par (valor,  Nodo) do topo da lista de prioridades
		if v.estado == OBJETIVO:
			return devolveAcoes(v)
		elif v.estado not in X:
			X.add(v.estado)
			for nodo in expande(v):
				g_value = nodo.custo
				h_value = calc_manhattan(nodo.estado) #valor da heuristica
				f_value = g_value + h_value #valor final do nodo na fila de prioridades
				heapq.heappush(F, (f_value, nodo))

	return None
    


#Areateste

noUM = Nodo('Nodo 0', '2_3541687', '', 0)

#print (sucessor(noUM.estado))
##print (bfs("12_463758"))

def mostraPuzzle(estado):
    print("""
    -------
    |"""+str(estado[0])+"|"+str(estado[1])+"|"+str(estado[2])+"""|
    -------
    |"""+str(estado[3])+"|"+str(estado[4])+"|"+str(estado[5])+"""|
    -------
    |"""+str(estado[6])+"|"+str(estado[7])+"|"+str(estado[8])+"""|
    -------""")
