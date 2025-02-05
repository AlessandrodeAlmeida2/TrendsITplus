import math

def simplificar(numerador, denominador):
    gcd = math.gcd(numerador, denominador)
    return numerador // gcd, denominador // gcd

def operar_frações(N1, D1, operador, N2, D2):
    if operador == '+':
        numerador = N1 * D2 + N2 * D1
        denominador = D1 * D2
    elif operador == '-':
        numerador = N1 * D2 - N2 * D1
        denominador = D1 * D2
    elif operador == '*':
        numerador = N1 * N2
        denominador = D1 * D2
    elif operador == '/':
        numerador = N1 * D2
        denominador = N2 * D1
    return numerador, denominador

n = int(input())

for _ in range(n):
    r = input().split()
    N1, D1 = int(r[0]), int(r[2])
    operador = r[3]
    N2, D2 = int(r[4]), int(r[6])
    
    numerador, denominador = operar_frações(N1, D1, operador, N2, D2)
    numerador_simplificado, denominador_simplificado = simplificar(numerador, denominador)
    
    if numerador_simplificado == numerador and denominador_simplificado == denominador:
        print(f"{numerador}/{denominador} = {numerador}/{denominador}")
    else:
        print(f"{numerador}/{denominador} = {numerador_simplificado}/{denominador_simplificado}")