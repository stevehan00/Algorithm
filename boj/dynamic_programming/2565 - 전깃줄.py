n = int(input())
lst = []
dp = [1 for _ in range(n)]

for _ in range(n):
    a,b = map(int, input().split())
    lst.append((a,b))

lst.sort(key= lambda x : x[0])

for i in range(n):
    for j in range(i):
        if lst[j][1] < lst[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))