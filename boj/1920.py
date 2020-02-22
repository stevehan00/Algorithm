import sys

n = int(sys.stdin.readline())
a = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

for i in lst:
    if i in a:  
        print(1)
    else:
        print(0)