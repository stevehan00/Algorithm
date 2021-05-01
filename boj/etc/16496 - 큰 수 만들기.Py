from functools import cmp_to_key

def com(x, y):
    t1 = int(str(x)+str(y))
    t2 = int(str(y)+str(x))
    if t1>t2:
        return -1
    else:
        return 1

n = int(input())
lst = list(map(int, input().split()))
lst.sort(key = cmp_to_key(com))
r = ''.join(map(str,lst))

if r[0] == '0':
    print(0)
else:
    print(r)