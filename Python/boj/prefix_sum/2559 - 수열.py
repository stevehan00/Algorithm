n,m = map(int, input().split())
lst = list(map(int, input().split()))
pref = [0]

for c in lst:
    pref.append(pref[-1]+c)

maxs = pref[m]
for i in range(m, len(pref)):
    maxs = max(maxs, pref[i]-pref[i-m])

print(maxs)