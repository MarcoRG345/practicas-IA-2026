# Algoritmos basados en agentes de Inteligencia Artificial.
Practica 1 


Correr el archivo con: python ejercicio5y6.py
Ejercicio 5 - A* Pesado con Heurística Manhattan
Se implementó el algoritmo de A* pesado para resolver el 8-puzzle dado el estado inicial con el 5 en la esquina superior izquierda y el espacio vacío en la esquina inferior izquierda
Usa la heurística de distancia Manhattan, que calcula cuántos movimientos le faltan a cada pieza para llegar a su posición en el
estado final, sumando las diferencias de filas y columnas de cada pieza. La función de evaluación combina el costo real del camino recorrido g(n) con la heurística multiplicada por un peso w, teniendo f(n) = g(n) + w * h(n). Y tenemos que el peso w controla cuánto influye la heurística en la búsqueda

Ejercicio 6 - Comparación de nodos expandidos
Se corre el algoritmo con tres pesos distintos.
Con w=0 el algoritmo ignora completamente la heurística y se comporta como búsqueda por costo uniforme (Dijkstra), expandiendo 480108 nodos por este paso tarda como 5 min en terminar.

Con w=0.8 encuentra un balance entre el costo recorrido y la heurística, reduciendo los nodos a 14472.

Con w=1, que corresponde al A* clásico, dodne se aprovecha al máximo la heurística Manhattan así siendo el más eficiente con 6976 nodos expandidos