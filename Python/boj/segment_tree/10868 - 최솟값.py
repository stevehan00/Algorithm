from math import ceil, log2
import sys

sys.setrecursionlimit(10**6)

def init(node, start, end):
    if start == end:
        tree[node] = lst[start]
        return lst[start]
    else:
        tree[node] = min(init(node*2, start, (start+end)//2), init(node*2+1, (start+end)//2+1, end))
        return tree[node]

def query(node, start, end, left, right):
    if right < start or end < left:
        return sys.maxsize

    if left <= start and end <= right:
        return tree[node]

    return min(query(node*2, start, (start+end)//2, left, right), query(node*2+1, (start+end)//2+1, end, left, right))


n, m = map(int, sys.stdin.readline().split())
tree_size = 1 << ((int)(ceil(log2(n)))+1)
lst = []
tree = [sys.maxsize for _ in range(tree_size)]

for _ in range(n):
    num = int(sys.stdin.readline())
    lst.append(num)

init(1, 0, n-1)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    print(query(1,0,n-1,a-1,b-1))