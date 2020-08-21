n = int(input())
lst = list(map(int, input().split()))
dp = []

dp.append(lst[0])

for i in range(1, len(lst)):
    dp.append(max(dp[i-1]+lst[i], lst[i]))

print(max(dp))