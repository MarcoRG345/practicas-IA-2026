from Nodo import Nodo
from Nodo import expandir
from Problema import Problema
from Cola import Cola


def make_problem(puzzle_array):
    return Problema(puzzle_array)
        

def breath_search(problema):

    # Añade el nodo inicial como alcanzado y a la frontera (crea la pila).
    root = Nodo(problema.inicial)
    alcanzados = {tuple(map(tuple, problema.inicial)): root}
    frontera = Cola()
    frontera.push(root)

    # Cuenta el numero de nodos expandidos.
    expandidos = 0

    # Mientras la frontera esté vacía.
    while not frontera.isEmpty():
        # Saca el nodo primero de la cola
        nodo = frontera.pop()

        # Revisa si este nodo es terminal, si lo es termina
        if problema.es_meta(nodo.estado):
            return(f"Resultado BFS: {nodo} expandidos = {expandidos}")

        # En otro caso, expande el nodo
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
    print(breath_search(make_problem(puzzle_array)))

main()
