import sys
sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())

def dfs(node, g):
    vis[node] = g
    for i in graph[node]:
        if vis[i] == 0:
            if not dfs(i,-g):
                return False
        elif vis[i] == vis[node]:
            return False
    return True

for _ in range(t):
    v,e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    vis = [0]*(v+1)

    for _ in range(e):
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = True

    for i in range(1, v+1):
        if vis[i] == 0:
            ans = dfs(i, 1)
            if not ans:
                break
    
    if ans:
        print('YES')
    else:
        print('NO')