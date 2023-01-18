from collections import defaultdict
import heapq

def prim(start, edges):
    mst = []
    adjacent_edges = defaultdict(list)
    for w, u, v in edges:
        adjacent_edges[u].append((w,u,v))
        adjacent_edges[v].append((w,v,u))

    connected_nodes = set(start)
    candidate_edges = adjacent_edges[start]

    heapq.heapify(candidate_edges)

    while candidate_edges:
        w, u, v = heapq.heappop(candidate_edges)
        if v not in connected_nodes:
            connected_nodes.add(v)
            mst.append((w,u,v))

            for e in adjacent_edges[v]:
                if e[2] not in connected_nodes:
                    heapq.heappush(candidate_edges, e)

    return mst

n, m = map(int, input().split())


edges = []

for _ in range(m):
    u,v,c = map(int, input().split())
    edges.append((c, str(u), str(v)))

d = prim(edges[0][1], edges)

ans = 0

for c in d:
    ans += c[0]

print(ans)