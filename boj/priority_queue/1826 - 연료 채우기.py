import heapq

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
lst.sort(key = lambda x : x[0])

l, p = map(int, input().split())
pq = []
idx = 0
cnt = 0
while idx < n or pq:
    
    if p >= l:
        break

    while idx < n and lst[idx][0] <= p:
        heapq.heappush(pq, (-lst[idx][1], lst[idx][0]))
        idx += 1
    
    if pq:
        cnt += 1
        temp = heapq.heappop(pq)
        p += -temp[0]
    else:
        idx += 1


if p < l:
    print(-1)
else:
    print(cnt)