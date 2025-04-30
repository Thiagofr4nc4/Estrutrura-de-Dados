class Lista:
    def __init__(self, nmaxelementos):
        self.dados = [0] * nmaxelementos
        self.nelementos = 0
    
    def duplicaComDobro(self):
        if (self.nelementos == 0) or ((self.nelementos * 2 ) > len(self.dados)):
            return False
        for i in range(self.nelementos):
            self.dados[self.nelementos+i] = self.dados[i]*2
        self.nelementos *=2 
        

lista = Lista(6)
lista.dados[0] = 1
lista.dados[1] = 2
lista.dados[2] = 3
lista.nelementos = 3
lista.duplicaComDobro()
print(lista.nelementos)
print(lista.dados)