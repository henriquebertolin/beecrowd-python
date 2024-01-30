amigos = 0
dist = 0
media = 0
while True:
    try:
        n = input()
        amigos += 1
        x = int(input())
        dist += x
    except EOFError:
        media = dist / amigos
        print (f'{media:.1f}')
        break 