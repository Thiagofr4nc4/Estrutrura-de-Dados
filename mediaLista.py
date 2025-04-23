class Lista:
    def __init__(self, nmaxelementos):
        self.dados = [0] * nmaxelementos
        self.nelementos = 0

    def mediaLista(self):
        if self.nelementos == 0:
            return 0
        soma = 0
        for i in range(self.nelementos):
            soma += self.dados[i]
        return soma / self.nelementos

lista = Lista(3)
lista.dados = [10, 10, 10]
lista.nelementos = 3
print(lista.mediaLista())
