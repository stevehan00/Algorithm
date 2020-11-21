import sys, heapq

inf = sys.maxsize

dx = [1,-1,0,0]
dy = [0,0,1,-1]

m,n = map(int, sys.stdin.readline().split())
lst = [list(sys.stdin.readline()[:-1]) for _ in range(n)]
dp = [[inf]*m for _ in range(n)]
visit = [[False]*m for _ in range(n)]

q = []

visit[0][0] = True
heapq.heappush(q, (0, 0, 0))
dp[0][0] = 0

while q:
    cur = heapq.heappop(q)

    for i in range(4):
        nr = cur[1] + dx[i]
        nc = cur[2] + dy[i]

        if 0 <= nr < n and 0 <= nc < m and visit[nr][nc] == False: 
            if lst[nr][nc] == '1':
                dp[nr][nc] = cur[0]+1
            else:
                dp[nr][nc] = cur[0]
            heapq.heappush(q, (dp[nr][nc], nr, nc))
            visit[nr][nc] = True

print(dp[n-1][m-1])