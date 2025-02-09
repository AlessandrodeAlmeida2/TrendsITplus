import sys
input = sys.stdin.read
dados = input().split()

N = int(dados[0])
valores = [int(dados[i]) for i in range(1, N + 1)]
    
pares = sorted([x for x in valores if x % 2 == 0])
impares = sorted([x for x in valores if x % 2 != 0], reverse=True)

for valor in pares + impares:
    print(valor)
