import sys

n, c = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

#1개
if c in lst:
	print(1)
	exit()

#2개
for i in range(len(lst)):
	temp = c - lst[i]
	if temp in lst and i != lst.index(temp):
		print(1)
		exit()

#3개
lst.sort()
for i in range(len(lst)-2):
    left, right = i+1, len(lst) - 1
    
    while left < right:
        sums = lst[i] + lst[left] + lst[right]

        if sums < c:
            left += 1
        elif sums > c:
            right -= 1
        else:
            print(1)
            exit()


print(0)