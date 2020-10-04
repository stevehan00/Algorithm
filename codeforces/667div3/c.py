import sys
 
t = int(sys.stdin.readline())
 
for _ in range(t):
    n,x,y = map(int, sys.stdin.readline().split())
    
    maxs = sys.maxsize
    d = 0
    for i in range(1, n):
        if i > y-x:
            break
 
        if (y-x)%i == 0:
            d = (y-x)//i
            #left part
            if x - d*(n-i-1) > 0:
                maxs = y
                break
            
            #right part
            for j in range(1, n-i):
 
                if x - d*(n-i-j-1) > 0:
                    maxs = y + d*j
                    break
            maxs = min(maxs, y+d*(n-2))
    
    print(*reversed([maxs - d*j for j in range(n)]))