n = int(input())
lst = list(map(int, input().split()))

left, right = 0, len(lst) - 1
ans = [abs(lst[left] + lst[right]), (lst[left], lst[right])]

lst.sort()

while left < right:
    temp = [abs(lst[left] + lst[right]), (lst[left], lst[right])]
    if lst[left]+lst[right] > 0:
        right -= 1
        if ans[0] > temp[0]:
            ans = temp
    elif lst[left]+lst[right] < 0:
        left += 1
        if ans[0] > temp[0]:
            ans = temp
    else:
        ans = temp
        break

if ans[1][0] > ans[1][1]:
    print(ans[1][1], ans[1][0])
else:
    print(*ans[1])