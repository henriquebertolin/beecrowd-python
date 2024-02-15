while True:
    soma = 0
    numeros = []
    x, y = map(int, input(). split())
    if x <= 0 or y <= 0:
        break
    if x > y:
        for i in range(y,x+1):
            soma += i
            numeros.append(i)
    if x < y:
        for i in range(x,y+1):
            soma += i
            numeros.append(i)
    print (*numeros, end ='')
    print (f' Sum={soma}')