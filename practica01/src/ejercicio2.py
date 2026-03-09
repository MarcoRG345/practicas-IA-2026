from Problema import Problema
from Pila import Pila
from Nodo import Nodo
from Nodo import expandir

def make_problem(puzzle_array):
    return Problema(puzzle_array)
        

def depth_search(problema):

    # Añade el nodo inicial como alcanzado y a la frontera (crea la pila).
    root = Nodo(problema.inicial)
    alcanzados = {tuple(map(tuple, problema.inicial)): root}
    frontera = Pila()
    frontera.push(root)

    # Cuenta el numero de nodos expandidos.
    expandidos = 0

    # Mientras la frontera esté vacía.
    while not frontera.isEmpty():
        # Saca el nodo del tope de la pila
        nodo = frontera.pop()

        # Revisa si este nodo es terminal, si lo es termina
        if problema.es_meta(nodo.estado):
            return(f"Resultado DFS: {nodo} expandidos = {expandidos}")

        # En otro caso, expande el nodo actual
        for hijo in expandir(problema, nodo):
            expandidos+=1
            estado_hash = tuple(map(tuple, hijo.estado))

            # Guarda los nodos hijos en la frontera.
            if estado_hash not in alcanzados:
                alcanzados[estado_hash] = hijo
                frontera.push(hijo)

    return None 

def main():
    puzzle_array = [['1','e','2'], ['6','3','4'], ['7','5','8']]
    print(depth_search(make_problem(puzzle_array)))

main()



         
    




