class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no, chave):
        if no is None:
            return No(chave)
        if chave < no.chave:
            no.esquerda = self._inserir_recursivo(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._inserir_recursivo(no.direita, chave)
        return no

    def buscar(self, chave):
        return self._buscar_recursivo(self.raiz, chave)

    def _buscar_recursivo(self, no, chave):
        if no is None or no.chave == chave:
            return no
        if chave < no.chave:
            return self._buscar_recursivo(no.esquerda, chave)
        else:
            return self._buscar_recursivo(no.direita, chave)

precos = [100, 50, 150, 30, 70, 130, 170]
arvore = ArvoreBinariaBusca()
for preco in precos:
    arvore.inserir(preco)

no_encontrado = arvore.buscar(70)
if no_encontrado:
    print("Preço 70 encontrado!")
else:
    print("Preço 70 não encontrado.")