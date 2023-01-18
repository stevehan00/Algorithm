import sys

sys.setrecursionlimit(10**6)

s = input()
t = input()

def rec(t):
    if len(s) > len(t):
        return
    if s == t:
        print(1)
        exit()
    
    if t[-1] == 'A':
        rec(t[:-1])
    
    if t[0] == 'B':
        rec(t[1:][::-1])

rec(t)
print(0)
