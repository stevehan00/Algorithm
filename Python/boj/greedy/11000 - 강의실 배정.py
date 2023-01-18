import sys, heapq

input = sys.stdin.readline

pairs = []

n = int(input())
for _ in range(n):
    s, t = map(int, input().split())
    pairs.append((s,t))

pairs.sort()

pq = []

for c in pairs:
    if not pq:
        heapq.heappush(pq, c[1])
    else:
        temp = heapq.heappop(pq)
        if c[0] < temp:
            heapq.heappush(pq, temp)
        heapq.heappush(pq, c[1])

print(len(pq))