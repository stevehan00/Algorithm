import sys

n, q = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
pref = [0]
for c in lst:
    pref.append(pref[-1]+c)

for _ in range(q):
    a,b = map(int, sys.stdin.readline().split())
    print(pref[b]-pref[a-1])