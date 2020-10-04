import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
 
    set_len = len(set(lst))
 
    if set_len == 1:
        print('YES')
        continue
    if set_len == n:
        if lst == sorted(lst, reverse=True):
            print('NO')
        else:
            print('YES')
    else:
        print('YES')