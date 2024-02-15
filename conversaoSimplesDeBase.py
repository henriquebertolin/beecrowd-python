while True:
    try:
        numero = input()
        if '-' in numero:
            break
        if 'x' in numero:
            numero = int(numero,16)
            print (numero)
        else:
            numero = int(numero)
            numero = hex(numero)
            print (f'0x{numero.upper()[2:]}')
    except EOFError:
        break