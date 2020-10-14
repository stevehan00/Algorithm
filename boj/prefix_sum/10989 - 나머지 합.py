import sys

n = int(sys.stdin.readline())

count = [0]*10001

for _ in range(n):
    c = int(sys.stdin.readline())
    count[c] += 1
    
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)