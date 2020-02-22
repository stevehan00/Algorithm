number = int(input())
lst = []
for i in range(number):
    lst.append(int(input()))
lst.sort()
for i in range(len(lst)):
    print(lst[i])