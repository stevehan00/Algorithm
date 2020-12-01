import sys

while True:
    candy = []
    n, m = map(float, sys.stdin.readline().split())
    n = int(n)
    m = int(round(m*100))

    if n == 0 and m == 0:
        break

    for _ in range(n):
        a,b = map(float, sys.stdin.readline().split())
        b = int(round(b*100))
        candy.append((int(a),b))

    dp = [0 for _ in range(10001)]

    for i in range(n):
        for j in range(m):
            if j+candy[i][1] > m:
                break
            else:
                dp[j+candy[i][1]] = max(dp[j]+candy[i][0], dp[j+candy[i][1]])
    

    print(max(dp))