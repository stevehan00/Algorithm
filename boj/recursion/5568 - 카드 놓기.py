import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

sets = set()
lst = []

for _ in range(n):
    a =sys.stdin.readline()[:-1]
    lst.append(a)

pre_val = []
def per(elements, c):
    if c == k:
        sets.add(''.join(pre_val))

    for e in elements:
        nexts = elements[:]
        nexts.remove(e)

        pre_val.append(e)
        per(nexts, c+1)
        pre_val.pop()

per(lst, 0)
print(len(sets))