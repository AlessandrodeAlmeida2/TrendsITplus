palavra1 = input().strip().lower()
palavra2 = input().strip().lower()
palavra3 = input().strip().lower()

if palavra1 == 'vertebrado':
    if palavra2 == 'ave':
        if palavra3 == 'carnivoro':
            animal = 'aguia'
        else:
            animal = 'pomba'
    elif palavra2 == 'mamifero':
        if palavra3 == 'onivoro':
            animal = 'homem'
        else:
            animal = 'vaca'
elif palavra1 == 'invertebrado':
    if palavra2 == 'inseto':
        if palavra3 == 'hematofago':
            animal = 'pulga'
        else:
            animal = 'lagarta'
    elif palavra2 == 'anelideo':
        if palavra3 == 'hematofago':
            animal = 'sanguessuga'
        else:
            animal = 'minhoca'
                
print(animal)
 