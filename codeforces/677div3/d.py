import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    ans = []

    if len(set(lst)) < 2:
        print('NO')
        continue

    vis = set()
    vis.add(1)

    for i in range(n):
        if len(ans) == n-1:
            break

        st = lst[i]
        for j in range(n):
            if len(ans) == n-1:
                break
            if lst[i] != lst[j] and j+1 not in vis:
                ans.append((i+1, j+1))
                vis.add(j+1)
            
    
    if len(ans) == n-1:
        print('YES')
        for c in ans:
            print(*c)
    else:
        print('NO')