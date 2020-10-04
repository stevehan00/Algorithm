import sys, bisect
 
t = int(sys.stdin.readline())
 
for _ in range(t):
    n,s = sys.stdin.readline().split()
    ori = list(n)
    s = int(s)
 
    pref = [int(ori[0])]
 
    for i in range(1, len(ori)):
        pref.append(pref[i-1]+int(ori[i]))
    
    if pref[-1] <= s:
        print(0)
        continue
 
    idx = bisect.bisect_left(pref, s)
 
    ori = ori[idx:]
    temp = 10**len(ori)
    print(temp - int(n[idx:]))