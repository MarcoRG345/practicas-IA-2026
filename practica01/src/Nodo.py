from Problema import Problema

class Nodo(object):
    
    def __init__(self, configuarcion):
        self.estado = configuarcion # estado actual del tablero.
        self.padre = None # objeto Nodo, de donde viene.
        self.accion = None # para donde se mueve.
    
    def __str__(self):
        if self.padre == None:
            return "Estado: {}".format(self.estado)
        else:
            return "Estado: {}, Accion: {}, Padre: {}".format(self.estado,self.accion,self.padre.estado)


def expandir(problema, nodo):
    estado = nodo.estado
    for accion_generada in problema.acciones:

        nuevo_tablero = problema.resultado(estado, accion_generada)
        nuevo_nodo = Nodo(nuevo_tablero)
        nuevo_nodo.padre = nodo
        nuevo_nodo.accion = accion_generada 

        yield nuevo_nodo
    

