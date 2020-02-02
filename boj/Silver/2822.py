lst = [int(input()) for _ in range(8)]

for _ in range(3):
    temp = lst.index(min(lst))
    lst[temp] = 151

s = sum(lst) - 151*3
print(s)

for i in range(8):
    if(lst[i] == 151):
        continue
    else:
        print(i+1, end=' ')