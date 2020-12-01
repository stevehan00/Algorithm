c, b = map(int, input().split())
lst = list(map(int, input().split()))

dp = [0 for _ in range(c+1)]
dp[0] = 1

for i in range(b):
    for j in range(c+1):
        if lst[i] == j:
            continue
        if dp[j] == 1 and j + lst[i] <= c:
            dp[j+lst[i]] = 1

for i in range(c, 0, -1):
    if dp[i]:
        print(i)
        break