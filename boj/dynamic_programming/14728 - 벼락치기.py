n, t = map(int, input().split())
lst = [(0,0)]
for _ in range(n):
    a,b = map(int, input().split())
    lst.append((a,b))

dp = [[0 for _ in range(t+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, t+1):
        if j < lst[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], lst[i][1]+dp[i-1][j-lst[i][0]])

print(dp[n][t])