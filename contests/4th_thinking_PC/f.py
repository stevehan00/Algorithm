import sys

n, m = map(int, sys.stdin.readline().split())

lst = []

for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    a = int(a)

    if not lst:
        temp = [(a,b)]
        lst.append(temp)
        continue
    
    for i in range(len(lst)):
        if len(lst[i]) >= m:
            continue
        if lst[i][0][0]-10 <= a <= lst[i][0][0]+10:
            lst[i].append((a,b))
            break
    else:
        temp = [(a,b)]
        lst.append(temp)


for i in range(len(lst)):
    if len(lst[i]) < m:
        print("Waiting!")
    else:
        print("Started!")
    
    lst[i].sort(key=lambda x: x[1])

    for c,d in lst[i]:
        print(c,d)