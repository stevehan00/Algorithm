t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    cnt = 0
    if a <= 2:
        print(1)
        continue
    else:
        a -= 2
        cnt += 1
 
    if a%b == 0:
        cnt += a//b
    else:
        cnt += a//b+1
 
    print(cnt)