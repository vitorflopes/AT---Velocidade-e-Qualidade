import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

lista_1000 = [i for i in range(1000, -1,-1)]
lista_10000 = [i for i in range(10000, -1,-1)]


inicio = time.time()
bubble_sort(lista_1000.copy())
fim = time.time()
tempo_1000 = fim - inicio

inicio = time.time()
bubble_sort(lista_10000.copy())
fim = time.time()
tempo_10000 = fim - inicio


print(f"Tempo com 1000 elementos: {tempo_1000:.6f} segundos")
print(f"Tempo com 10000 elementos: {tempo_10000:.6f} segundos")