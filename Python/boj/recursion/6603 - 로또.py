from itertools import combinations
result = []
while(True):
    s = list(map(int, input().split()))

    if s[0]==0:
        break

    s.pop(0)
    result.append(list(combinations(s, 6)))

for i in result:
    for j in i:
        for k in j:
            print(k, end=' ')
        print()
    print()