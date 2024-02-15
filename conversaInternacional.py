x = int(input())
for i in range(x):
    y = int(input())
    idiomas = []
    igual = True
    for j in range(y):
        idiomas.append(input())
    for j in range(len(idiomas)):
        for c in range(len(idiomas)):
            if idiomas[j] != idiomas[c]:
                igual = False
    if igual == True:
        print(idiomas[0])
    else:
        print("ingles")