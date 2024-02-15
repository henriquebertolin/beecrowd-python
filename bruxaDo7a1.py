x, operador, y = input(). split()
x = int(x)
y = int(y)
if operador == '+':
    soma = x + y
    if '7' in str(x):
        soma -= 7
        print (soma)
    elif '7' in str(y):
        soma -= 7
        print (soma)
    elif soma == 7:
        soma = 0
        print (soma)
    elif '7' in str(soma):
        soma = str(soma)
        soma = soma.replace('7','0')
        print(int(soma))
    else:
        print (soma)
elif operador == 'x':
    soma = x*y
    if '7' == str(x):
        soma = 0
        print (soma)
    elif '7' == str(y):
        soma = 0
        print (soma)
        
    elif soma == 7:
        soma = 0
        print (soma)
    elif '7' in str(soma):
        soma = str(soma)
        soma = soma.replace('7','0')
        print(int(soma))
    else:
        print (soma)