from pprint import pprint

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j]['pontuacao'] < lista[min_idx]['pontuacao']:
                min_idx = j

        lista[i], lista[min_idx] = lista[min_idx], lista[i]

jogadores = [
    {'nome': 'Jogador 1', 'pontuacao': 150},
    {'nome': 'Jogador 2', 'pontuacao': 50},
    {'nome': 'Jogador 3', 'pontuacao': 200},
    {'nome': 'Jogador 4', 'pontuacao': 100},
    {'nome': 'Jogador 5', 'pontuacao': 100},
    {'nome': 'Jogador 6', 'pontuacao': 120},
    {'nome': 'Jogador 7', 'pontuacao': 110},
    {'nome': 'Jogador 8', 'pontuacao': 105},
    {'nome': 'Jogador 9', 'pontuacao': 300},
    {'nome': 'Jogador 10', 'pontuacao': 200}
]

selection_sort(jogadores)
pprint(jogadores)