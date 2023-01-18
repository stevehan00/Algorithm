import sys, heapq

n,m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
inDgree = [0 for _ in range(n+1)]

for _ in range(m):
    s,e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    inDgree[e] += 1

q = []
result = []

for i in range(1, n+1):
    if inDgree[i] == 0:
        heapq.heappush(q, i)

while q:
    cur = heapq.heappop(q)
    result.append(cur)

    for t in graph[cur]:
        inDgree[t] -= 1
        if inDgree[t] == 0:
            heapq.heappush(q, t)

print(*result)