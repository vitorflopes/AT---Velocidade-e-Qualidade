class FilaChamados:
    def __init__(self):
        self.chamados = []

    def adicionar(self, chamado):
        self.chamados.append(chamado)

    def remover(self):
        if self.chamados:
            return self.chamados.pop(0)
        else:
            return None

fila = FilaChamados()
fila.adicionar("Chamado 1")
fila.adicionar("Chamado 2")
fila.adicionar("Chamado 3")

print(fila.remover())
print(fila.remover())
