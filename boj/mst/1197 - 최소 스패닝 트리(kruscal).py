parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    
    return parent[v]


def union(u, v):
    root1 = find(u)
    root2 = find(v)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
 
def kruscal(vertex, edge):

    for v in vertex:
        make_set(v)

    mst = []

    edge.sort()

    for e in edge:
        w,u,v = e
        if find(u) != find(v):
            union(u, v)
            mst.append(e)

    return mst

n, m = map(int, input().split())

vertex = []
edges = []

for i in range(1, n+1):
    vertex.append(str(i))
for _ in range(m):
    u,v,c = map(int, input().split())
    edges.append((c, str(u), str(v)))

d = kruscal(vertex, edges)
ans = 0
for c in d:
    ans += c[0]

print(ans)