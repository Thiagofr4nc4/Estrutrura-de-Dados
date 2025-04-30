class Lista:
    def __init__(self, nmaxelementos):
        self.dados = [0] * nmaxelementos
        self.nelementos = 0

    def maiorPrimeiro(self):
        if(self.nelementos == 0):
            return False, -1
        
        primeiro = self.dados[0]
        maiores = 0
        for i in range(1, self.nelementos):
            if (primeiro < self.dados[i]):
                maiores += 1
        return True, maiores
    
lista = Lista(5)
lista.dados = [0, 1, 2, 3, 4]
lista.nelementos = 5
print(lista.maiorPrimeiro())
