n, l = map(int, input().split())

cnt = 0
num = 1

while cnt < n:
    if str(l) in str(num):
        num += 1
    else:
        cnt += 1
        num += 1

print(num-1)