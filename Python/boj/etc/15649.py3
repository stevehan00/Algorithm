from itertools import permutations

n, m = map(int, input().split())
lst = []
for i in range(1, n+1):
    lst.append(i)

result = list(permutations(lst, m))

for i in result:
    for j in i:
        print(j, end=" ")
    print()