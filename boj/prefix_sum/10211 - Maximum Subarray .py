t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    pref = [0]
    for c in lst:
        pref.append(pref[-1] + c)
    maxs = -1001
    for i in range(len(pref)-1):
        for j in range(i+1, len(pref)):
            maxs = max(maxs, pref[j] - pref[i])
    
    print(maxs)