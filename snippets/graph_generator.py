import sys
from collections import defaultdict

# number of node
n = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(n-1):
    #start, end, weight
    a,b,w = map(int, sys.stdin.readline().split())
    graph[a].append((w,b))
    graph[b].append((w,a))