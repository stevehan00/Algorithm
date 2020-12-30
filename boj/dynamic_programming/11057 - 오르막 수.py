mod = 10007
n = int(input())

dp = [[0]*10 for _ in range(n)]

for i in range(10):
    dp[0][i] = 1

for i in range(1,n):
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][j] = sum(dp[i-1][:j+1])%mod

print(sum(dp[-1])%mod)