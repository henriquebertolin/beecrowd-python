while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        estado = 0
        menores = 0
        letras = list(map(int, input().split()))
        opcoes = ['A','B','C','D','E']
        media = 0
        for i in range(len(letras)):
            media += letras[i]
            if letras[i] <= 127:
                estado+=1 
                menores += i
        media /= 5
        if estado == 1:
            print (opcoes[menores])
        else:
            print ('*')