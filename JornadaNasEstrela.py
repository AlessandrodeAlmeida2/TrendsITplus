N = int(input())

estrela = list(map(int, input().split()))

i =0
estrela_atacada = [False] * N

while 0 <= i < N and estrela[i] > 0:
  estrela_atacada[i] = True

  if estrela[i] % 2 == 0:
    estrela[i] -= 1
    i -= 1
  else:
    estrela[i] -= 1
    i += 1

total_estrela_atacada = sum(estrela_atacada)
total_carneiros = sum(estrela)

print(total_estrela_atacada, total_carneiros)
