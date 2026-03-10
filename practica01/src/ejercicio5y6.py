import numpy as np
from Problema import Problema
from Nodo import Nodo, expandir

#cola de prioridad
class PriorityQueue:
    def __init__(self):
        self.queue = [] #cola vacia
    def isEmpty(self):
        return self.queue == [] #revisamos que sea vacía
    def push(self, element):
        self.queue.append(element) #agregamos un nodo al final sin ordenar
    def pop(self):
        #creamos una lista con todos los valores f de los nodos y encontramos el indice del menor
        min_index = np.argmin([n.f for n in self.queue])
        #guardamos el nodo con menor f y lo borramos de la cola
        return self.queue.pop(min_index)

#Heurística Manhattan
#Posición goal de cada pieza: pieza -> (fila, columna)
GOAL_POS = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '7': (2, 0), '8': (2, 1), 'e': (2, 2),
}

def manhattan(estado):
    #Suma de distancias Manhattan de cada pieza a su posición final
    total = 0 #aqui acumulamos la distancia
    #con i, j recorremos filas y columnas
    for i in range(3):
        for j in range(3):
            pieza = estado[i][j] #guardamos la que está en esta posición
            if pieza != 'e': #saltamos espacios vacíos
                gi, gj = GOAL_POS[pieza] #buscamos en que lugar debería estar en el resultado final
                total += abs(i - gi) + abs(j - gj) #calculamos los movimientos que le faltan
    return total

#A* pesado
def aestrella_pesado(problema, w):
    root = Nodo(problema.inicial)
    root.g = 0 #no ha dado ningun paso
    root.f = w * manhattan(problema.inicial)
    alcanzados = {tuple(map(tuple, problema.inicial)): root.f}
    frontera = PriorityQueue() #creamos frontera como cola de prioridad
    frontera.push(root) #nodo inicial
    expandidos = 0 #inicializamos

    #mientras haya nodos por explorar saco el de menor valor
    while not frontera.isEmpty():
        nodo = frontera.pop()
        #si el estado actual es el tablero final ent encontramos la solución y regresamos cuantos nodos expandimos
        if problema.es_meta(nodo.estado):
            return expandidos
        #generamos todos los movimientos posibles desde el nodo actual y contamos cada uno como nodo expandido
        for hijo in expandir(problema, nodo):
            expandidos += 1
            hijo.g = nodo.g + 1 #costo uniforme por paso
            hijo.f = hijo.g + w * manhattan(hijo.estado) #f = g + w*h
            estado_hash = tuple(map(tuple, hijo.estado))
            #solo agrega el nodo a la frontera si no fue visitado o encontramos un camino más corto asi no exploramos caminos innecesarios.
            if estado_hash not in alcanzados or hijo.f < alcanzados[estado_hash]:
                alcanzados[estado_hash] = hijo.f
                frontera.push(hijo)
    return None  #no encontró solución

def main():
    #estado inicial del ejercicio 5
    puzzle = [['5', '4', '2'],
              ['3', '1', '7'],
              ['e', '6', '8']]
    #EJERCICIO 6
    problema = Problema(puzzle)
    pesos = [0, 0.8, 1]
    print("A* Pesado - Heurística Manhattan")
    print("Peso (w) - Nodos expandidos")
    for w in pesos:
        nodos = aestrella_pesado(problema, w)
        print("w=" + str(w) + " -> " + str(nodos) + " nodos")
    print("w=0 -> ignora heurística, explora más nodos")
    print("w=0.8 -> balance entre optimización y velocidad")
    print("w=1 -> A* clásico, usa la heurística al máximo")

main()