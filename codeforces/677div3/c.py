import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))

    maxs = max(lst)
    ans = -1
    for i in range(n):
        if lst[i] == maxs:
            if i == 0 and lst[i+1] < maxs:
                ans = i+1
                break
            elif i == n-1 and lst[i-1] < maxs:
                ans = i+1
                break
            elif (0 < i < n-1) and  (lst[i-1] < maxs or lst[i+1] < maxs):
                ans = i+1
                break
    
    print(ans)