import sys

sys.setrecursionlimit(10**6)

parent = {}
rank = {}

def find(nn):
    if parent[nn] != nn:
        parent[nn] = find(parent[nn])
    
    return parent[nn]

def union(n1,n2):
    root1 = find(n1)
    root2 = find(n2)

    if rank[root1] < rank[root2]:
        parent[root1] = root2
    else:
        parent[root2] = root1
        if rank[root1] == rank[root2]:
            rank[root1] += 1

def kruscal():
    mst = []
    vv = 0
    for e in edges:
        w,u,v = e

        if find(u) != find(v):
            vv += w
            mst.append(e)
            union(u,v)

    return vv, mst

n, m = map(int, sys.stdin.readline().split())

for i in range(2,n+1):
    parent[str(i)] = str(i)
    rank[str(i)] = 0

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    union(str(a),str(b))

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
edges = []

for i in range(1,n):
    for j in range(i+1,n+1):
        if i == 1:
            break
        if find(str(i)) != find(str(j)):
            edges.append((arr[i-1][j-1], str(i),str(j)))

edges.sort()

d, val = kruscal()

print(d,len(val))

if val:
    for c in val:
        print(c[1],c[2])