Hi, Mi, Hf, Mf = map(int, input().split())

Inicio = Hi * 60 + Mi
Fim = Hf * 60 + Mf

if Fim <= Inicio:
    Fim += 24 * 60

res = Fim - Inicio

hora = res // 60
minuto = res % 60

print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")