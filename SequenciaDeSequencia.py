caso = 1

while True:
    try:
        n = int(input())
    except EOFError:
        break

    # Inicializa a sequência com o primeiro elemento
    sequencia = [0]

    # Constrói a sequência
    for i in range(1, n + 1):
        for _ in range(i):
            sequencia.append(i)
            
    numero_termo = 'numero' if len(sequencia) == 1 else 'numeros'

    print(f"Caso {caso}: {len(sequencia)} {numero_termo}")
    print(" ".join(map(str, sequencia)))
    print()
    
    caso += 1
