import sys
from collections import defaultdict

n = int(sys.stdin.readline())
dd = defaultdict(list)

cnt = 0

for _ in range(n):
    a,b = sys.stdin.readline().split()
    dd[b].append(a)

    c = a[:2]
    
    if c in dd and c != b:
        for i in dd[c]:
            if i[:2] == b:
                cnt += 1

print(cnt)