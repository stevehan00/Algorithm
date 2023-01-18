import heapq, sys

n = int(sys.stdin.readline())
time = []

for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    time.append((a,b))

time.sort(key=lambda x: x[0])

MAX_SIZE = 100001
cnt = 0
seat = [0]*MAX_SIZE
cur = []
left_pc = [] 

for s,e in time:
    while cur:
        if cur[0][0] <= s:
            heapq.heappush(left_pc, cur[0][1])
            heapq.heappop(cur)
        else:
            break
    
    if not left_pc:
        heapq.heappush(cur, (e, cnt))
        seat[cnt] += 1
        cnt += 1
    else:
        temp = heapq.heappop(left_pc)
        heapq.heappush(cur, (e, temp))
        seat[temp] += 1


print(cnt)
print(*seat[:cnt])