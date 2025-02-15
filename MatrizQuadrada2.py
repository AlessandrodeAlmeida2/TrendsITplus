def construir_matriz(n):
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
                matriz[i][j] = abs(i - j) + 1
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{num:3}" for num in linha))
    print()

while True:
    N = int(input())
    if N == 0:
        break
    matriz = construir_matriz(N)
    imprimir_matriz(matriz)