import sys

n, m =map(int, sys.stdin.readline().split())
pref = []
pref.append([0 for i in range(n+1)])

for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    temp = [0]
    
    for i in range(len(line)):
        temp.append(temp[i]+line[i])

    pref.append(temp)

for _ in range(m):
    instruc = list(map(int, sys.stdin.readline().split()))

    if instruc[0] == 0:
        r = instruc[1]
        c = instruc[2]
        dis = instruc[3] - (pref[r][c]-pref[r][c-1])

        for i in range(c, n+1):
            pref[r][i] += dis
    else:
        sums = 0
        for i in range(instruc[1], instruc[3]+1):
            sums += pref[i][instruc[4]] - pref[i][instruc[2]-1]
        print(sums)