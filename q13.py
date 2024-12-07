def mochila_dinamica(capacidade, pesos, valores):
    n = len(valores)
    tabela = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i-1] <= w:
                tabela[i][w] = max(valores[i-1] + tabela[i-1][w-pesos[i-1]], tabela[i-1][w])
            else:
                tabela[i][w] = tabela[i-1][w]

    return tabela[n][capacidade]

capacidade = 50
pesos = [10, 20, 30]
valores = [60, 100, 120]

valor_maximo = mochila_dinamica(capacidade, pesos, valores)
print(f"Valor máximo: {valor_maximo}")