def contar_letras(texto):
    from collections import Counter
    texto = texto.lower()
    contagem = Counter(filter(str.isalpha, texto))
    max_frequencia = max(contagem.values())
    letras_mais_frequentes = [letra for letra, freq in contagem.items() if freq == max_frequencia]
    return ''.join(sorted(letras_mais_frequentes))

N = int(input())

for _ in range(N):
    texto = input()
    resultado = contar_letras(texto)
    print(resultado)
