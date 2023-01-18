import heapq, sys

n, k = map(int, sys.stdin.readline().split())

lst = []

for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    lst.append((a,b))

pq = []
mx = []

cal = [0 for _ in range(k+1)]
cal_temp = [0 for _ in range(k+1)]

idx = 0
cnt = 1

if n > k:
    pre = 0
    for i in range(1, k+1):
        heapq.heappush(pq, (lst[idx][1], i, lst[idx][0]))
        cal[i] = 1
        idx += 1

    while idx < n or pq:
        cur = heapq.heappop(pq)
        heapq.heappush(mx, (cur[0], -cur[1], cur[2]))
        cal[cur[1]] = 0
        cal_temp[cur[1]] = cur[0]

        if idx < n:
            heapq.heappush(pq, (cur[0]+lst[idx][1], cur[1], lst[idx][0]))
            idx += 1
else:
    for i in range(n):
        heapq.heappush(mx, (lst[idx][1], -i, lst[idx][0]))
        idx += 1


ans = 0
cnt = 1
while mx:
    c = heapq.heappop(mx)
    ans += c[2]*cnt
    cnt += 1

print(ans)