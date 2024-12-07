def busca_linear(contatos, nome_busca):
    for contato in contatos:
        if contato['nome'] == nome_busca:
            return contato['telefone']
    return "Contato não encontrado"

contatos = [
    {'nome': 'Ana', 'telefone': '5463-7890'},
    {'nome': 'Bruno', 'telefone': '9876-3210'},
    {'nome': 'Carla', 'telefone': '5555-4567'},
    {'nome': 'Vitor', 'telefone': '1111-2222'}
]

nome_buscado = "Vitor"
telefone = busca_linear(contatos, nome_buscado)
print(telefone)