
class Cola(object):

    def __init__(self):
        self.cola = []
    
    def isEmpty(self):
        return self.cola == []
    
    def push(self, elem):
        self.cola.append(elem)
    
    def pop(self):
        return self.cola.pop(0)
    

