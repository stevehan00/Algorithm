import sys, heapq

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for _ in range(m):
    lst = list(map(int, sys.stdin.readline().split()))
    
    for i in range(1, lst[0]):
        graph[lst[i]].append(lst[i+1])
        indegree[lst[i +1]] += 1

pq = []
results = []

for i in range(1,n+1):
    if indegree[i] == 0:
        pq.append(i)

while pq:
    cur = pq.pop()
    results.append(cur)

    for t in graph[cur]:
        indegree[t] -= 1
        if indegree[t] == 0:
            pq.append(t)

if len(results) == n:
    for c in results:
        print(c)
else:
    print(0)