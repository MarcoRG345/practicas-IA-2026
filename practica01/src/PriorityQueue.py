
class PriorityQueue(object):
    """Clase de una cola de prioridad en los problemas de búsqueda."""
    def __init__(self,f=lambda x: 1):
        self.queue = []
        self.f = f
  
    def __str__(self):
        return ' '.join([str(q) for q in self.queue])
  
    def isEmpty(self):
        return self.queue == []
  
    def push(self, element):
        """Agrega elementos a la pila"""
        self.queue.append(element)
  
    def pop(self):
        """Saca de la pila el elemento con mayor valor f."""
        #Encuentra el elemento máximo en base al costo
        min_element = np.argmin([element.f for element in self.queue])
        #Guarda el elemento máximo
        item = self.queue[min_element]
        #Borra este elemento de la cola
        del self.queue[min_element]
    
        return item