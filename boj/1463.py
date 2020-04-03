
n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        dp[i] = 0
        continue
    dp[i] = dp[i-1] + 1
    if i%3==0 and dp[i//3] < dp[i]:
        dp[i] = dp[i//3] + 1
    elif i%2==0 and dp[i//2] < dp[i]:
        dp[i] = dp[i//2] + 1

print(dp[n])