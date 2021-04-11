from collections import defaultdict

n = int(input())

digit = defaultdict(int)
lst = []
maps = []

for _ in range(n):
    line = input()
    lst.append(list(line))
    for i in range(len(line)):
        digit[line[i]] += 10**(len(line) - i - 1)

for k in digit:
    maps.append((k,digit[k]))

maps.sort(key=lambda x:-x[1])
res = dict()
cnt = 9

for c in maps:
    res[c[0]] = cnt
    cnt -= 1

ans = 0
for line in lst:
    size = len(line)
    for i in range(size):
        ans += res[line[i]]*(10**(size-i-1))

print(ans)