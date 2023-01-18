from collections import deque, defaultdict
import sys

INF = sys.maxsize

def bfs(parent):
    visited = [0 for _ in range(n+1)]
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        u = q.popleft()
        for ind in edge[u]:
            if visited[ind]:
                continue
            if edge[u][ind] == 0:
                continue
            q.append(ind)
            visited[ind] = 1
            parent[ind] = u
    
    return 1 if visited[sink] == 1 else 0


def ford_fulkerson():
    parent = [0 for _ in range(n+1)]
    max_flow = 0

    while bfs(parent):
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
            v= parent[v]


    return max_flow

n,p = map(int ,sys.stdin.readline().split())
edge = defaultdict(lambda: defaultdict(int))

start = 1
sink = 2

for _ in range(p):
    a,b = map(int ,sys.stdin.readline().split())
    edge[a][b] = 1

print(ford_fulkerson())