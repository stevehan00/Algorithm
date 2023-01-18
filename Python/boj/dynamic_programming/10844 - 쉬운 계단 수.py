n = int(input())
MOD = 1000000000
dp = [[0]*11 for _ in range(101)]

for i in range(1,10):
    dp[1][i] = 1

for i in range(2,n+1):
    dp[i][0] = dp[i-1][1]
    for j in range(1,10):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])%MOD

print(sum(dp[n])%MOD)