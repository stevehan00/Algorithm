import sys
from collections import deque

n = int(sys.stdin.readline())
for _ in range(n):
    n, m = map(int, sys.stdin.readline().split())
    ipt = list(map(int, sys.stdin.readline().split()))
    doc = deque([k for k in range(n)])
    cnt = 0
    while True:
        temp = doc.popleft()
        if max(ipt) > ipt[temp]:
            doc.append(temp)
        else:
            ipt[temp] = 0
            cnt += 1

            if temp == m:
                print(cnt)
                break