n = int(input())

for _ in range(n):
    m = int(input())
    produtos = {}
    for _ in range(m):
        item, preco = input().split()
        produtos[item] = float(preco)
    
    p = int(input())
    total = 0.0
    for _ in range(p):
        item, quantidade = input().split()
        quantidade = int(quantidade)
        total += produtos[item] * quantidade
   
    print(f"R$ {total:.2f}")
