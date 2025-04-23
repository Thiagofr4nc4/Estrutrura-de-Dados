class Lista:
    def __init__(self, nmaxelementos):
        self.dados = [0] * nmaxelementos
        self.nelementos = 0

    def retirarMaior(self):
        if (self.nelementos == 0):
            return False
        
        indice_maior = 0
        for i in range(1, self.nelementos):
            if(self.dados[i] > self.dados[indice_maior]):
                indice_maior = i
        self.dados[indice_maior] = self.dados[self.nelementos-1]
        self.nelementos -= 1
        return True
        
    
lista = Lista(5)
lista.dados = [10, 60, 30, 40, 50]
lista.nelementos = 5

print(lista.dados)
lista.retirarMaior()
print(lista.dados)
