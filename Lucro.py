while True:
    try:
        n = int(input())
        custo_por_dia = int(input())
        receitas = [int(input()) for _ in range(n)]
        
        max_lucro = 0
        
        for i in range(n):
            for j in range(i, n):
                lucro = sum(receitas[i:j+1]) - (j - i + 1) * custo_por_dia
                max_lucro = max(max_lucro, lucro)
        
        print(max_lucro)
    except EOFError:
        break
