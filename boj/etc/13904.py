import heapq

n = int(input())
lst = []
for _ in range(n):
    a,b = map(int, input().split())
    lst.append((a,b))

pq = []

lst.sort(key = lambda x: -x[0])
day = lst[0][0]
idx = 0

ans = 0

while day > 0:
    while idx < n and lst[idx][0] == day:
        heapq.heappush(pq, (-lst[idx][1], lst[idx][1]))
        idx += 1
    
    if pq:
        ans += heapq.heappop(pq)[1]
    day -= 1

print(ans)