import sys
input = sys.stdin.read
dados = input().split()
    
indice = 0
N = int(dados[indice])
indice += 1

resultados = []

for _ in range(N):
    alunos = int(dados[indice])
    indice += 1

    notas = [int(dados[indice + aluno]) for aluno in range(alunos)]
    indice += alunos

    notas_ordenadas = sorted(notas, reverse=True)

    nao_trocados = sum(1 for aluno in range(alunos) if notas[aluno] == notas_ordenadas[aluno])
        
    resultados.append(nao_trocados)
    
for resultado in resultados:
        print(resultado)