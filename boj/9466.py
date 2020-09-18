import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    num = nums[x]

    if visited[num]:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return
    else:
        dfs(num)


for _ in range(int(input())):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [True] + [False]*n
    result = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n-len(result))