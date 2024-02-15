while(True):
    try:
        soma = 0
        n = int(input())
        pilotos = list(map(int,input(). split()))
        pilotosFinal = list(map(int,input(). split()))
        for i in range(len(pilotos)):
            valor = (pilotos[i] - pilotosFinal[i])
            if valor < 0:
                valor *= -1
            soma += valor
        print(int(soma/2))
    except EOFError:
        break
