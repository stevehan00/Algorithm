import sys, heapq

n = int(sys.stdin.readline())
pq = []

for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for c in line:
        heapq.heappush(pq, c)
        if len(pq) > n:
            heapq.heappop(pq)


print(heapq.heappop(pq))