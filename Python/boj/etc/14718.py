import sys
from itertools import combinations

n, k = map(int, sys.stdin.readline().split())

a = [0]*100
b = [0]*100
c = [0]*100

MAXS = 1000000
aa, bb, cc = MAXS, MAXS, MAXS

ans = 100

for i in range(n):
    a[i], b[i], c[i] = map(int, sys.stdin.readline().split())

for i in range(n):
    for j in range(n):
        for l in range(n):
            ta, tb, tc = a[i], b[j], c[l]
            cnt = 0

            for t in range(n):
                if ta >= a[t] and tb >= b[t] and tc >= c[t]:
                    cnt += 1
            
            if cnt >= k and cnt <= ans and ta+tb+tc < aa+bb+cc:
                ans = cnt
                aa,bb,cc = ta,tb,tc

print(aa+bb+cc)
            


