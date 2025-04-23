class Lista:
    def __init__(self, nmaxelementos):
        self.dados = [0] * nmaxelementos
        self.nelementos = 0

    def consulta(self, x):
        if self.nelementos == 0: #Se a lista estiver vazia retorna falso
            return False
        for i in range(self.nelementos): #Percorre lista de elementos
            if x == self.dados[i]:  # Compara x no indice i
                return True
        return False # Não achou X
    
    def inserir(self, x):
        if self.nelementos < len(self.dados): #Verifica se há espaço para a inserção
            self.dados[self.nelementos] = x #Vetor na posição do valor de self.nelementos recebe x
            self.nelementos += 1
        else: return False #Caso lista cheia
                    
    def remover(self, x):
        if (self.consulta(x)):
            for i in range(self.nelementos):
                if(self.dados[i] == x):
                    self.dados[i] = self.dados[self.nelementos-1] #Recebe ultimo elemento da lista
                    self.nelementos -= 1
                return True
        else:
            False

