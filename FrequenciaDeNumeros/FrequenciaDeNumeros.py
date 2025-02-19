n = int(input())
count = {}

for _ in range(n):
    
    numero = int(input())
    
    if numero in count:
        count[numero] += 1
    else:
        count[numero] = 1
        
for numero in sorted(count):
    print(f'{numero} aparece {count[numero]} vez(es)')
