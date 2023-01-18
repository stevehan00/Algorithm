a,b,c,n = map(int, input().split())

dp = [0 for i in range(301)]

dp[0] = 1

for i in range(len(dp)):

    if i+a > 300:
        a = 0
    if i+b > 300:
        b = 0
    if i+c > 300:
        c = 0

    if dp[i]==1:
        dp[i+a] = dp[i+b] = dp[i+c] = 1
    
print(dp[n])