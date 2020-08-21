from collections import Counter

n = int(input())
lst = []

for _ in range(n):
   lst.append(input())

arr = Counter(lst).most_common()
maxs = arr[0][1]
re = []

for i in range(len(arr)):
    if arr[i][1] == maxs:
        re.append(arr[i][0])
    else:
        break

print(sorted(re)[0])