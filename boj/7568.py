import sys
n = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

rank = [1 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if lst[i][0] > lst[j][0] and lst[i][1] > lst[j][1]:
            rank[j] = rank[j] + 1

for i in rank:
    print(i, end=" ")