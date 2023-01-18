import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cost = []
for _ in range(n):
    cost.append(int(input()))

left = max(cost)
right = 10**9
ans = sys.maxsize

while left <= right:
    half = (left + right) // 2

    cnt = 0
    cur = 0
    for k in range(n):
        if cur + cost[k] > half:
            cur = cost[k]
            cnt += 1
        else:
            cur += cost[k]
    if cur != 0:
        cnt += 1

    if cnt > m:
        left = half+1
    else:
        ans = half
        right = half-1

print(ans)