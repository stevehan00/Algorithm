t = int(input())
 
dp = [0]*(63245)
 
for _ in range(t):
    n = int(input())
 
    dp[0] = 1
 
    maxs = 1
    maxs_cnt = 1
 
    re = 1
 
    cnt = 0
    while re < n:
        cnt += 1
        if n-re >= maxs:
            if maxs_cnt >= 2:
                maxs += 1
                dp[cnt] = dp[cnt-1] + maxs
                maxs_cnt = 1
            else:
                dp[cnt] = dp[cnt-1] + maxs
                maxs_cnt += 1
        else:
            dp[cnt] = dp[cnt-1]+(n-re)
 
        
        re = dp[cnt]
 
    print(cnt)