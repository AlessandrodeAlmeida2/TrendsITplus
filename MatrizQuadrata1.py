def construir_matriz(n):
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matriz[i][j] = min(i, j, n- i - 1, n - j - 1) + 1
    return matriz       
            
def imprimir(matriz):
    for linha in matriz:
        print(" ".join(f"{num:3}" for num in linha))
    print()

while True:
    n = int(input())
    if n == 0:
        break
    else:
        matriz = construir_matriz(n)
        imprimir(matriz)
