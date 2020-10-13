n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]

ps = []
ps.append([0]*(n+1))

for i in range(n):
    line = [0]
    for j in range(n):
        line.append(lst[i][j]+line[j]+ps[i][j+1]-ps[i][j])
    ps.append(line)

maxs = ps[1][1]
for s in range(1, n+1):
    for i in range(s, n+1):
        for j in range(s, n+1):
            sums = ps[i][j] - ps[i-s][j] - ps[i][j-s] + ps[i-s][j-s]
            maxs = max(maxs, sums)

print(maxs)