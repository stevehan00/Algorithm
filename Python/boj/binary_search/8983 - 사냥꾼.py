import sys

m,n,l = map(int, sys.stdin.readline().split())
m_lst = list(map(int, sys.stdin.readline().split()))
m_lst.sort()

ans = 0

for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    
    leftmost = 0
    left, right = 0, m-1
    
    while left <= right:
        mid = (left + right) // 2
        
        if a < m_lst[mid]:
            right = mid -1
        else:
            leftmost = mid
            left = mid + 1

    if abs(a-m_lst[leftmost])+b <= l:
        ans += 1
    elif leftmost+1 < m and abs(m_lst[leftmost+1]-a)+b <= l:
        ans += 1
    
print(ans)