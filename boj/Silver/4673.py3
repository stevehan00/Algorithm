def d(n):
    r = n
    for i in str(n):
        r += int(i)
    return r

st = set(range(1,10001))
stt = set()

for i in range(10001):
    stt.add(d(i))

result = sorted(list(st-stt))
for i in result:
    print(i)