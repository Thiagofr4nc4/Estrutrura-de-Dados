class Lista:
    def __init__(self, nmaxelementos):
        self.dados = [0] * nmaxelementos
        self.nelementos = 0

    def retornarMenor(self):
        if self.nelementos == 0:
            return False, -1
        
        menor = self.dados[0]
        
        for i in range(1, self.nelementos):
            if (self.dados[i] < menor):
                menor = self.dados[i]
        return True, menor
    
    
