import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    if not visited[node]:
        visited[node] = True
        dfs(ipt[node])

t = int(input())
for _ in range(t):
    n = int(input())
    ipt = [0] + list(map(int, input().split()))

    cnt = 0
    visited = [False]*(n+1)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(ipt[i])
            cnt += 1
    
    print(cnt)