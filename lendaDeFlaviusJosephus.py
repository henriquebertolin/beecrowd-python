n = int(input())
for i in range(1, n+1):
    x, y = map(int, input(). split())
    lista = list(range(1,x+1))
    indice = 0
    while len(lista) > 1:
        indice = (indice + y - 1) % len(lista)
        lista.pop(indice)
    print(f'Case {i}: {lista[0]}')