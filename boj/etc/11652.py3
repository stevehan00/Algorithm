import sys
from collections import Counter

num = int(sys.stdin.readline())
lst = []

for i in range(num):
    lst.append(int(sys.stdin.readline()))

result = Counter(lst).most_common()


same = result[0][1]
idx = 0
for k in range(len(result)):
    if result[k][1] == same:
        idx +=1

min = 2**62
result = result[:idx]

for i in range(idx):
    if result[i][0] <= min:
        min = result[i][0]

print(min)