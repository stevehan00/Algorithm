import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

maxs = 0
for i in range(n-1):
    cnt = 0
    for j in range(i+1, n):
        if lst[j] < lst[i]:
            cnt += 1
        else:
            break
    
    maxs = max(maxs, cnt)

print(maxs)