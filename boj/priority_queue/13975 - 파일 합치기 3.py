import sys, heapq

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    pq = []

    for c in lst:
        heapq.heappush(pq, c)

    cnt = 0
    while len(pq) > 1:
        c1 = heapq.heappop(pq) + heapq.heappop(pq)
        cnt += c1
        heapq.heappush(pq, c1)
    print(cnt)