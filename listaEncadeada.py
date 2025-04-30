class ListaEncadeada:
    def __init__(self):
        self.prim = None  # Primeiro nó da lista

    def No(self, chave):
        self.chave = chave
        self.prox = None

    def consuta(self, chave):
        p = self.prim
        while (p is not None):
            if(p.chave == chave):
                return True
            p = self.prox
        return False
    
    def inserir(self, chave):
        novo_no = No(chave)
    
        if self.prim is None:  
            self.prim = novo_no
        else:
            p = self.prim
            while p.prox is not None: 
                p = p.prox 
            p.prox = novo_no 
        
    def remover(self, chave):
        if (self.consuta(chave)):
            p = self.consuta(chave)
            q = self.prim

            while (q.prox is not p):
                q = q.prox
            q = q.prox.prox

