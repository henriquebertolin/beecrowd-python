while(True):
    try:
        n = input()
        maior = 0
        num = '1'
        teste = '1234567890'
        for i in range (len(teste)):
            if n.count(teste[i]) == maior:
                if int(num) < int(teste[i]):
                    num = int(teste[i])
                    maior = n.count(teste[i])
            if n.count(teste[i]) > maior:
                num = int(teste[i])
                maior = n.count(teste[i])
        print (num)
    except EOFError:
        break
