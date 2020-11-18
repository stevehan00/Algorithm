import sys
n = int(sys.stdin.readline())
lst = sorted([int(sys.stdin.readline()) for _ in range(n)])

for i in lst:
    print(i)