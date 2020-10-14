from collections import defaultdict

n = int(input())
s,e = map(int, input().split())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()
ans = -1

def dfs(node, k):
    global ans

    visited.add(node)

    if node == e:
        ans = k
        return

    for c in graph[node]:
        if not c in visited:
            dfs(c, k+1)
dfs(s, 0)
print(ans)