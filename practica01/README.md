# Algoritmos de busqueda.
Practica 1 



Ejercicio 4. 
la variable "expandidos" indica el numero de nuevos nodos hijos generados en la frontera. En el caso de BFS y DFS hay un margen
de diferencia en el numero de nodos que se expandieron; DFS: 437,328, contra BFS: 30,340 nodos asi como el tiempo
de ejecucion el nodo solucion. Esto por proposicion, a pesar de tener las mismas complejidades exponenciales, BFS en un ambiente finito
y con costo constante (en este caso no se tomo en cuenta por lo que c = 0) nos da la solucion optima, contrario a DFS donde si hay un subarbol
lo suficientemente grande, la explotacion se relentiza, es decir, no acaba hasta llegar al nodo mas profundo por cada d. Contrario a BFS,
recorremos por nivel, y en este caso solo tenemos 4 acciones posibles por verificar, para el nodo solucion econtrado en el nivel se dentra de ahi.


Correr el archivo con: python ejercicio5y6.python

Ejercicio 5 - A* Pesado con Heurística Manhattan
Se implementó el algoritmo de A* pesado para resolver el 8-puzzle dado el estado inicial con el 5 en la esquina superior izquierda y el espacio vacío en la esquina inferior izquierda
Usa la heurística de distancia Manhattan, que calcula cuántos movimientos le faltan a cada pieza para llegar a su posición en el
estado final, sumando las diferencias de filas y columnas de cada pieza. La función de evaluación combina el costo real del camino recorrido g(n) con la heurística multiplicada por un peso w, teniendo f(n) = g(n) + w * h(n). Y tenemos que el peso w controla cuánto influye la heurística en la búsqueda

Ejercicio 6 - Comparación de nodos expandidos
Se corre el algoritmo con tres pesos distintos.
Con w=0 el algoritmo ignora completamente la heurística y se comporta como búsqueda por costo uniforme (Dijkstra), expandiendo 480108 nodos por este paso tarda como 5 min en terminar.

Con w=0.8 encuentra un balance entre el costo recorrido y la heurística, reduciendo los nodos a 14472.

Con w=1, que corresponde al A* clásico, dodne se aprovecha al máximo la heurística Manhattan así siendo el más eficiente con 6976 nodos expandidos
