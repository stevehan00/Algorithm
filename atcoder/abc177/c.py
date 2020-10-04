import sys
 
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
 
pref = [lst[0]]
for i in range(1, len(lst)):
    pref.append(pref[i-1]+lst[i])
 
ans = 0
for i in range(len(lst)):
    ans += lst[i] * (pref[-1] - pref[i])
 
print(ans%(10**9+7))