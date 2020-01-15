num = int(input())
cnt = 0
lst = list(map(int, input().split()))

for i in lst:
    j = 2
    if i == 1:
        continue
    while j<i:
        if i%j==0:
            break
        j += 1
    else:
        cnt += 1

print(cnt)