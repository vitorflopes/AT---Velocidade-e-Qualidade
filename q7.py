def encontra_duplicatas(lista):
    vistos = {}
    duplicatas = []
    for elemento in lista:
        if elemento in vistos:
            duplicatas.append(elemento)
        else:
            vistos[elemento] = True
    return duplicatas

minha_lista = [1, 2, 3, 2, 4, 5, 1, 6]
duplicatas = encontra_duplicatas(minha_lista)
print(f"Duplicatas: {duplicatas}")