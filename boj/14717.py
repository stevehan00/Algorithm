from itertools import combinations
a,b = map(int, input().split())

if a == b:
    if a == 10:
        print("%.3f" %(1))
    else:
        key = 10 - a
        p = ((1/(9*17))*key)

        print("%.3f" %(1-p))
else:
    if a + b == 10:
        print("%.3f" %(0))
    else:
        cnt = 0
        target = (a+b)%10
        lst = [1,2,3,4,5,6,7,8,9,10]*2
        lst.remove(a)
        lst.remove(b)

        for c in combinations(lst, 2):
            if c[0] != c[1] and sum(c)%10 < target:
                cnt += 1
        
        print("%.3f" %(cnt/(9*17)))