n = int(input())
lst = list(map(int, input().split()))

dp = [0]*(n+1)

for i in range(1,n+1):
    dp[i] = lst[i-1]

    for j in range(1, i//2+1):
        dp[i] = max(dp[i], dp[j]+dp[i-j])

print(dp[-1])