class Lista:
    def __init__(self, nmaxelementos):
        self.dados = [0] * nmaxelementos
        self.nelementos = 0

    def retornarImpares(self):
        if self.nelementos == 0:
            return False, -1
        
        impares = 0 
        for i in range(self.nelementos):
            if(self.dados[i] % 2 != 0):
                impares += 1
            
        return impares
