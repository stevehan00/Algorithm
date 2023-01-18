num = input()
lst=[]
for i in range(len(num)):
    lst.append(int(num[i]))

lst.sort()
for i in range(len(lst)-1,-1,-1):
    print(lst[i], end='')