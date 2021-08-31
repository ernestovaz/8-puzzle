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


print ("pulos necessarios", calc_manhattan ('1234567_8'))