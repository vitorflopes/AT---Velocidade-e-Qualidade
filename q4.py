def busca_binaria(lista, isbn_alvo):
    inicio = 0
    fim = len(lista) - 1
    iteracoes = 0

    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2 
        if lista[meio]['isbn'] == isbn_alvo:
            return meio, iteracoes  
        elif lista[meio]['isbn'] < isbn_alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, iteracoes


livros = [{'isbn': i, 'titulo': f'Livro {i}'} for i in range(100000)]
isbn_buscado = 77777

posicao, iteracoes_binaria = busca_binaria(livros, isbn_buscado)

print(f"Número de iterações (busca binária): {iteracoes_binaria}")

# ---------------------------------------------------------------

iteracoes_linear = 0
for i, livro in enumerate(livros):
    iteracoes_linear += 1
    if livro['isbn'] == isbn_buscado:
        break

print(f"Número de iterações (busca linear): {iteracoes_linear}")