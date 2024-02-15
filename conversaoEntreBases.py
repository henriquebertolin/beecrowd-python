def binaryToDec(bin):
    dec = 0
    for i in bin:
        dec = dec*2+int(i)
    return dec



n = int(input())
for i in range(n):
    num, base = input(). split()
    if base == 'bin':
        decimal = binaryToDec(num)
        print (f'Case {i+1}:')
        print (f'{decimal} dec')
        print (f'{hex(decimal)[2:]} hex')
        print()
    elif base == 'dec':
        num = int(num)
        print (f'Case {i+1}:')
        print (f'{hex(num)[2:]} hex')
        print (f'{bin(num)[2:]} bin')
        print()
    elif base == 'hex':
        print (f'Case {i+1}:')
        print (f'{int(num,16)} dec')
        decimal = int(num,16)
        print (f'{bin(decimal)[2:]} bin')
        print()