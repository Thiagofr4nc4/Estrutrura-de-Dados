class Lista:
    def __init__(self, nmaxelementos):
        self.dados = [0] * nmaxelementos
        self.nelementos = 0

    def removeIesimo(self, i):
        if i < 0 or i >= self.nelementos:
            return False
        
        self.dados[i] = self.dados[self.nelementos-1]
        self.nelementos -=1