import sys
from itertools import combinations

n = int(sys.stdin.readline())

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

p_sum = 0
w_sum = 0

for i in range(n-2):
    p_sum += lst[i][0]
    w_sum += lst[i][1]

print(p_sum/w_sum)

def cal(lst):
    maxi = -1
    for i in lst:
        p_sum = 0
        w_sum = 0
        for j in range(8):
            p_sum += i[j][0]
            w_sum += i[j][1]
        if maxi < (p_sum/w_sum):
            maxi = p_sum/w_sum

    return maxi

if n != 8:
    for i in range(9, n+1):
        a = list(combinations(lst[:i], 8))
        print(cal(a))
