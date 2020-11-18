import sys, heapq

inf = sys.maxsize

dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt = 1

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visit = [[False]*n for _ in range(n)]
    dp = [[inf]*n for _ in range(n)]

    q = []
    heapq.heappush(q, (lst[0][0], 0, 0))
    visit[0][0] = True

    while q:
        cur = heapq.heappop(q)

        for i in range(4):
            next_r = cur[1] + dx[i]
            next_c = cur[2] + dy[i]

            if 0 <= next_r < n and 0 <= next_c < n and visit[next_r][next_c] == False:
                dp[next_r][next_c] = min(dp[next_r][next_c], cur[0]+lst[next_r][next_c])
                heapq.heappush(q, (cur[0]+lst[next_r][next_c], next_r, next_c))
                visit[next_r][next_c] = True

    print("Problem {}: {}" .format(cnt, dp[n-1][n-1]))
    cnt += 1