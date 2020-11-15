from math import log2
import sys

sys.setrecursionlimit(10**6)

def dfs(parentNode, curDepth):
    depth[parentNode] = curDepth

    for c in tree[parentNode]:
        if not depth[c]:
            parent[c] = parentNode
            dfs(c, curDepth+1)


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    tree = [[] for _ in range(n+1)]
    parent = [0 for _ in range(n+1)]
    depth = [0 for _ in range(n+1)]

    visit = set()
    root = -1

    for _ in range(n-1):
        a,b = map(int, sys.stdin.readline().split())
        visit.add(b)
        tree[a].append(b)
 
    for c in range(1, n+1):
        if c not in visit:
            root = c
            break
    
    dfs(root,1)

    a,b = map(int, sys.stdin.readline().split())
    if depth[a] < depth[b]:
        a, b = b, a

    while depth[a] != depth[b]:
        a = parent[a]

    while a != b:
        a = parent[a]
        b = parent[b]
        
    print(a)