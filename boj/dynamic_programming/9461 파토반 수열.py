t = int(input())

dp = [1,1,1,2,2,3]

for _ in range(6, 101):
    dp.append(dp[-1]+dp[-5])

for _ in range(t):
    print(dp[int(input())-1])