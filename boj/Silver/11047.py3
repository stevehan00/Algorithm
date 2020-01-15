n, k = map(int, input().split())

coin = []

cnt = 0

for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
for i,value in enumerate(coin):
    if value<=k:
        coin = coin[i:]
        max_v = value
        break

for j in coin:
    a,b = divmod(k, j)
    k -= j*a
    cnt += a

    if k == 0:
        break

print(cnt)