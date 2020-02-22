import math
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    diff = int(y-x)
    if diff<=3:
        print(diff)
    else:
        n = int(math.sqrt(diff))
        if diff == n**2:
            print(2*n-1)
        elif n**2<diff<=n**2+n:
            print(2*n)
        else:
            print(2*n+1)