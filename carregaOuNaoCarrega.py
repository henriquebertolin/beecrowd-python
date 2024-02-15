def mofiz(n, m):
    bitsN = format(n, '032b')
    bitsM = format(m, '032b')
    return bitsN, bitsM

def mofizReverso(stringResul):
    soma = int(stringResul, 2)
    return soma

while True:
    try:
        n, m = map(int, input().split())
        resultado = mofiz(n, m)
        stringN = resultado[0]
        stringM = resultado[1]
        stringR = ''.join('0' if c1 == c2 else '1' for c1, c2 in zip(stringN, stringM))
        print(mofizReverso(stringR))
    except EOFError:
        break
