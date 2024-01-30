num = []
n = int(input())
for i in range(n):
    cont = 0
    qtd = int(input())
    num = list(map(int, input(). split()))
    sortedNum = num.copy()
    sortedNum.sort(reverse = True)
    for j in range(len(num)):
        if num[j] != sortedNum[j]:
            cont += 1
    # print(num)
    # print (sortedNum)
    print (len(num) - cont)