n, k = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

dp = [0 for _ in range(k+1)]

dp[0] = 1

for coin in lst:
    for j in range(k+1):
        if dp[j] != 0:
            if j + coin > k:
                continue
            dp[j+coin] += dp[j]

print(dp[-1])