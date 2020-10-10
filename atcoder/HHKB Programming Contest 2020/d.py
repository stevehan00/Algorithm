MOD = 10 ** 9 + 7
 
 
t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
       
    total = (n - a + 1) * (n - a + 1) * (n - b + 1) * (n - b + 1)
    init = b * (a + 1) + (a - 1)
 
    init += (a + b - 1) * (n - (a + b))
 
    total = total - init * init
    if n < a + b:
        print(0)
    else:
        print(total % MOD)