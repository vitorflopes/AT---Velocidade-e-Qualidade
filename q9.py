
class Perfil:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

def criar_hashtable(lista_perfis):
    hashtable = {}
    for perfil in lista_perfis:
        hashtable[perfil.nome] = perfil
    return hashtable

def buscar_perfil(hashtable, nome_usuario):
    if nome_usuario in hashtable:
        return hashtable[nome_usuario]
    else:
        return None

perfis = [
    Perfil("joaozinho", 20, "São Paulo"),
    Perfil("mariazinha", 25, "Rio de Janeiro"),
    Perfil("pedrinho", 30, "Belo Horizonte")
]

hashtable = criar_hashtable(perfis)

perfil_buscado = buscar_perfil(hashtable, "mariazinha")

if perfil_buscado:
    print(f"Nome: {perfil_buscado.nome}, Idade: {perfil_buscado.idade}, Cidade: {perfil_buscado.cidade}")
else:
    print("Perfil não encontrado.")