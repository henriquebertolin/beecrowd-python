n = int(input())
print()
for i in range(n):
    arvores = {}
  #  while True:
  #      try:
    for j in range(5):
        teste = input()
        arvores[teste] = 1 + arvores.get(teste, 0)
        arvores = dict(sorted(arvores.items()))
    for k,v in arvores.items():
        print (f'{k} {v*100/len(arvores):.4f}')
        #except EOFError:
          #  break