from math import log2, floor
import sys

sys.setrecursionlimit(10**6)

def dfs(parentNode, curDepth):
    depth[parentNode] = curDepth

    for c in tree[parentNode]:
        if not depth[c]:
            exp_parent[c][0] = parentNode
            dfs(c, curDepth+1)

def compute_exp_parent(exp_parent, N):
    for i in range(1, logN):
        for j in range(1, n+1):
            exp_parent[j][i] = exp_parent[exp_parent[j][i-1]][i-1]


n = int(sys.stdin.readline())

tree = [[] for _ in range(n+1)]
depth = [0 for _ in range(n+1)]

logN = (int)(log2(n)+1)
exp_parent = [[0 for _ in range(logN)] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1, 1)

compute_exp_parent(exp_parent, n)

m = int(sys.stdin.readline())

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(logN-1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = exp_parent[b][i]

    if a != b:
        for i in range(logN-1, -1, -1):
            if exp_parent[a][i] != exp_parent[b][i]:
                a = exp_parent[a][i]
                b = exp_parent[b][i]

        b = exp_parent[b][0]

    print(b)