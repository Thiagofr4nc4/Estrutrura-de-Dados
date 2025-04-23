class Lista:
    def __init__(self, nmaxelementos):
        self.dados = [0] * nmaxelementos
        self.nelementos = 0


    def removeX(self, x):
        i = 0
        while i < self.nelementos:
            if self.dados[i] == x:
                self.dados[i] = self.dados[self.nelementos-1]
                self.dados[self.nelementos-1] = 0
                self.nelementos -= 1
            else:
                i += 1
        
lista = Lista(10)
lista.dados = [2,2,2,5,2,6,2,10,2,8]
lista.nelementos = 10
print(lista.dados)
lista.removeX(2)

print(lista.dados)