import sys
n, m = map(int, sys.stdin.readline().split())

lst = {sys.stdin.readline() for _ in range(n)}
lst2 = {sys.stdin.readline() for _ in range(m)}
lst = lst & lst2
r = sorted(list(lst))

print(len(r))
for i in r:
    print(i, end='')