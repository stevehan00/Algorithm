import sys

n,h = map(int, sys.stdin.readline().split())
pref = [0 for _ in range(h+1)]

for i in range(2, n//2):
    l = int(sys.stdin.readline())
    r = int(sys.stdin.readline())

    #겹치는 경우
    if l+r > h:
        
    #겹치지 않는 경우
    else:
        pref[1] += 1
        pref[l+1] -= 1
        pref[h-r+1] += 1

