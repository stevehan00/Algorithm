from bisect import bisect_left

n = int(input())
lst = list(map(int, input().split()))

dp = [lst[0]]

for i in range(1, n):
    if dp[-1] < lst[i]:
        dp.append(lst[i])
    else:
        idx = bisect_left(dp, lst[i])
        dp[idx] = lst[i]

print(n-len(dp))