class Lista:
    def __init__(self, nmaxelementos):
        self.dados = [0] * nmaxelementos
        self.nelementos = 0

    def returnarMaior(self):
        maior = self.dados[0]
        if self.nelementos == 0:
            return False, -1
        else:
            for i in range(1, self.nelementos):
                if(maior < self.dados[i]):
                    maior = self.dados[i]
        return True, maior
 
lista = Lista(5)
lista.dados = [3, 1, 4, 2, 5]
lista.nelementos = 5

print(lista.returnarMaior())