from collections import deque
import sys

n,m = map(int , sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
inDgree = [0 for _ in range(n+1)]

q = deque()
result = []

for _ in range(m):
    s,e = map(int , sys.stdin.readline().split())
    graph[s].append(e)
    inDgree[e] += 1

for i in range(1, n+1):
    if inDgree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    result.append(cur)
    for t in graph[cur]:
        inDgree[t] -= 1
        if inDgree[t] == 0:
            q.append(t)

print(*result)