n = int(input())
string = input()
total = 0
for j in range (len(string)):
    if j == 0:
        if string[j] == 'a' and string[j+1] == 'a':
            total +=1
    elif j+1 != len(string):
        if string[j] == 'a' and (string[j+1] == 'a' or string[j-1] == 'a'):
            total +=1
    elif j+1 == len(string):
        if string[j] == 'a' and string[j-1] == 'a':
            total +=1
print (total)
