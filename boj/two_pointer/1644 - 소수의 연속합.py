n = int(input())

lst = [True] * (n+1)
lst[0] = False
lst[1] = False

for i in range(2, int(n**0.5)+1):
    if lst[i] == True:
        for j in range(i*2, n+1, i):
            lst[j] = False
    
prime = [i for i in range(len(lst)) if lst[i] == True]


start, end, sums, cnt = 0, 0, 0, 0

while start < len(prime):
    
    if sums > n or end == len(prime):
        sums -= prime[start]
        start += 1
    
    else:
        sums += prime[end]
        end += 1

    if sums == n:
        cnt += 1

print(cnt)