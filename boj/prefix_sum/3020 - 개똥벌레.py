import sys

n,h = map(int, sys.stdin.readline().split())
pref = [0 for _ in range(h+1)]

for i in range(n//2):
    l = int(sys.stdin.readline())
    r = int(sys.stdin.readline())

    if l+r > h:
        pref[1] += 1
        pref[h-r+1] += 1
        pref[l+1] -= 1
    else:
        pref[1] += 1
        pref[l+1] -= 1
        pref[h-r+1] += 1

res = [pref[1]]
mins = sys.maxsize

for c in pref[2:]:
    cur = c + res[-1]
    mins = min(mins, cur)
    res.append(cur)

print(mins, res.count(mins))