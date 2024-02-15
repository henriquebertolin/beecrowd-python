n = int(input())
palavras = []
for i in range(n):
    teste = input()
    teste = teste.replace('·',' ')
    palavras.append(teste.split())
    for j in range(len(palavras[i])):
        print(f'{palavras[i][j][0]}',end='')
    print('')
