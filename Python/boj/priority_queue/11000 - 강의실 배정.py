import heapq

n = int(input())

hpq = []

for _ in range(n):
    s, t = map(int, input().split())
    heapq.heappush(hpq, (s, t))

cnt = []

while hpq:
    cur = heapq.heappop(hpq)

    if not cnt:
        heapq.heappush(cnt, cur[1])
    else:
        temp = heapq.heappop(cnt)
        if cur[0] < temp:
            heapq.heappush(cnt, temp)
        heapq.heappush(cnt, cur[1])


print(len(cnt))