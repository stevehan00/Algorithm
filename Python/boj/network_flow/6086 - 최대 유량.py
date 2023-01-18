from collections import defaultdict, deque
import sys

INF = sys.maxsize

def bfs(start, sink, parent):
    visited = defaultdict(lambda : 0)
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        u = q.popleft()
        for ind in edge[u]:
            val = edge[u][ind]
            if visited[ind]:
                continue
            if val <= 0:
                continue
            q.append(ind)
            visited[ind] = 1
            parent[ind] = u
    
    return 1 if visited[sink] else 0

def ford_fulkerson(start, sink):
    parent = defaultdict(lambda: -1)
    max_flow = 0
    while bfs(start, sink, parent):
        path_flow = INF
        s = sink
        while s != start:
            path_flow = min(path_flow, edge[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink

        while v != start:
            u = parent[v]
            edge[u][v] -= path_flow
            edge[v][u] += path_flow
            v = parent[v]
    
    return max_flow

n = int(input())

edge = defaultdict(lambda : defaultdict(int))

for _ in range(n):
    i,j,c = input().split()
    edge[i][j] += int(c)
    edge[j][i] += int(c)

print(ford_fulkerson('A','Z'))