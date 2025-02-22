italic = False
bolden = False

while True:
    try:
        string = input()
        texto = ''
        for char in string:
            if char == '_':
                if italic:
                    char = '</i>'
                    italic = False
                else:
                    char = '<i>'
                    italic = True
                texto += char
            elif char == '*':
                if bolden:
                    char = '</b>'
                    bolden = False
                else:
                    char = '<b>'
                    bolden = True
                texto += char
            else:
                texto +=char
        print(texto)
    except EOFError:
        break
