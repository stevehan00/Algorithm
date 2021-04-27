n, l = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
idx = 0
start = 0
ans = 0

while idx < len(lst):
    if start == 0:
        start = lst[idx]-0.5
        ans += 1
        idx += 1
        continue
    
    if lst[idx] - start + 0.5 <= l:
        idx += 1
    else:
        start = 0

print(ans)