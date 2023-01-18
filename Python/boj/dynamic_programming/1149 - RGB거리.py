n = int(input())
lst = []
lst.append(list(map(int, input().split())))

for i in range(1, n):
    temp = list(map(int, input().split()))
    temp[0] = min(lst[i-1][1], lst[i-1][2]) + temp[0]
    temp[1] = min(lst[i-1][0], lst[i-1][2]) + temp[1]
    temp[2] = min(lst[i-1][0], lst[i-1][1]) + temp[2]

    lst.append(temp)
    
print(min(lst[-1]))