import sys
 
t = int(sys.stdin.readline())
 
for _ in range(t):
    a,b,x,y,n = map(int, sys.stdin.readline().split())
 
    a2, b2, n2 = a, b, n
 
    if a-x <= n:
        n -= a-x
        a = x
    else:
        a -= n
        n = 0
 
    if b-y <= n:
        n -= b-y
        b = y
    else:
        b -= n
        n = 0
 
    if b2-y <= n2:
        n2 -= b2-y
        b2 = y
    else:
        b2 -= n2
        n2 = 0
 
    if a2-x <= n2:
        n2 -= a2-x
        a2 = x
    else:
        a2 -= n2
        n2 = 0
 
    print(min(a*b, a2*b2))