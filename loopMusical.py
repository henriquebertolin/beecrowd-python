while True:
    cont = 0
    n = int(input())
    if n == 0:
        break
    vetor = []
    valores = input().split()
    for i in range(n):
        vetor.append(int(valores[i]))
    for i in range(n):
        if i == 0:
            if (vetor[i] > vetor[i + 1] and vetor[i] > vetor[-1]) or (vetor[i] < vetor[i + 1] and vetor[i] < vetor[-1]):
                cont += 1
        elif i == n - 1:
            if (vetor[i] > vetor[i - 1] and vetor[i] > vetor[0]) or (vetor[i] < vetor[i - 1] and vetor[i] < vetor[0]):
                cont += 1
        elif (vetor[i] > vetor[i + 1] and vetor[i] > vetor[i - 1]) or (vetor[i] < vetor[i + 1] and vetor[i] < vetor[i - 1]):
            cont += 1
    print(cont)