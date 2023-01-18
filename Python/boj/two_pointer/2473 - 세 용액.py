n = int(input())
lst = list(map(int, input().split()))

ans = []

lst.sort()

for i in range(len(lst)-2):
    left, right = i+1, len(lst)-1

    while left < right:
        temp = [abs(lst[i]+lst[left]+lst[right]), (lst[i], lst[left], lst[right])]

        if not ans:
            ans = temp
        
        if (lst[i]+lst[left]+lst[right]) > 0:
            right -= 1
        elif (lst[i]+lst[left]+lst[right]) < 0:
            left += 1
        else:
            ans = temp
            break

        if ans[0] > temp[0]:
            ans = temp

aaa = sorted(list(ans[1]))

print(*aaa)