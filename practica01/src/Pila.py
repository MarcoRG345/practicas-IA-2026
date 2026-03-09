

class Pila(object):

    def __init__(self):
        self.pila = []
    
    def isEmpty(self):
        return self.pila == []

    def push(self, elem):
        self.pila.append(elem)
    
    def pop(self):
        last = self.pila[-1]
        del self.pila[-1]
        return last
    
    def top(self):
        return self.pila[-1]
    
    def __str__(self):
        return ' '.join([str(q) for q in self.pila])

