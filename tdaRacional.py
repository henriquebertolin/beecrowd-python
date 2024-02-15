def euclides(a, b):
    if b == 0:
        return a
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
for i in range(n):
    operacao = input().split()
    resultado = 0
    for j in range(0,len(operacao),2):
       operacao[j] = int(operacao[j])
    if operacao[3] == '+':
        num = ((operacao[0] * operacao[6]) + (operacao[2] * operacao[4]))
        den = (operacao[2] * operacao[6])
        mdc = euclides(num, den)
        print (f'{num}/{den} = {int(num/mdc)}/{int(den/mdc)}')
    elif operacao[3] == '-':
        num = ((operacao[0] * operacao[6]) - (operacao[2] * operacao[4]))
        den = (operacao[2] * operacao[6])
        mdc = euclides(num,den)
        print (f'{num}/{den} = {int(num/mdc)}/{int(den/mdc)}')
    elif operacao[3] == '*':
        num = (operacao[0] * operacao[4])
        den = (operacao[2] * operacao[6])
        mdc = euclides(num, den)
        print (f'{num}/{den} = {int(num/mdc)}/{int(den/mdc)}')
    elif operacao[3] == '/':
        num = operacao[0] * operacao[6]
        den = operacao[4] * operacao[2]
        mdc = euclides(num, den)
        print (f'{num}/{den} = {int(num/mdc)}/{int(den/mdc)}')     

