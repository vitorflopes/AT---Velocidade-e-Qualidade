class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no, chave):
        if no is None:
            return No(chave)
        if chave < no.chave:
            no.esquerda = self._inserir_recursivo(no.esquerda, chave)
        else:
            no.direita = self._inserir_recursivo(no.direita, chave)
        return no


    def encontrar_minimo(self):
        if self.raiz is None:
            return None
        no_atual = self.raiz
        while no_atual.esquerda:
            no_atual = no_atual.esquerda
        return no_atual.chave

    def encontrar_maximo(self):
        if self.raiz is None:
            return None
        no_atual = self.raiz
        while no_atual.direita:
            no_atual = no_atual.direita
        return no_atual.chave

notas = [85, 70, 95, 60, 75, 90, 100]
arvore = Arvore()
for nota in notas:
    arvore.inserir(nota)

nota_minima = arvore.encontrar_minimo()
nota_maxima = arvore.encontrar_maximo()

print(f"Nota mínima: {nota_minima}")
print(f"Nota máxima: {nota_maxima}")