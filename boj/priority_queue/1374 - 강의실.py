import heapq

n = int(input())
lst = []
pq = []
for _ in range(n):
    a,b,c = map(int, input().split())
    lst.append((b,c))

lst.sort()

for i in range(n):
    if not pq:
        heapq.heappush(pq, lst[i][1])
    else:
        peek = heapq.heappop(pq)
        if peek > lst[i][0]:
            heapq.heappush(pq, peek)
        heapq.heappush(pq, lst[i][1])

print(len(pq))