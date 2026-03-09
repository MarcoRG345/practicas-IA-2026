

class Problema(object):

    def __init__(self, inicial):
        self.inicial = inicial
        self.acciones = ['up', 'down', 'right', 'left']
        self.final = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', 'e']]
    
    def es_meta(self, configuarcion):
        return configuarcion == self.final
    
    def resultado(self, estado, accion):

        for i in range(len(estado)):
            for j in range(len(estado[0])):
                if estado[i][j] == 'e':
                    x = i
                    y = j
        
        nuevo = [fila[:] for fila in estado]

        if accion == 'up' and x > 0:
            nuevo[x][y], nuevo[x-1][y] = nuevo[x-1][y], nuevo[x][y]
        if accion == 'down' and x < 2:
            nuevo[x][y], nuevo[x+1][y] = nuevo[x+1][y], nuevo[x][y]
        if accion == 'left' and y > 0:
            nuevo[x][y], nuevo[x][y-1] = nuevo[x][y-1], nuevo[x][y]
        if accion == 'right' and y < 2:
            nuevo[x][y], nuevo[x][y+1] = nuevo[x][y+1], nuevo[x][y]

        return nuevo