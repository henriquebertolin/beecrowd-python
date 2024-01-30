while True:
    n = int(input())
    if n == 0:
        break
    aceitos = []
    tentados = []
    tempoTotal = 0
    incorretos = 0
    for i in range(n):
        questao, tempo, status = input(). split()
        tempo = int(tempo)
        indice = 0
        if questao not in aceitos:
            if status == 'correct':
                aceitos.append(questao)
                tempoTotal += tempo
            elif status == 'incorrect':
                if questao not in tentados:
                    tentados.append(questao)
                    tentados.append(1)
                else:
                    indice = tentados.index(questao) + 1
                    tentados[indice] += 1
                # if len(aceitos) > 0:
                #     incorretos += 1
    for i in range(len(tentados)):
        if tentados[i] in aceitos:
            incorretos += tentados[i+1]
    tempoTotal += incorretos * 20
    print (f'{len(aceitos)} {tempoTotal}')