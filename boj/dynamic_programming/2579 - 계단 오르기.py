n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

dp = []

if n < 3:
    print(sum(lst))
else:
    dp.append(lst[0])
    dp.append(dp[0]+lst[1])
    dp.append(max(dp[0]+lst[2], lst[1]+lst[2]))

    for i in range(3, n):
        dp.append(max(lst[i]+dp[i-2], lst[i]+lst[i-1]+dp[i-3]))
    
    print(dp[-1])