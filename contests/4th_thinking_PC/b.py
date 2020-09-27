n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]


def prefixSum2D(a) : 
    psa = [[0 for x in range(n)]  for y in range(n)]  
    psa[0][0] = a[0][0] 
  

    for i in range(1, n) : 
        psa[0][i] = (psa[0][i - 1] + 
                       a[0][i]) 
    for i in range(0, n) : 
        psa[i][0] = (psa[i - 1][0] + 
                       a[i][0]) 
  
    for i in range(1, n) : 
        for j in range(1, n) : 
  
            psa[i][j] = (psa[i - 1][j] + 
                         psa[i][j - 1] - 
                         psa[i - 1][j - 1] + 
                           a[i][j]) 
    return psa
psa = prefixSum2D(lst)

maxs = -300000

for i in range(1, n+1):
    
    for k in range(i-1, n):
        for j in range(i-1, n):
            sums = psa[k][j]
            if k-i >= 0:
                sums -= psa[k-i][j]
            if j-i >= 0:
                sums -= psa[k][j-i]
            if k-1 >= 0 and j-1 >= 0:
                sums +=  psa[k-i][j-i]

            maxs = max(sums, maxs)

print(maxs)