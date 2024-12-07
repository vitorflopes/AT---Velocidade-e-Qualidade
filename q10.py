class Navegador:
    def __init__(self):
        self.historico_voltar = []
        self.historico_avancar = []
        self.pagina_atual = None

    def visitar_pagina(self, url):
        if self.pagina_atual:
            self.historico_voltar.append(self.pagina_atual)
        self.pagina_atual = url
        self.historico_avancar = []
        print(f"Página atual: {self.pagina_atual}")

    def voltar(self):
        if self.historico_voltar:
            self.historico_avancar.append(self.pagina_atual)
            self.pagina_atual = self.historico_voltar.pop()
            print(f"Página atual: {self.pagina_atual}")
        else:
            print("Não há páginas para voltar.")

    def avancar(self):
        if self.historico_avancar:
            self.historico_voltar.append(self.pagina_atual)
            self.pagina_atual = self.historico_avancar.pop()
            print(f"Página atual: {self.pagina_atual}")
        else:
            print("Não há páginas para avançar.")


navegador = Navegador()
navegador.visitar_pagina("google.com")
navegador.visitar_pagina("youtube.com")
navegador.voltar()
navegador.avancar()