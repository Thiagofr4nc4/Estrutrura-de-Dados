class Lista:
    def __init__(self, nmaxelementos):
        self.dados = [0] * nmaxelementos
        self.nelementos = 0
    
    def duplicaComDobro(self):
        if (self.nelementos == 0) or ((self.nelementos * 2 ) > len(self.dados)):
            return False
        for i in range(self.nelementos):
            self.dados[self.nelementos+1] = self.dados[i]*2
        self.nelementos *=2 
            