def diamante(teste, diamantes):
    for i in range(len(teste)-1):
        if teste[i] == "<" and teste[i+1] == ">":
            diamantes+=1
            teste.pop(i+1)
            teste.pop(i)
            break
    string = ''.join(teste)
    if "<>" in string:
        return diamante(teste, diamantes)
    else:
        return diamantes
n = int(input())
for i in range(n):
    teste = input()
    letra = "."
    teste = teste.replace(letra,"")
    teste = list(teste)
    diamantes = 0
    resultado = diamante(teste, diamantes)
    print(resultado)
