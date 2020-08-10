n = int(input())
lst = list(map(int, input().split()))

left, right = 0, len(lst) - 1
ans = lst[left] + lst[right]

lst.sort()

while left < right:
    temp = lst[left] + lst[right]
    if temp > 0:
        right -= 1
        if ans > 0 and ans > temp:
            ans = temp
        elif ans < 0 and -ans > temp:
            ans = temp
    elif temp < 0:
        left += 1
        if ans > 0 and ans > -temp:
            ans = temp
        elif ans < 0 and -ans > -temp:
            ans = temp
    else:
        ans = temp
        break

print(ans)