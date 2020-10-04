import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    exc = (n*(n-1))//2
 
    len_set = len(set(lst))
    if n > 1 and len_set == 1:
        print(exc)
        continue
 
    sums = 0
    
    lst.sort()
    c = 2
    cnt = 0
    while c <= lst[0]:
        c *= 2
 
    for i in range(n):
        if lst[i] < c:
            cnt += 1
        else:
            while c <= lst[i]:
                c *= 2
            sums += (cnt*(cnt-1))//2
            cnt = 1
    sums += (cnt*(cnt-1))//2
    print(sums)