class pilha():
    def __init__(self):
        self.lista=[]

    def push(self, valor):
        self.lista.append(valor)

    def pop(self):
        if (not(self.isEmpty())):
            self.lista.pop()
    def isEmpty(self):
        return len(self.lista)==0
    def lenght(self):
        return len (self.lista)
    def peek(self):
        if (not(self.isEmpty())):
            return self.lista [-1]
        
    
