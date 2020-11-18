import sys
from collections import Counter

num = int(sys.stdin.readline())
lst=[]
for i in range(num):
    lst.append(int(sys.stdin.readline()))

if num == 1:
    print(lst[0])
    print(lst[0])
    print(lst[0])
    print("0")
    exit()

avg = 0
for i in range(num):
    avg += lst[i]

print(round(avg/num)) #1


lst.sort()
print(lst[num//2]) #2

cnt = Counter(lst)
cnt = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))

# 최빈값 출력
if cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])


print(lst[-1]-lst[0]) #4