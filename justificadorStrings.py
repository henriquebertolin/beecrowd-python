cont = 0
while(True):
    n = int(input())
    if n == 0:
        break
    palavras = []
    maior = 0
    for i in range(n):
        teste = input()
        if len(teste) > maior:
            maior = len(teste)
        palavras.append(teste)
    if cont != 0:
        print()
    for i in range(len(palavras)):
        diferenca = maior - len(palavras[i])
        print(f"{' ' * diferenca}{palavras[i]}")
    cont += 1