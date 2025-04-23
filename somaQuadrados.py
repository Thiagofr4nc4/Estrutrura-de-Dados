class Lista:
    def __init__(self, nmaxelementos):
        self.dados = [0] * nmaxelementos
        self.nelementos = 0

    def somaQuadrados(self):
        if (self.nelementos == 0):
            return 0
        
        soma = 0

        for i in range(self.nelementos):
            soma += (self.dados[i] ** 2)
        return soma 
            