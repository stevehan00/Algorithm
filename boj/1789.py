n = int(input())

cnt = 1

while True:
    n -= cnt
    if n >= 0:
        cnt += 1
    else:
        print(cnt-1)
        break