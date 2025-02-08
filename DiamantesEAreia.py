N = int(input())

for _ in range(N):
    entrada = input().replace('.', '')
    sin = []
    count = 0
    
    for caracter in entrada:
        if caracter == '<':
            sin.append(caracter)
        elif caracter == '>' and sin:
            if sin[-1] == '<':
                sin.pop()
                count += 1
    
    print(count)
