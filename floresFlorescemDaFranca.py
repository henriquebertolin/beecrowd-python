while True:
    frase = input(). split()
    if frase[0][0] == '*':
        break
    total = 0
    letra = ''
    letra = frase[0][0]
    for i in range(1, len(frase)):
        if frase[i][0].upper() != letra.upper():
            total += 1
    if total > 0:
        print ('N')
    else:
        print ('Y')